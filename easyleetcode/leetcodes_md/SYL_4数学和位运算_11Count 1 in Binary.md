# SYL_4数学和位运算_11Count 1 in Binary

---

```
'''
Count how many 1 in binary representation of a 32-bit integer.

Example
Given 32, return 1
Given 5, return 2
Given 1023, return 9

Challenge
If the integer is n bits with m 1 bits. Can you do it in O(m) time?
'''

# x & (x - 1) 的含义为去掉二进制数中1的最后一位，无论 x 是正数还是负数都成立。

'''

给定 32 (100000)，返回 1
给定 5 (101)，返回 2
给定 1023 (111111111)，返回 9 ? python 10
'''
```
---