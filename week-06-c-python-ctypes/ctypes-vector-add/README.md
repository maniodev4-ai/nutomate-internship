# ctypes vector_add dry run

Simple C function compiled as a shared library and called from Python via
`ctypes`, passing NumPy array data directly by pointer. This is a dry run
ahead of interfacing with `nuLASCL` (NUCES OpenCL-based linear algebra
library) from Python.

## Files

- `add.c` — defines `void vector_add(double* A, double* B, double* C, int size)`
- `test.py` — loads `libadd.so`, casts NumPy array pointers, calls the function

## Build and run

```bash
gcc -shared -o libadd.so -fPIC add.c
python3 test.py
```

## Output
[11. 22. 33. 44. 55.]
Confirms `A + B` computed correctly in C and read back into the NumPy
array `C`, with no explicit return value needed — the C function writes
directly into memory Python already owns via the pointer passed in.

## Environment

- Ubuntu (WSL)
- Python 3, virtual environment (`venv`)
- NumPy (see `requirements.txt` at repo root)
- gcc
