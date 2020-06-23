# L 136 Single Number

[https://www.bilibili.com/video/BV1Hk4y1677X](https://www.bilibili.com/video/BV1Hk4y1677X)

--- 


```
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.

Example
Given [1,2,2,1,3,4,3], return 4

Challenge
One-pass, constant extra space

共有2*n + 1个数，且有且仅有一个数落单，要找出相应的「单数」

思路：根据x ^ x = 0和x ^ 0 = x可将给定数组的所有数依次异或，最后保留的即为结果。


```