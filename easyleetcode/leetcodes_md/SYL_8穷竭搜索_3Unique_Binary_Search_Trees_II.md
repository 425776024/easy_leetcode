# SYL_8穷竭搜索_3Unique_Binary_Search_Trees_II

```

Given n, generate all structurally unique BST's
(binary search trees) that store values 1...n.

Example
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


利用『二叉搜索树』的定义，如果以 i 为根节点，那么其左子树由[1, i - 1]构成，右子树由[i + 1, n] 构成

要构建包含1到n的二叉搜索树，只需遍历1到n中的数作为根节点，以i为界将数列分为左右两部分，
小于i的数作为左子树，大于i的数作为右子树，使用两重循环将左右子树所有可能的组合链接到以i为根节点的节点上。

```