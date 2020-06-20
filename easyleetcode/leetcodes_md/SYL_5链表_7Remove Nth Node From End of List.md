# SYL_5链表_7Remove Nth Node From End of List

---

```
'''
Given a linked list, remove the nth node from the end of list and return its head.

Note
The minimum number of nodes in list is n.

Example
Given linked list: 1->2->3->4->5->null, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5->null.

Challenge
O(n) time
'''

'''
移除链表倒数第N个节点，限定n一定是有效的，即n不会大于链表中的元素总数
使用快慢指针解决此题，需要注意最后删除的是否为头节点。
让快指针先走n步，直至快指针走到终点，找到需要删除节点之前的一个节点，改变node->next域即可
'''

```
---