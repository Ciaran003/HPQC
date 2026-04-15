import numpy as np

def pushQubit(weights):
	global workspace
	workspace = np.reshape(workspace, (1,-1))
	workspace = np.kron(workspace, weights)

def probQubit():
    global workspace
    workspace = np.reshape(workspace,(-1,2)) 
    return np.linalg.norm(workspace,axis=0)**2

def measureQubit():
    global workspace
    prob = probQubit()
    measurement = np.random.choice(2,p=prob)         # select 0 or 1 
    workspace = (workspace[:,[measurement]]/
    np.sqrt(prob[measurement])) 
    return str(measurement)


workspace = np.array([[1. ]])
for n in range(30):
    pushQubit([0.6,0.8])
    print(measureQubit(), end="")
