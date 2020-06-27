# Leetcode_145_Binary_Tree_Postorder_Traversal

```
Problem Statement
Given a binary tree, return the postorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
copy
return [3,2,1].

Challenge
Can you do it without recursion?


```

- 1.递归
- 2.直接迭代
- 3.反转先序遍历，『左右根』的后序遍历结果，我们发现只需将『根右左』的结果转置即可：先序遍历通常为『根左右』，故改变『左右』的顺序即可，所以如此一来后序遍历的非递归实现起来就非常简单了。