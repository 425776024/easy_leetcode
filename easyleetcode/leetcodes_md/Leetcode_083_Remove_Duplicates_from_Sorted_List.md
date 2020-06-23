# L 083 Remove Duplicates from Sorted List

[https://www.bilibili.com/video/BV1eK411p7V5](https://www.bilibili.com/video/BV1eK411p7V5)

--- 
 
``` 
'''
Given a sorted linked list,
delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

'''
遇到当前节点和下一节点的值相同时，删除下一节点，并将当前节点next值指向下一个节点的next, 
当前节点首先保持不变，直到相邻节点的值不等时才移动到下一节点。
'''


 ```