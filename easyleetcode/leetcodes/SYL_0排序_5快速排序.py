
def Partion(arr, left, right):
    # 一次对比操作，返回中间索引（索引前面比他小，后面比他大）
    tag = right # 作为判断点，一轮后，比他小的会到他前面，比他大的在他后面
    center = arr[tag]
    while left < right:
        while left < right and arr[left] <= center:
            left += 1
        while left < right and arr[right] >= center:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[tag] = arr[tag], arr[left]
    return left


def quickSort(arr):
    left = 0
    right = len(arr) - 1
    # 多伦操作的索引记录数组，这样做避免递归写法
    stack = []
    # 初始时，对最左、右的进行一轮Partion
    stack.append([left, right])
    while len(stack) != 0:
        pos = stack.pop()
        center_i = Partion(arr, pos[0], pos[1])
        if center_i - 1 > pos[0]:
            stack.append([pos[0], center_i - 1])
        if center_i + 1 < pos[1]:
            stack.append([center_i + 1, pos[1]])


if __name__ == '__main__':
    data = [16, 25, 39, 27, 12, 8, 45, 63]
    quickSort(data)
    print(data)
