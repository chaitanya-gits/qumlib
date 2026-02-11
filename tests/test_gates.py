import numpy as np
from qumlib.gates import X

def test_x_gate():
    state = np.array([1, 0], dtype=complex)
    result = X @ state
    assert np.allclose(result, [0, 1])
