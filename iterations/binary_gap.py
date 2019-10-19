def solution(N):
    binary = "{0:b}".format(N)
    result = 0
    for i in range(1, len(binary) - 1):
        if binary[i] == '0' and binary[i - 1] == '1':
            j = 1
            try:
                while binary[i + j] != '1':
                    j += 1
                if j > result:
                    result = j
            except IndexError:
                pass
    return result 
           

assert solution(9) == 2
assert solution(529) == 4
assert solution(20) == 1
assert solution(15) == 0
assert solution(32) == 0
