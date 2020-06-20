# L 142 Linked List Cycle II
 
--- 
 
``` 

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Example
Given -21->10->4->5, tail connects to node index 1，return node 10

Challenge
Follow up:
Can you solve it without using extra space?

给定一个链表，如果链表中存在环，则返回到链表中环的起始节点，如果没有环，返回null。
先由快慢指针检测链表上是否存在环
如果环存在，根据相遇点到环入口点的距离 = 链表起始点到环入口点的距离，
我们可以同时从D点（链表起始点）和B点（相遇点）循环两个指针
两个会最终指向A点，即，环的起始点

 ```

head 到环的起点+环的起点到他们相遇的点的距离 与 环一圈的距离相等
head 运行到环起点 和 相遇点到环起点 的距离也是相等的。（相当于他们同时减掉了 环的起点到他们相遇的点的距离）
![](https://box.kancloud.cn/2015-10-24_562b1f4ae20b6.png)