# Leetcode 086 Partition List
 
--- 
 
``` 

'''
Given a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes
in each of the two partitions.

For example,
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null.
'''

'''
要求将小于x的节点放到前面，而并不要求对元素进行排序。这种分割的题使用两路指针即可轻松解决。
左边指针指向<x的节点，右边指针指向>=x的节点。
由于左右头节点不确定，我们可以使用两个dummy节点。
'''


 ```