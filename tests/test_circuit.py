import numpy as np
from qumlib import Circuit, StatevectorSimulator, gates


def test_single_qubit_hadamard():
    circuit = Circuit(1)
    circuit.add_gate(gates.H, target=0)

    simulator = StatevectorSimulator(circuit)
    result = simulator.run()

    expected = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=complex)
    assert np.allclose(result, expected)


def test_single_qubit_x_gate():
    circuit = Circuit(1)
    circuit.add_gate(gates.X, target=0)

    simulator = StatevectorSimulator(circuit)
    result = simulator.run()

    expected = np.array([0, 1], dtype=complex)
    assert np.allclose(result, expected)


def test_two_qubit_identity_initialization():
    circuit = Circuit(2)
    simulator = StatevectorSimulator(circuit)

    result = simulator.run()

    expected = np.array([1, 0, 0, 0], dtype=complex)
    assert np.allclose(result, expected)
