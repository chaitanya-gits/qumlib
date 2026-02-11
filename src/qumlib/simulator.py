import numpy as np

class StatevectorSimulator:
    def __init__(self, circuit):
        self.circuit = circuit
        self.state = np.zeros(2 ** circuit.num_qubits, dtype=complex)
        self.state[0] = 1

    def run(self):
        for gate, target in self.circuit.operations:
            self.apply_gate(gate, target)
        return self.state

    def apply_gate(self, gate, target):
        # Minimal example: single-qubit only
        n = self.circuit.num_qubits
        full_gate = 1
        for i in range(n):
            if i == target:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, np.eye(2))
        self.state = full_gate @ self.state
