# Leetcode_061_Rotate_List

[https://leetcode.com/problems/rotate-list/](https://leetcode.com/problems/rotate-list/)

---


```
Given a list, rotate the list to the right by k places, where k is non- negative.

Example
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```

---

- 思路1:先遍历整个链表获得链表长度n，然后此时把链表头和尾链接起来，在往后走n - k % n个节点就到达新链表的头结点前一个点，这时断开链表即可
- 思路2:快慢指针、后半段反到前面、合并list