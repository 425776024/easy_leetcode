class Solution1:
    def hashCode(self, key, HASH_SIZE):
		# 原始方法
        if key == None or len(key) == 0: return -1;
        hashSum = 0
        for i in range(len(key)):
            hashSum += ord(key[i]) * (33 ** (len(key) - i - 1))
        return hashSum % HASH_SIZE


class Solution:
    def hashCode(self, key, HASH_SIZE):
		# 快速方法
        if key == None or len(key) == 0: return -1;
        hashSum = 0
        for i in range(len(key)):
            hashSum = 33 * hashSum + ord(key[i])
            # 既然是取模，后面很大的数也能取模到< HASH_SIZE，为何不每次都取模到<HASH_SIZE，
            # 然后再去做上面的乘法？计算量小很多！
            hashSum %= HASH_SIZE
        return hashSum % HASH_SIZE


'''
(a+b) % p =((a % p)+(b % p))% p
'''

s = Solution()  # 直接计算，缺点，计算量大，可能溢出
s2 = Solution() # 每步取模，一直控制数据在很小的范围内。

print(s.hashCode(key="abcd", HASH_SIZE=1000))
print(s2.hashCode(key="abcd", HASH_SIZE=1000))
