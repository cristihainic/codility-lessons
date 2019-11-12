def solution(X, Y, D):
    steps = 0
    while Y > X:
        steps += 1
        Y -= D
    return steps 




# test cases
assert solution(10, 85, 30) == 3
