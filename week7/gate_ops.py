import numpy as np

def pushQubit(weights):
    global workspace
    workspace = np.reshape(workspace,(1,-1))
    workspace = np.kron(workspace,weights)

workspace = np.array([[1.]])
pushQubit([1,0])
#print(workspace)
pushQubit([3/5,4/5])
#print(workspace)

def applyGate(gate):
    global workspace
    workspace = np.reshape(workspace,(-1,gate.shape[0]))     
    np.matmul(workspace,gate.T,out=workspace)

X_gate = np.array([[0, 1],                      # Pauli X gate
                   [1, 0]])                     # = NOT gate

Y_gate = np.array([[ 0,-1j],                    # Pauli Y gate
                   [1j,  0]])                   # = SHZHZS
  
Z_gate = np.array([[1, 0],                      # Pauli Z gate
                   [0,-1]])                     # = P(pi) = S^2
                                                # = HXH

H_gate = np.array([[1, 1],                      # Hadamard gate 
                   [1,-1]]) * np.sqrt(1/2)

S_gate = np.array([[1, 0],                      # Phase gate
                   [0,1j]])                     # = P(pi/2) = T^2
                   
T_gate = np.array([[1,                0],       # = P(pi/4)
                   [0,np.exp(np.pi/-4j)]])
                   
Tinv_gate = np.array([[1, 0],                   # = P(-pi/4) 
                      [0,np.exp(np.pi/4j)]])    # = T^-1
                      
def P_gate(phi):                                # Phase shift gate
    return np.array([[1,             0],
                     [0,np.exp(phi*1j)]])
                     
def Rx_gate(theta):                             # Y rotation gate
    return np.array([[np.cos(theta/2),-1j*np.sin(theta/2)],
                     [-1j*np.sin(theta/2),np.cos(theta/2)]])
                     
def Ry_gate(theta):                             # Y rotation gate return 
    np.array([[np.cos(theta/2),-np.sin(theta/2)],
              [np.sin(theta/2), np.cos(theta/2)]])
              
def Rz_gate(theta):                             # Z rotation gate 
    return np.array([[np.exp(-1j*theta/2),                0],
                     [                  0,np.exp(1j*theta/2)]])
                     
CNOT_gate = np.array([[1, 0, 0, 0],             # Ctled NOT gate
                      [0, 1, 0, 0],             #=XORgate
                      [0, 0, 0, 1],
                      [0, 0, 1, 0]])
                      
CZ_gate = np.array([[1, 0, 0, 0],               # Ctled Z gate
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0,-1]])
                    
SWAP_gate = np.array([[1, 0, 0, 0],             # Swap gate
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]])
                      
TOFF_gate = np.array([[1, 0, 0, 0, 0, 0, 0, 0], # Toffoli gate
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0, 0, 1, 0]])


def gate_choice(value):
    global workspace
    if value=="1":
        workspace=np.array([[1.]])
		pushQubit([1,0])
		print(f"before gate: {workspace}")
		applyGate(X_gate)
		print(f"after gate: {workspace}")

    elif value=="2":
        workspace = np.array([[1.+0j]])
        pushQubit([1, 0])
        print(f"before gate: {workspace}")
        applyGate(Y_gate)
        print(f"after gate: {workspace}")

    elif value == "3":
        workspace = np.array([[1.]])
        pushQubit([1, 0])
        print(f"before gate: {workspace}")
        applyGate(Z_gate)
        print(f"after gate: {workspace}")

    elif value == "4":
        workspace = np.array([[1.]])
        pushQubit([1, 0])
        print("before:", workspace)
        applyGate(H_gate)
        print("after: ", workspace)

    elif value == "5":
        workspace = np.array([[1.+0j]])
        pushQubit([1, 0])
        print("before:", workspace)
        applyGate(S_gate)
        print("after: ", workspace)

    elif value == "6":
        workspace = np.array([[1.+0j]])
        pushQubit([1, 0])
		applyGate(H_gate)
        print("before:", workspace)
        applyGate(T_gate)
        print("after: ", workspace)

value = input("choose gate between 1-6: ").strip()
gate_choice(value)

