# Leetcode_260_Single Number III

[https://www.bilibili.com/video/BV1Xp4y1Q7Wb](https://www.bilibili.com/video/BV1Xp4y1Q7Wb)

---

```


Given 2*n + 2 numbers, every numbers occurs twice except two, find them.

Example
Given [1,2,2,3,4,4,5,3] return 1 and 5

Challenge
O(n) time, O(1) extra space.

利用了x1 ^ x2不为0的特性
如果x1 ^ x2不为0，那么x1 ^ x2的结果必然存在某一二进制位不为0（即为1）

由于除了x1和x2之外其他数都是成对出现，故与最低位的1异或时一定会抵消，
因此找到的第一个最低位的1，就是x1 x2中的某一个的
最低位的1提取出来:在这一二进制位上x1和x2必然相异（1111,1110总得不一样，不然x^y=0）



```

---