# Leetcode_131_Palindrome_Partitioning

```

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

典型的 DFS. 此题要求所有可能的回文子串，即需要找出所有可能的分割，使得分割后的子串都为回文
```