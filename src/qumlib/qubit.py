import numpy as np

class Qubit:
    def __init__(self, state=None):
        if state is None:
            self.state = np.array([1+0j, 0+0j])
        else:
            state = np.array(state, dtype=complex)
            norm = np.linalg.norm(state)
            if not np.isclose(norm, 1):
                raise ValueError("Statevector must be normalized.")
            self.state = state

    def apply(self, gate):
        self.state = gate @ self.state
