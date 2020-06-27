# L 103 Binary Tree Zigzag Level Order Traversal
 
--- 
 
``` 
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7


return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

二叉树的之字形层序遍历
二叉树的之字形层序遍历是之前那道 Binary Tree Level Order Traversal 的变形，不同之处在于一行是从左到右遍历，
下一行是从右往左遍历，交叉往返的之字形的层序遍历。最简单直接的方法就是利用层序遍历，
并使用一个变量 cnt 来统计当前的层数（从0开始），将所有的奇数层的结点值进行翻转一下即可
 ```