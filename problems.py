import numpy as np
from qiskit import QuantumCircuit

def hsp_oracle(seed, shifted=False, fourier_transformed=False):
    np.random.seed(seed)
    s = np.random.randint(0, 2**6)
    oracle = QuantumCircuit(6)
    if shifed and fourier_transformed:
        oracle.name = 'shifted fourier f'
    elif shifted:
        oracle.name = 'shifted f'
    elif fourier_transformed:
        oracle.name = 'fourier f'
    else:
        oracle.name = 'f'
    s = bin(s)
    s = s[2:]
    s = s[::-1]

    if shifted:
        for i in range(len(s)):
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

    oracle.cz(0,3)
    oracle.cz(1,4)
    oracle.cz(2,5)
    
    if shifted:  
        for i in range(len(s)):
            if s[i] == '0':
                continue
            else:
                oracle.x(i)
    

    return oracle.to_gate()