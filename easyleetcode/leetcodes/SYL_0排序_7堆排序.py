def sort(array):
    # 遍历非叶子节点，建立堆结构数组
    for i in range(int(len(array) / 2) - 1, -1, -1):
        adjustHeap(array, i, len(array))

    print('arr of heap:', array)
    # 堆积树建立完成，开始排序。
    for j in range(len(array) - 1, 0, -1):
        # 一开始最大元素是[0]，然后被换到最后一个
        # 从n-0，不断和[0]元素交换，重新堆排序（既把第2、3..n大的翻转到最上面）
        array[0], array[j] = array[j], array[0]
        adjustHeap(array, 0, j)


def adjustHeap(array, i, length):
    # 对第i号进行堆调整
    # 获取非叶子节点的数据
    temp = array[i]
    # 非叶子节点的左子节点
    k = 2 * i + 1
    # 遍历对比k后面的节点，把temp放入合理位置
    while k < length:
        #  k + 1 < length 确保有左右节点才比较
        if k + 1 < length and array[k] < array[k + 1]:  # 如果左子节点比右子节点小，k就切换到右子节点
            k += 1
        # 如果子节点有更大的
        if array[k] > temp:
            # 父节点替换为更大的
            array[i] = array[k]
            # 记录当前最大点位置
            i = k
        else:  # 直接打断，因为堆特点，后面层的更不满足
            break
        # k切换到下一个左子节点
        k = 2 * k + 1
    # 此时i是空位，i上层的都比temp大，temp放到这里
    array[i] = temp


if __name__ == '__main__':
    data = [16, 25, 39, 27, 12, 8, 45, -10, 63]
    print('arr', data)
    print('start max heap sort')
    sort(data)
    print('arr sorted:', data)
