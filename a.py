import random
import numpy as np

N = 11 # Number of qubits
P = 6 # Number of gates per qubit

for j in range(P): # Loop over the gates layers
    col = np.zeros(N)
    countarget = 0
    flag = 0
    for i in range(N):
        if col[i] != 3: # It is not the target of the CX-gate
            listemp = []
            if flag == 0: # There isn't a CX-gate in this layer of gates
                r = random.randint(0, 2) # Random choice between H, T and the control of the CX-gate
                listemp.append(r)
                if r == 2: # If it is the control of the CX-gate
                    r2 = random.randint(1, N - 1)
                    t = (i + r2) % N # This is the target of the CX-gate
                    listemp.append(t)
            else: # If the CX-gate has been defined, only 1-qubit gate can be added in this layer of gates
                r = random.randint(0, 1)
                listemp.append(r)               
            col[i]=listemp[0]
            if len(listemp) == 2:
                flag = 1 # Now there is a CX-gate in this layer of gates
                col[listemp[1]] = 3
