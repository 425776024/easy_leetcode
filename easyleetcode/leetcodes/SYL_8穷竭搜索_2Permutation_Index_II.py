

class Solution:
    def permutationIndexII(self, A):
        if A is None or len(A) == 0:
            return 0

        index = 1
        factor = 1
        for i in range(len(A) - 1, -1, -1):
            hash_map = {A[i]: 1}
            rank = 0
            for j in range(i + 1, len(A)):
                if A[j] in hash_map.keys():
                    hash_map[A[j]] += 1
                else:
                    hash_map[A[j]] = 1
                # get rank
                if A[i] > A[j]:
                    rank += 1

            index += rank * factor / self.dupPerm(hash_map)
            factor *= (len(A) - i)

        return int(index)

    def dupPerm(self, hash_map):
        # 记录i，以及i后面出现的每个元素的次数
        # 不重复的是1，   1！=1
        if hash_map is None or len(hash_map) == 0:
            return 0
        dup = 1
        for val in hash_map.values():
            dup *= self.factorial(val)

        return dup

    def factorial(self, n):
        # n!
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r


s = Solution()
print(s.permutationIndexII([1, 6, 5, 3, 1]))
