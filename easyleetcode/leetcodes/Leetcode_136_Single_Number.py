
def solution(arr):
    res = 0
    for ai in arr:
        res = res ^ ai
    return res


arr = [1, 2, 2, 1, 3, 4, 4, 5, 3]
print(solution(arr))