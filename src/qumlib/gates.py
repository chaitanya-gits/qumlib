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

CH = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1/np.sqrt(2), 1/np.sqrt(2)],
<<<<<<< HEAD
    [0,0,1/np.sqrt(2), -1/np.sqrt(2)]], dtype=complex)
=======
    [0,0,1/np.sqrt(2), -1/np.sqrt(2)]
], dtype=complex)
>>>>>>> 291db6251c9931f0544cd8d32ac8bbb218154061

CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
<<<<<<< HEAD
    [0,0,1,0]], dtype=complex)
=======
    [0,0,1,0]
], dtype=complex)
>>>>>>> 291db6251c9931f0544cd8d32ac8bbb218154061

CZ = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
<<<<<<< HEAD
    [0,0,0,-1]], dtype=complex)
=======
    [0,0,0,-1]
], dtype=complex)
>>>>>>> 291db6251c9931f0544cd8d32ac8bbb218154061

SWAP = np.array([
    [1,0,0,0],
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,1]], dtype=complex)

CCX = np.array([
      [1,0,0,0,0,0,0,0],
      [0,1,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0],
      [0,0,0,1,0,0,0,0],
      [0,0,0,0,1,0,0,0],
      [0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,1],
<<<<<<< HEAD
      [0,0,0,0,0,0,1,0]], dtype=complex)
=======
      [0,0,0,0,0,0,1,0]
  ], dtype=complex)
>>>>>>> 291db6251c9931f0544cd8d32ac8bbb218154061
