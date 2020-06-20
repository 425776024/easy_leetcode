# L 003 Longest Substring Without Repeating Characters

https://leetcode.com/articles/longest-substring-without-repeating-characters/

--- 
 
``` 
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 ```

如果 s[j] 在 [i,j) 范围内有与j′重复的字符，我们不需要逐渐增加 i 。 我们可以直接跳过[i，j′] 范围内的所有元素，并将 i 变为j′+1。