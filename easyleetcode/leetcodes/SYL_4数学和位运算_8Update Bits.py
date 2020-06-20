

def updateBits(n, m, i, j):
    ones = ~0
    mask = 0
    if j < 31:
        # 得到第i位到第j位的比特位为0，而其他位均为1的掩码mask。(1111...000...111)
        left = ones << (j + 1)
        right = ((1 << i) - 1)
        mask = left | right
    else:
        mask = (1 << i) - 1
    # mask与 N 进行按位与，清零 N 的第i位到第j位。
    # M 右移i位，将 M 放到 N 中指定的位置。
    # 返回 N | M 按位或的结果。
    return (n & mask) | (m << i)


a = -521, 0, 31, 10
print(updateBits(*a))
