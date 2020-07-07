
class Solution:
    def combinationSum(self, candidates, target):
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝是为了提速，在本题非必需
        candidates.sort()
        # 在遍历的过程中记录路径，它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, path, res, target)
        return res

    def __dfs(self, candidates, begin, path, res, target):
        if target == 0:
            res.append(path[:])
            return

        for index in range(begin, len(candidates)):
            # 减去candidates[index]，求，和为residue的集合
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            # 记住减去的路径，如果最后target==0，则拷贝此路径作为一个结果
            path.append(candidates[index])
            # 因为不限次数的使用，[2, 3, 6, 7] 7，可以是 2+2+4，所以还能本index开始
            self.__dfs(candidates, index, path, res, residue)
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)
