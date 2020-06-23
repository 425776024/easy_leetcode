# Leetcode_169_Majority Element

[https://www.bilibili.com/video/BV1bz4y1d7B5](https://www.bilibili.com/video/BV1bz4y1d7B5)

---

```
'''
Given an array of integers, the majority number is
the number that occurs more than half of the size of the array. Find it.

Example
Given [1, 1, 1, 1, 2, 2, 2], return 1

Challenge
O：n：time and O：1：extra space
'''

'''
找出现次数超过一半的数，使用哈希表统计不同数字出现的次数，超过二分之一即返回当前数字。
这种方法非常简单且容易实现，但会占据过多空间
既然某个数超过二分之一，那么用这个数和其他数进行 PK，不同的计数器都减一**（核心在于两两抵消）**，
相同的则加1，最后返回计数器大于0的即可
'''
```

---