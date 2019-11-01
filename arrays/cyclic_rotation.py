def solution(A, K):
    return A[-K:] + A[:-K]

# test cases
A, K = [3, 8, 9, 7, 6], 3
assert solution(A, K) == [9, 7, 6, 3, 8]

A, K = [0, 0, 0], 1
assert solution(A, K) == [0, 0, 0]

A, K = [1, 2, 3, 4], 4
assert solution(A, K) == [1, 2, 3, 4]

