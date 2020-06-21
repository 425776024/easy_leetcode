
class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """

    def fastPower(self, a, b, n):
        if n == 1:
            return a % b
        elif n == 0:
            return 1 % b
        elif n < 0:
            return -1

        # 拆分：(a * b) % p = ((a % p) * (b % p)) % p
        # 拆分：(a^n) % p = ((a^n/2) * (a^n/2)) % p
		
        product = self.fastPower(a, b, int(n / 2))
        product = (product * product) % b
        # 奇数次
        if n % 2 == 1:
            product = (product * a) % b

        return product


'''
没必要算2^32再不断取%！！
(a+b) % p =((a % p)+(b % p))% p
(a*b) % p =((a % p)*(b % p))% p

'''

s = Solution()
print(s.fastPower(2, 3, 31))
print(s.fastPower(100, 1000, 1000))
