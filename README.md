# Qumlib 

A minimal quantum computing simulation library implemented in pure Python.

`qumlib` provides a lightweight statevector-based simulator for constructing and executing quantum circuits using core quantum gates. It is designed for clarity, mathematical correctness, and educational use.

---

## Installation

Install directly from PyPI (works in Google Colab):

```python
!pip install qumlib
```

Verify installation:
```
!pip show qumlib
```

Import the library:
```
from qumlib import Circuit, StatevectorSimulator, gates
```

## Features

1. Statevector-based quantum simulation
2. Core quantum gates (X, Y, Z, H, CNOT)
3. Multi-qubit circuit abstraction
4. Deterministic linear algebra execution
5. Pure NumPy backend
6. Lightweight and dependency-minimal

## Computational Model

For an N-qubit system, the quantum state is represented as:

  ∣𝜓⟩ ∈ 𝐶2𝑁

Quantum gates are applied as unitary matrices expanded via tensor products and multiplied against the global statevector.


## Basic Example (Google Colab)
### 1.Create a superposition state using the Hadamard gate:
```
import numpy as np
from qumlib import Circuit, StatevectorSimulator, gates

# Create 1-qubit circuit
circuit = Circuit(1)

# Apply Hadamard gate
circuit.add_gate(gates.H, target=0)

# Run simulator
simulator = StatevectorSimulator(circuit)
state = simulator.run()

print("Statevector:")
print(state)

print("Probabilities:")
print(np.abs(state) ** 2)
```
Expected output:
```
Statevector:
[0.70710678+0.j  0.70710678+0.j]

Probabilities:
[0.5 0.5]
```
### 2.Apply Pauli-X Gate

```
circuit = Circuit(1)
circuit.add_gate(gates.X, target=0)

simulator = StatevectorSimulator(circuit)
state = simulator.run()
print(state)
```
Expected output:
```
[0.+0.j 1.+0.j]
```
## Project Structure
```
qumlib/
│── .github/
│    └── workflows/
│         └── publish.yml
├── pyproject.toml
├── README.md
├── src/
│   └── qumlib/
│       ├── __init__.py
│       ├── qubit.py
│       ├── gates.py
│       ├── circuit.py
│       └── simulator.py
│
└── tests/
    ├── test_gates.py
    └── test_circuit.py

```
## The architecture separates:

1. Mathematical operators (unitary matrices)
2. Circuit construction layer
3. Execution backend

## Version
```
Current Release: 0.1.0
Distribution: qumlib-0.1.0-py3-none-any.whl
```
## Screenshots:

<img width="1920" height="906" alt="image" src="https://github.com/user-attachments/assets/621f999a-43c7-41f4-bd8d-f717a274a51d" />
<img width="1901" height="902" alt="image" src="https://github.com/user-attachments/assets/45a3081b-8833-4601-8614-76d2a7a56b5c" />

### Google Colab Code with Output:
<img width="1802" height="397" alt="image" src="https://github.com/user-attachments/assets/b824f3b4-4ade-406a-b565-429ede99efdc" />
<img width="1795" height="712" alt="image" src="https://github.com/user-attachments/assets/76f0a41e-a83d-42d3-9e16-789de2445224" />
<img width="1811" height="348" alt="image" src="https://github.com/user-attachments/assets/9c7f4ecc-fe7d-4890-92d9-3798d4ba7403" />


