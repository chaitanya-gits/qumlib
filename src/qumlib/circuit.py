import numpy as np
from .gates import X, H

class Circuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.operations = []

    def add_gate(self, gate, target):
        self.operations.append((gate, target))
