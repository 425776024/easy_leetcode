# Leetcode_023_Merge_k_Sorted_Lists

[https://www.bilibili.com/video/BV1Ct4y117Ua](https://www.bilibili.com/video/BV1Ct4y117Ua)

```
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

```

- 1.迭代调用Merge Two Sorted Lists，两两合并
> 先合并链表1和2，接着将合并后的新链表再与链表3合并，如此反复直至 vector 内所有链表均已完全

- 2.使用二分法对其进行归并，从中间索引处进行二分归并

```