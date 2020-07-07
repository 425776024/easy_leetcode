# SYL_8穷竭搜索_1Permutation_Index

```

Given a permutation which contains no repeated number, find its index in all the permutations of
these numbers, which are ordered in lexicographical order. The index begins at 1.

Example
Given [1,2,4], return 1.

给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号，
其中，编号从1开始。
例如，排列[1,2,4]是第1个排列。

对于某一个给定的位数A[i],需要判断在它后面有几个小于它的数，记下这个数字和A[i]所在的位置。
比如对于一个四位数，5316  ， 第一位后面有2小于它的数，如果这两个数排在第一位，那么（1和3）各有3！的排列组合数小于（5316）.
同理，对于第二位，其后有1个小于它的数，如果它放在第二位，那么有2！种排列。
因此判断一个给定数位于排列组合的第几位，则可以按照以下公式进行
count1*(A.length-1)!+count2*(A.length-2)!+......+countn*(0)!

```