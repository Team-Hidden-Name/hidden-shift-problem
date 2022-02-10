# hidden-shift-problem
1. The Hidden Shift Problem

 The hidden shift problem is an oracle-based problem where the quantum solution shows exponential speedup. We can model some generally used cryptosystems like Poly1305 and CSIDH by the hidden shift problem, and it is also employed to benchmark quantum computers and classical simulators.

2.1Super oracle algorithm

 In case fourier transform of function $f$ is given this algorithm can be used 

![A1 algorithm](https://user-images.githubusercontent.com/69569033/153343222-b2a6037d-675e-4922-9391-c251f5f3968b.png)


2.2Qiskit Implementation- super oracle algorithm
  
 We'll now walk through the hidden-shift algorithm implementation in Qiskit for a six bit string s= 1011. We first set the number of qubits used in the experiment, and the hidden bit string  to be found by the algorithm. The hidden bit string  together with the function  f determines the circuit for the quantum oracle
 
![image](https://user-images.githubusercontent.com/69569033/153343017-ab2c5348-b638-4b65-8a86-2731423e6157.png)
 
 
 3.1
![image](https://user-images.githubusercontent.com/69569033/153345283-ab8cb69e-b706-42f4-800d-6505a5866ce9.png)







