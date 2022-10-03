from qulacs import QuantumCircuit, QuantumState
import random
import numpy as np

flag = 0
#num_circuits = 1000000 #Number of quantum circuits that will be simulated
num_circuits = 10000 #Number of quantum circuits that will be simulated
N = 11 # Number of qubits
P = 6 # Number of gates per qubit

filei = open(f'qdata/input_N{N}_P{P}.dat','w')
fileo = open(f'qdata/output_N{N}_P{P}.dat','w')

circ = np.zeros((N,P))
for n in range(num_circuits):
    if n % 100 == 0:
        print(n)
    
    qc = QuantumCircuit(N)  
    state = QuantumState(N)

    for j in range(P): # Loop over the gates layers
        col = np.zeros(N)
        countarget = 0
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
        for i in range(N): # We build the j-th layer of gates
            if col[i] == 0:
                qc.add_T_gate(i)
            elif col[i] == 1:
                qc.add_H_gate(i)
            elif col[i] == 2:
                qc.add_CNOT_gate(i, t)

         # We store the gates that we have generated in a list           
        circ[:,j] = col
        flag = 0
        
    # Simulation of the quantum circuit
    qc.update_quantum_state(state)
    
    # Write on files
    for i in range(N):
        for j in range(P): 
            filei.write(f'{circ[i][j]}\n')
    filei.write('\n')
    for j in range(N):
        fileo.write(f'{state.get_zero_probability(j)}\n')
    fileo.write('\n')

fileo.close()
filei.close()
