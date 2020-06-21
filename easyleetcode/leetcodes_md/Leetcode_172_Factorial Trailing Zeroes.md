# Leetcode 172 Factorial Trailing Zeroes

---

```
'''
Write an algorithm which computes the number of trailing zeros in n factorial.

Example
11! = 39916800, so the out should be 2

Challenge
O(log N) time
'''

'''
找阶乘数中末尾的连零数量
容易想到的是找相乘能为10的整数倍的数，也就是要找乘数中 10 的个数，而 10 可分解为2和5，
2×5,1×10,
2的数量远大于5的数量（比如1到 10 中有2个5，5个2），那么此题即便为找出5的个数(随便拿些2出来和5凑，总能组成10)

原题的问题即转化为求阶乘数中质因数5的个数，首先可以试着分析下100以内的数，再试试100以上的数，
'''


```



---