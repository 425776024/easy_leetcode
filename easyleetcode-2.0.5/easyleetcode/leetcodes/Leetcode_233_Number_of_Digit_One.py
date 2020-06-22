

class Solution:
    def digitCounts(self, k: int, n: int):
        count = 0
        kChar = str(k)
        for i in range(n+1):
            iChars = str(i)
            for iChar in iChars:
                if kChar == iChar:
                    count += 1
                    print(iChars,end=',')
        print()
        return count


s = Solution()

print(s.digitCounts(k=1, n=12))
