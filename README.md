# Qiskit Hackathon Korea 2022 (Feb.7 - Feb.10)
[Issue #13 Implement the algorithm for the hidden shift problem and explain it!](https://github.com/qiskit-community/qiskit-hackathon-korea-22/issues/13)

# Team Hidden Name

## Abstract
- Study algorithms for the hidden shift problem
- Implement it by Qiskit
- Make it easy to understand!

## Description
The hidden shift problem is closely related to the dihedral hidden subgroup problem.
Understanding this problem can lead to deeper insights into those related problems and also into the cryptographic use-cases.
Implementing this algorithm via Qiskit and explaining it would be beneficial for us, and also for the Qiskit community!

We aim to make a tutorial notebook file that describes the hidden shift problem and shows how to implement it by Qiskit.

### Reference
1. S. Bravyi & D. Gosset (2016), "Improved classical simulation of quantum circuits dominated by Clifford gates", Phys. Rev. Lett. 116, 250501, [doi:10.1103/PhysRevLett.116.250501](https://doi.org/10.1103/PhysRevLett.116.250501), [arXiv:1601.07601](https://arxiv.org/abs/1601.07601) [quant-ph]
2. M. Roetteler (2008), "Quantum algorithms for highly non-linear Boolean functions", Proceedings of the 21st Annual ACM-SIAM Symposium on Discrete Algorithms (SODA'10), pp. 448-457, [arXiv:0811.3208](https://arxiv.org/abs/0811.3208) [quant-ph]
3. X. Bonnetain & M. Naya-Plasencia (2018), "Hidden Shift Quantum Cryptanalysis and Implications", In: T. Peyrin , S. Galbraith (eds) Advances in Cryptology – ASIACRYPT 2018, Lecture Notes in Computer Science, vol 11272, Springer, Cham, [doi:10.1007/978-3-030-03326-2_19](https://doi.org/10.1007/978-3-030-03326-2_19)
4. K. Wright, K. M. Beck, S. Debnath et al. (2019), "Benchmarking an 11-qubit quantum computer", Nat Commun 10, 5464, [doi:10.1038/s41467-019-13534-2](https://doi.org/10.1038/s41467-019-13534-2)

## Members
 - Boseong Kim [@BStar14](https://github.com/BStar14) - Slack: `@BoSeong Kim` email: `boseong14@gmail.com`
 - Inhyuk Oh [@OHINHYUK55](https://github.com/OHINHYUK55)
 - Sekang Kwon [@skk9967](https://github.com/skk9967)
 - Sehoon Bang [@hackathon-bsh](https://github.com/hackathon-bsh)
 - Junghun Phee [@BiPhee](https://github.com/BiPhee)

## Mentors
 - Prof. Hyukjoon Kwon [@hjkwon9001](https://github.com/hjkwon9001)
 - Dr. Adel Sohbi [@adelshb](https://github.com/adelshb)

---

## Hidden Shift Problem

### The Hidden Shift Problem

The hidden shift problem is an oracle-based problem where the quantum solution shows exponential speedup. We can model some generally used cryptosystems like Poly1305 and CSIDH by the hidden shift problem, and it is also employed to benchmark quantum computers and classical simulators.

### Super-oracle algorithm

In case fourier transform of function f is given this algorithm can be used

![A1 algorithm](https://user-images.githubusercontent.com/69569033/153343222-b2a6037d-675e-4922-9391-c251f5f3968b.png)

### Qiskit Implementation: super-oracle algorithm

We'll now walk through the hidden-shift algorithm implementation in Qiskit for a six bit string s= 1011. We first set the number of qubits used in the experiment, and the hidden bit string  to be found by the algorithm. The hidden bit string  together with the function f determines the circuit for the quantum oracle

![image](https://user-images.githubusercontent.com/69569033/153343017-ab2c5348-b638-4b65-8a86-2731423e6157.png)

### Qiskit Implementation: general oracle algorithm

![image](https://user-images.githubusercontent.com/69569033/153345283-ab8cb69e-b706-42f4-800d-6505a5866ce9.png)

### Experiment with Real Devices: general oracle algorithm

We can run the circuit on the real device and get experiment results as below.

![image](https://user-images.githubusercontent.com/69569033/153345562-14df7e84-e0af-4d3d-8db1-415082066d0b.png)






