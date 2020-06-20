# SYL_5链表_3Remove Duplicates from Unsorted List

---

```

'''
Write a removeDuplicates() function which takes a list and deletes
any duplicate nodes from the list. The list is not sorted.

For example if the linked list is 12->11->12->21->41->43->21,
then removeDuplicates() should convert the list to 12->11->21->41->43.

If temporary buffer is not allowed, how to solve it?
'''


最容易想到的简单办法就是两重循环删除重复节点了，当前遍历节点作为第一重循环，当前节点的下一节点作为第二重循环。


```
---