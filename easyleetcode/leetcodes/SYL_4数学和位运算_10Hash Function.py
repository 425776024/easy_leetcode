

class Solution1:
    def hashCode(self, key, HASH_SIZE):
        if key == None or len(key) == 0: return -1;
        hashSum = 0
        for i in range(len(key)):
            hashSum += ord(key[i]) * (33 ** (len(key) - i - 1))
        return hashSum % HASH_SIZE


class Solution:
    def hashCode(self, key, HASH_SIZE):
        if key == None or len(key) == 0: return -1;
        hashSum = 0
        for i in range(len(key)):
            hashSum = 33 * hashSum + ord(key[i])
            # 既然是取模，后面很大的数也能取模到< HASH_SIZE，为何不每次都取模到<HASH_SIZE，
            # 然后再去做上面的乘法？计算量小很多！
            hashSum %= HASH_SIZE
        return hashSum % HASH_SIZE


'''
不必要总数算得那么大了，再最后取模！。
最终总数和是：1xxx无穷个0xxx 8 % 10 = 8，
和每次总数涨一点点，就尝试 xi % 10 不一样吗
 (2+3+4+5) % 2 = 14 % 2=0 和 ((((((2 %2 =0）+3) %2 =1) +4 )%2=1) + 5)%2 =0


输入:  key = "abcd", size = 1000
输出: 97
样例解释：(97 * 33^3 + 98*33^2 + 99*33 + 100*1)%1000 = 978
        (33 * 0 + 97)    %100 = 97
        (97 * 33 + 98)   %100 = 
        (((97 * 33 + 98)   %100) * 33 + 99)   % 100 = 97*33^2 % 100 + 98*33 % 100 + 99 % 100 
        (((97 * 33 + 98)   %100) % 100 * (33 %100) + 99 %100)   % 100 = 

(a+b) % p =((a % p)+(b % p))% p
'''

s = Solution()  # 直接计算，缺点，计算量大
s2 = Solution()

print(s.hashCode(key="abcd", HASH_SIZE=1000))
print(s2.hashCode(key="abcd", HASH_SIZE=1000))
