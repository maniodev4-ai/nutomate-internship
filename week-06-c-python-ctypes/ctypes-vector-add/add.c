void vector_add(double* A, double* B, double* C, int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        C[i] = A[i] + B[i];
    }
}
