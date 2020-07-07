# SYL_8穷竭搜索_2Permutation_Index_II

```

Given a permutation which may contain repeated numbers, find its index in all the
permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

Input :[1,4,2,2]
Output:3

Example 2:
Input :[1,6,5,3,1]
Output:24

不同的是，可重复，题 Permutation Index 的扩展，这里需要考虑重复元素，
有无重复元素最大的区别在于原来的1!, 2!, 3!...等需要除以重复元素个数的阶乘（重复元素的出现次数）
i重复了a次，j重复了b次，k重复了c次那么总共的不重复序列数= n!/(a!b!c!)
如[1,1,1,2,2,3]，排列数为：6!÷(3!×2!×1!)。

记录重复元素个数同样需要动态更新，引入哈希表这个万能的工具较为方便

```