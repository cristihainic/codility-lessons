def solution(A):
    for num in A:
        if A.count(num) % 2 != 0:
            return num

# test cases
x = [9, 3, 9, 3, 9, 7, 9]
y = [9, 9, 3, 3, 9, 7, 7]
z = [42]
assert solution(x) == 7
assert solution(y) == 9
assert solution(z) == 42
