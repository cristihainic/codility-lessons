def solution(A):
    nums = ''.join(str(i) for i in A)
    for num in nums:
        if nums.count(num) % 2 != 0:
            return int(num)

# test cases
x = [9, 3, 9, 3, 9, 7, 9]
y = [9, 9, 3, 3, 9, 7, 7]
assert solution(x) == 7
assert solution(y) == 9
