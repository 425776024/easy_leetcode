# Leetcode_138_Copy_List_with_Random_Pointer

bilibili:
[https://www.bilibili.com/video/BV1nk4y1r7N9?from=search&seid=9406074840994037345](https://www.bilibili.com/video/BV1nk4y1r7N9?from=search&seid=9406074840994037345)

---

A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
要求：深度拷贝一个带有 random 指针的链表，random 可能指向空，也可能指向链表中的任意一个节点。

对于通常的单向链表，我们依次遍历并根据原链表的值生成新节点即可，原链表的所有内容便被复制了一份。
但由于此题中的链表不只是有 next 指针，还有一个随机指针，故除了复制通常的 next 
指针外还需维护新链表中的随机指针。
容易混淆的地方在于原链表中的随机指针指向的是原链表中的节点，深拷贝则要求将随机指针指向新链表中的节点。



这道链表的深度拷贝题的难点就在于如何处理随机指针的问题，由于每一个节点都有一个随机指针，
这个指针可以为空，也可以指向链表的任意一个节点，
如果在每生成一个新节点给其随机指针赋值时，都要去遍历原链表的话，OJ 上肯定会超时，
所以可以考虑用 HashMap 来缩短查找时间，第一遍遍历生成所有新节点时同时建立一个原节点和新节点的 
HashMap，
第二遍给随机指针赋值时，查找时间是常数级。

---