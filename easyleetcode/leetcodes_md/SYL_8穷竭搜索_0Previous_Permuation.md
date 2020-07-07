# SYL_8穷竭搜索_0Previous_Permuation

```

Given a list of integers, which denote a permutation.

Find the previous permutation in ascending order.

Example
For [1,3,2,3], the previous permutation is [1,2,3,3]

For [1,2,3,4], the previous permutation is [4,3,2,1]

Note
The list may contains duplicate integers.

和前一题 Next Permutation 非常类似，这里找上一个排列，仍然使用字典序算法，大致步骤如下：

从后往前寻找索引满足 a[k] > a[k + 1], 如果此条件不满足，则说明已遍历到最后一个。
从后往前遍历，找到第一个比a[k]小的数a[l], 即a[k] > a[l].
交换a[k]与a[l].
反转k + 1 ~ n之间的元素。
（为何不从前往后呢？因为只有从后往前才能保证得到的是相邻的排列）

```