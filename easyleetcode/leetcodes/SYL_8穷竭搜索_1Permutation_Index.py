
class Solution:
    def permutationIndex(self, A):
        if A is None or len(A) == 0:
            return 0

        index = 1
        factor = 1
        # 从最后位开始，阶乘(factor)依次保留着
        for i in range(len(A) - 1, -1, -1):
            rank = 0
            for j in range(i + 1, len(A)):
                # 统计i号位后面，有几个小于i号位的
                if A[i] > A[j]:
                    rank += 1
            # 如，2个 3!
            index += rank * factor
            factor *= (len(A) - i)

        return index

    
print(Solution().permutationIndex([1,2,4]))
print(Solution().permutationIndex([1,4,2]))