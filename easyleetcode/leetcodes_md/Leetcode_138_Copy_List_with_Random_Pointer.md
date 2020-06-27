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


根据 next 指针新建链表
维护新旧节点的映射关系
拷贝旧链表中的 random 指针
更新新链表中的 random 指针

---

![](https://raw.githubusercontent.com/billryan/algorithm-exercise/master/shared-files/images/copy_list_with_random_pointer.jpg)