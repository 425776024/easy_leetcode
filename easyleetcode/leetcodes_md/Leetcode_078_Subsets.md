# L 078 Subsets
 
[https://www.bilibili.com/video/BV1Yp4y1Q7dJ](https://www.bilibili.com/video/BV1Yp4y1Q7dJ)


```
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


[]
[]  -> [1]
[][1]  -> [2][1,2]
[][1][2][1,2]  -> [3][1,3][2,3][1,2,3]
将上述过程转化为代码即为对数组遍历，每一轮都保存之前的结果并将其依次加入到最终返回结果中
```