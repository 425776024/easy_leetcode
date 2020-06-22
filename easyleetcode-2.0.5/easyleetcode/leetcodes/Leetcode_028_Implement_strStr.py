
class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    # 全部for里面的，一次break都没执行时，会调用最后的for else 的else
                    break
            else:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    # 在acdbcdbdse中，找到第一次出现dbd的地方
    a = s.strStr('acdbcdbdse', 'dbd')
    print(a)
