import numpy as np
from qiskit import QuantumCircuit

def hsp_oracle(
    seed: int, 
    output: bool=False, 
    shifted: bool=False, 
    fourier_transformed: bool=False
) -> QuantumCircuit:
    """
    Returns 4-qubit hidden shift problem oracle according to input options.
    Args:
        seed (int): the seed for the random shift string s.
        output (bool): if true, returns a 5-qubit circuit with the output register.
        shifted (bool): if true, apply the shift operation on both sides of the function.
        fourier_transformed (bool): if true, apply the Fourier transformed function instead.
    Returns:
        QuantumCircuit: oracle circuit with 4-qubit if ouput==False, 5-qubit if output==True.
    """
    
    np.random.seed(seed)
    s = f'{np.random.randint(0, 2**4):4b}'
    s = s[::-1]
    n = 4
    oracle = QuantumCircuit(4+output)
    
    # Apply the shift operation according to 'shifted'
    if shifted:
        for i in range(n):
            if s[i] == '1':
                oracle.x(i+output)
    
    # Apply the function according to output
    # f(x, y) = x·y = tilde f(x, y)
    if output:
        oracle.ccx(1,3,0)
        oracle.ccx(2,4,0)
    else:
        oracle.cz(0,2)
        oracle.cz(1,3)
    
    # Apply the shift operation according to 'shifted'
    if shifted:
        for i in range(n):
            if s[i] == '1':
                oracle.x(i+output)
    
    # Name the oracle
    if shifted and fourier_transformed:
        oracle.name = 'Oracle g tilde'
    elif shifted:
        oracle.name = 'Oracle g'
    elif fourier_transformed:
        oracle.name = 'Oracle f tilde'
    else:
        oracle.name = 'Oracle f'
    
    return oracle.to_gate()