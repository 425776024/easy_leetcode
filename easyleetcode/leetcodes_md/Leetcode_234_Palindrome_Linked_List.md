# Leetcode_234_Palindrome_Linked_List
[https://leetcode-cn.com/problems/palindrome-linked-list/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china](https://leetcode-cn.com/problems/palindrome-linked-list/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china)

```

Implement a function to check if a linked list is a palindrome.

Example
Given 1->2->1, return true

Challenge
Could you do it in O(n) time and O(1) space?

让我们判断一个链表是否为回文链表

```
- 题解1，不是 O(1) space:先按顺序把所有的结点值都存入到一个栈 stack 里，再按顺序从末尾取出结点值了，同时，头遍历一遍链表，看一致与否
- 题解2:头节点，慢指针到中点，快指针到尾部，将快慢指针中间部段，链表翻转