# SYL_5链表_8Delete_Node_in_the_Middle_of_Singly_Linked_List

```

Implement an algorithm to delete a nodein the middle of a singly linked list,
given only access to that node.

Example
Given 1->2->3->4, and node 3. return 1->2->4

ps:无法知道欲删除节点的前一个节点
找不到前一个节点，那么也就意味着不能用通常的方法删除给定节点。
这种另类『删除』方法就是——使用下一个节点的值覆盖当前节点的值，删除下一个节点。

```