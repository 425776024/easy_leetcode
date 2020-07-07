# L 039 Combination Sum
 
--- 
 
``` 

Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]


Note
- All numbers (including target) will be positive integers.
- Elements in a combination (a1, a2, … , ak) must be in non-descending order.
(ie, a1 ≤ a2 ≤ … ≤ ak).
- The solution set must not contain duplicate combinations.

给定一个候选数字的集合 candidates 和一个目标值 target. 找到 candidates 中所有的和为 target 的组合.
在同一个组合中, candidates 中的某个数字不限次数地出现

和 Permutations 十分类似，区别在于剪枝函数不同。这里允许一个元素被多次使用，故递归时传入的索引值不自增，而是由 for 循环改变

 ```
![](https://pic.leetcode-cn.com/ade93b4f0678b2b1385ad1362ff426ce0a5a800a5b0ae07dfb65f58677374559-39-3.png)