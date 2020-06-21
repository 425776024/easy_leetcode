def updateBits(n, m, i, j):
# 	-1，全1
    ones = ~0
# 	全0
    mask = 0
    if j < 31:
        # 得到第i位到第j位的比特位为0，而其他位均为1的掩码mask。(1111...000...111)
		# 111..0000
        left = ones << (j + 1)
		# 000...1111 :(000...10000 - 1 = 000...01111)
        right = ((1 << i) - 1)
		# 1111...000...1111
        mask = left | right
    else:
# 		在j为31时j + 1为32，也就是说此时对left位移的操作已经超出了此时int的最大位宽：左边被消除了
        mask = (1 << i) - 1

    # mask与 N 进行按位与，清零 N 的第i位到第j位。
    # M 右移i位，将 M 放到 N 中指定的位置。
    # 返回 N | M 按位或的结果。
    return (n & mask) | (m << i),mask

'''
0b10000000000
    0b10101
      i   j
0b10001010100
'''

if __name__=='__main__':

	a = 1024, 21, 2, 6


	print(bin(1024))
	print(' '*3,bin(21))
	print(' '*5,'i',' '*1,'j')

	s=updateBits(*a)
	print(bin(s[1]))
	print(bin(s[0]))
