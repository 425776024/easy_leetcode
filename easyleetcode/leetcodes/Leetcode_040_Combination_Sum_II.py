

class Solution(object):
    def combinationSum2(self, candidates, target):
        if target == 0 or len(candidates) == 0:
            return []
        res = []
        path = []

        candidates.sort()
        self.__dfs(candidates, 0, path, res, target)
        return res

    def __dfs(self, candidates, begin, path, res, target):
        # 从集合candidates中，起点begin开始，在path基础上，寻找和为target的集合，结果保存到res

        if target == 0:
            # 在path基础上，寻找和为0的集合，意味着找到一组正确解了
            res.append(path[:])
            return
        for index in range(begin, len(candidates)):
            if candidates[index] > target:
                break
            # 去重，index > begin要加，又重复的第2，3..个元素起始的时候，同样和前一个相等，但是不能continue
            if index > begin and candidates[index] == candidates[index - 1]:
                continue
            residue = target - candidates[index]
            if residue < 0:
                break
            path.append(candidates[index])
            # 第二个参数和Combination Sum的位置不一样，是i+1
            # 因为这里每个数最多只能使用一次，而之前是使用无限次，故递归时索引变量传i + 1
            self.__dfs(candidates, index + 1, path, res, residue)
            # 回溯
            path.pop()


s = Solution()
print(s.combinationSum2([10, 1, 6, 7, 2, 1, 5], target=8))
