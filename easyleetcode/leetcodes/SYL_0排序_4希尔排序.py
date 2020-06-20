
def shell(data):
    size = len(data)
    # 最初，一半长度的跳跃对比
    jmp = size // 2
    while jmp != 0:
        for i in range(jmp, size):
            temp = data[i]  # 保留需要插入的数
            j = i - jmp  # i和第一个前方对比的位置j
            while j >= 0 and data[j] > temp:  # 如果前面jmp号元素比后面的大，继续往前面跳jmp部，继续对比
                data[j + jmp] = data[j]  # 后面的替换为前面的
                j = j - jmp  # 到下一个点继续对比
            data[j + jmp] = temp  # 插入点找到，插入数据
        jmp = jmp // 2

if __name__ == '__main__':
    data = [16, 25, 39, 27, 12, 8, 45, 63]
    shell(data)
    print(data)
