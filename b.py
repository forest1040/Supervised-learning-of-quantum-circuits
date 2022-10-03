import random
import numpy as np

N = 11 # Number of qubits
P = 6 # Number of gates per qubit

for j in range(P): # Loop over the gates layers
    col = np.zeros(N)

    # CX Layer
    isCXSelected = False
    for i in range(N):
        if col[i] != 3: # It is not the target of the CX-gate
            listemp = []
            if isCXSelected == False: # There isn't a CX-gate in this layer of gates
                r = random.randint(0, 2) # Random choice between H, T and the control of the CX-gate
                listemp.append(r)
                if r == 2: # If it is the control of the CX-gate
                    r2 = random.randint(1, N - 1)
                    t = (i + r2) % N # This is the target of the CX-gate
                    listemp.append(t)
                    col[i]=r
                    isCXSelected = True # Now there is a CX-gate in this layer of gates
                    col[listemp[1]] = 3

    print(col)

# 上位ビットをtargetとするCNOTがない
# CNOTは1階層につき1個しかない

# モデルに対して、NとPが固定
# 回路の推定は特別ルールで生成したトレインデータから抽出したデータ

# TODO
# - 2D回路の制限を入れたい
