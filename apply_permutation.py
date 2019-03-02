from test_framework import generic_test
import copy

def apply_permutation(perm, A):
    # TODO - you fill in here.
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i] # A[i] always stores the value which should be permutated to the desitnation
            tmp = perm[next]
            perm[next] -= len(A)
            next = tmp

    perm[:] = [ p + len(A) for p in perm ]

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
