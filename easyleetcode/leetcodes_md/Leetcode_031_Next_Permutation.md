# L 031 Next Permutation
 
[https://www.bilibili.com/video/BV1vK411W71S](https://www.bilibili.com/video/BV1vK411W71S)

```
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]

Note
The list may contains duplicate integers.

找下一个升序排列
'''

'''
字典序算法：

从后往前寻找索引满足 a[k] < a[k + 1], 如果此条件不满足，则说明已遍历到最后一个。
从后往前遍历，找到第一个比a[k]大的数a[l], 即a[k] < a[l].
交换a[k]与a[l].
反转k + 1 ~ n之间的元素。
由于这道题中规定对于[4,3,2,1], 输出为[1,2,3,4], 故在第一步稍加处理即可。

```