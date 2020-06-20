
def Sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


if __name__ == '__main__':
    arr = Sort([3, 5, 1, 2, 6, 7, 9, 11,22])
    print(arr)
