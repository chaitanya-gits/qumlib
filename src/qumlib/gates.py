import numpy as np

X = np.array([[0, 1],
              [1, 0]], dtype=complex)

Y = np.array([[0, -1j],
              [1j, 0]], dtype=complex)

Z = np.array([[1, 0],
              [0, -1]], dtype=complex)

H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]], dtype=complex)

I = np.array([[1, 0],
              [0, 1]], dtype=complex)

T = np.array([[1, 0],
              [0, np.exp(1j * np.pi / 4)]], dtype=complex)

S = np.array([[1, 0],
              [0, 1j]], dtype=complex)

CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
], dtype=complex)

CZ = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,-1]
], dtype=complex)

SWAP = np.array([
    [1,0,0,0],
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,1]], dtype=complex)

CXX = np.array([
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,-1j,-1j,-1j,-1j],
    [0,0,0,-1j,-1j,-1j,-1j,-1j],
    [0,-1j,-1j,-1j,-1j,-1j,-1j,-1j],
    [-1j,-1j,-1j,-1j,-1j,-1j,-1j,-1j]
], dtype=complex)