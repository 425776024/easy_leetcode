# L 143 Reorder List
 
--- 
 
``` 
Given a singly linked list L: L0→L1→…→L__n-1→Ln,
reorder it to: L0→L__n_→L1→_L__n-1→L2→L__n-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.


这道链表重排序问题可以拆分为以下三个小问题：
1. 使用快慢指针来找到链表的中点，并将链表从中点处断开，形成两个独立的链表。
2. 将第二个链翻转。
3. 将第二个链表的元素间隔地插入第一个链表中。
 ```