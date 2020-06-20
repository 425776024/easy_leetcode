
def Sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


if __name__ == '__main__':
    arr = [1, 4, 3, 7, 8, 10, 9, 2, 11]
    Sort(arr)
    print(arr)
