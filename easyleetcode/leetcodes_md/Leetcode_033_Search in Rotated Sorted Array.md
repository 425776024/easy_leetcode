# Leetcode_033_Search in Rotated Sorted Array


[https://www.bilibili.com/video/BV1sZ4y1p79i](https://www.bilibili.com/video/BV1sZ4y1p79i)

---


```
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge
O(logN) time

```

---

对于旋转数组的分析可使用画图的方法，如下图所示，升序数组经旋转后可能为如下两种形式。
![](https://raw.githubusercontent.com/billryan/algorithm-exercise/master/shared-files/images/rotated_array.png)