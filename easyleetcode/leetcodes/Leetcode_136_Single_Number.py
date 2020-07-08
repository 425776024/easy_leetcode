def solution(arr):
    res = 0
    for ai in arr:
        # 二进制位全相同，为0
        res = res ^ ai
    return res

print(1^2^2)
print(1^2^2^1)
print(1^2^2^1^3)

arr = [1, 2, 2, 1, 3, 4, 4, 5, 3]
print(solution(arr))