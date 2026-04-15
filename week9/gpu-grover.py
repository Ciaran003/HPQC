import time
import numpy as np
import torch as pt

pt.autograd.set_grad_enabled(False)

# Device setup

if pt.cuda.is_available():
    dev= pt.device("cuda")
    print("GPU available")
else:
    dev= pt.device("cpu")
    print("Sorry, only CPU available")

workspace = pt.tensor([[1.0]], device=dev, dtype=pt.float32)
namestack = []

X_gate = np.array([[0, 1],                      # Pauli X gate
                   [1, 0]])                     # = NOT gate

Y_gate = np.array([[ 0,-1j],                    # Pauli Y gate
                   [1j,  0]])                   # = SHZHZS
  
Z_gate = np.array([[1, 0],                      # Pauli Z gate
                   [0,-1]])                     # = P(pi) = S^2
                                                # = HXH

H_gate = np.array([[1, 1],                      # Hadamard gate 
                   [1,-1]]) * np.sqrt(1/2)

def pushQubit(name,weights):
    global workspace
    global namestack
    if (workspace.shape[0],workspace.shape[1]) == (1,1): #!
        namestack = []                                   # reset if workspace empty 
    namestack.append(name)
    weights = weights/np.linalg.norm(weights)            # normalize 
    weights = pt.tensor(weights,device=workspace.device, #!
                        dtype=workspace[0,0].dtype)      #! 
    workspace = pt.reshape(workspace,(1,-1))             #! 
    workspace = pt.kron(workspace,weights)               #!
    
def tosQubit(name):
    global workspace
    global namestack
    k = len(namestack)-namestack.index(name)                  # position of qubit 
    if k > 1:                                                 # if non-trivial
        namestack.append(namestack.pop(-k))
        workspace = pt.reshape(workspace,(-1,2,2**(k-1)))     #! 
        workspace = pt.swapaxes(workspace,-2,-1)              #!
        
def applyGate(gate,*names):
    global workspace
    if list(names) != namestack[-len(names):]:                # reorder stack
        for name in names:                                    # if necessary 
            tosQubit(name)
    workspace = pt.reshape(workspace,(-1,2**len(names)))      #!
    subworkspace = workspace[:,-gate.shape[0]:]
    gate = pt.tensor(gate.T,device=workspace.device,          #! 
                     dtype=workspace[0,0].dtype)              #! 
    if workspace.device.type == 'cuda':                       #! 
        pt.matmul(subworkspace,gate,out=subworkspace)         #!
    else:    #! workaround for issue #114350 in torch.matmul 
        subworkspace[:,:]=pt.matmul(subworkspace,gate) #!
        
def probQubit(name):                             # Check probabilities
    global workspace                             # of qubit being 0 or 1
    tosQubit(name)                               # qubit to TOS
    workspace = pt.reshape(workspace,(-1,2))     #! to 2 cols
    prob = pt.linalg.norm(workspace,axis=0)**2   #! compute prob 
    prob = pt.Tensor.cpu(prob).numpy()           #! convert to numpy
    return prob/prob.sum()                       # make sure sum is one
    
def measureQubit(name):                          # Measure and pop qubit
    global workspace
    global namestack
    prob = probQubit(name)                      # Compute probabilities
    measurement = np.random.choice(2,p=prob)    # 0 or 1 
    workspace = (workspace[:,[measurement]]/    # extract col
                 np.sqrt(prob[measurement])) 
    namestack.pop()                             # pop stacks
    return measurement
    
def sample_phaseOracle(qubits):          # sample function 
        # if all f(x)==1 return -weight else return weight
    applyGate(X_gate,qubits[1])          # negate qubit 1
    applyGate(Z_gate,*namestack)         # controlled Z gate
    applyGate(X_gate,qubits[1])          # restore qubit 1

def zero_phaseOracle(qubits):            # all qubits zero? 
    # if all qubits==0 return -weight else return weight
    for qubit in qubits:                 # negate all inputs
        applyGate(X_gate,qubit)
    applyGate(Z_gate,*namestack)         # controlled Z gate
    for qubit in qubits:                 # restore inputs
        applyGate(X_gate,qubit)

def zero_booleanOracle(qubits,result): # all qubits zero? 
    # if all qubits==0 return 1 else return 0
    for qubit in qubits:             # negate all inputs
        applyGate(X_gate,qubit)
    TOFFn_gate(qubits,result)        # compute AND
    for qubit in qubits:             # restore inputs
        applyGate(X_gate,qubit)

def groverSearch(n, printProb=True):
    optimalTurns = int(np.pi/4*np.sqrt(2**n)-1/2)   # iterations 
    qubits = list(range(n))                         # generate qubit names
    for qubit in qubits:                            # initialize qubits
        pushQubit(qubit,[1,1])
    for k in range(optimalTurns):                   # Grover iterations:
        sample_phaseOracle(qubits)                  # apply phase oracle
        for qubit in qubits:                        # H-gate all qubits
            applyGate(H_gate,qubit) 
        zero_phaseOracle(qubits)                    # apply 0 phase oracle
        for qubit in qubits:                        # H-gate all qubits
            applyGate(H_gate,qubit) 
        if printProb:                               # peek probabilities
            print(probQubit(qubits[0]))             # to show convergence
    for qubit in reversed(qubits):                  # print result 
        result=measureQubit(qubit)
        print(result,end="")

import time
workspace = pt.tensor([[1.]],device=dev,
                             dtype=pt.float32) 
t = time.process_time()                               # with GPU
t1 = time.perf_counter()
groverSearch(16, printProb=False)                     # skip prob printouts 
print("\CPU time:", time.process_time() - t, "s")
print("Elapsed:", time.perf_counter() - t1, "s")

