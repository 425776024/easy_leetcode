# L 079 Word Search
 
--- 
 
``` 
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell,
 where "adjacent" cells are those horizontally or vertically neighboring.
  The same letter cell may not be used more than once.

Example
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
copy
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


原二维数组就像是一个迷宫，可以上下左右四个方向行走，我们以二维数组中每一个数都作为起点和给定字符串做匹配
需要一个和原数组等大小的 visited 数组，是 bool 型的，用来记录当前位置是否已经被访问过，因为题目要求一个 cell 只能被访问一次

 ```