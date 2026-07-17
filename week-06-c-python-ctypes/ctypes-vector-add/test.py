import ctypes
import numpy as np

lib = ctypes.CDLL("./libadd.so")

lib.vector_add.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]
lib.vector_add.restype = None

size = 5
A = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
B = np.array([10.0, 20.0, 30.0, 40.0, 50.0], dtype=np.float64)
C = np.zeros(size, dtype=np.float64)

ptr_A = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
ptr_B = B.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
ptr_C = C.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

lib.vector_add(ptr_A, ptr_B, ptr_C, size)

print(C)
