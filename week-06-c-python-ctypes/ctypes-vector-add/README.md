# ctypes vector_add dry run

Simple C function compiled as a shared library and called from Python via
`ctypes`, passing NumPy array data directly by pointer.

## Files

- `add.c` — defines `void vector_add(double* A, double* B, double* C, int size)`
- `test.py` — loads `libadd.so`, casts NumPy array pointers, calls the function

## Build and run

```bash
gcc -shared -o libadd.so -fPIC add.c
python3 test.py
```

Expected: prints the elementwise sum of the two input arrays.
