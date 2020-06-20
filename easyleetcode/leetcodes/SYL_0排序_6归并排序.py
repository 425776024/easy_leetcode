def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        # 谁小插入谁
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    # 谁还有剩余把谁全部放进去
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])  # 左边并归排序(排好序了）
    right = merge_sort(lists[middle:])  # 右边部分并归排序(排好序了）
    return merge(left, right)  # 合并左边和右边的排序


if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print(merge_sort(a))

