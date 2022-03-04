import numpy as np
from qiskit import QuantumCircuit

def hsp_oracle(seed, shifted=False, fourier_transformed=False):
    np.random.seed(seed)
    s = f'{np.random.randint(0, 2**6):06b}'
    s = s[::-1]
    n = 6
    oracle = QuantumCircuit(6)
    if shifted:
        for i in range(n):
            if s[i] == '0':
                continue
            else:
                oracle.x(i)
    if fourier_transformed:
        oracle.cz(3,4)
        oracle.cz(4,5)
    else:
        oracle.cz(0,1)
        oracle.cz(1,2)
    for i in range(int(n/2)):
        oracle.cz(i,i+int(n/2))
    if shifted:
        for i in range(n):
            if s[i] == '0':
                continue
            else:
                oracle.x(i)
    if shifted and fourier_transformed:
        oracle.name = 'Oracle g tilde'
    elif shifted:
        oracle.name = 'Oracle g'
    elif fourier_transformed:
        oracle.name = 'Oracle f tilde'
    else:
        oracle.name = 'Oracle f'
    return oracle.to_gate()