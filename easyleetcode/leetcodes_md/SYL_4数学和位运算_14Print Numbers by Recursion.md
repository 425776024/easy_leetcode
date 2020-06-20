# SYL_4数学和位运算_14Print Numbers by Recursion

---

```
'''
Print numbers from 1 to the largest number with N digits by recursion.

Example
Given N = 1, return [1,2,3,4,5,6,7,8,9].

Given N = 2, return [1,2,3,4,5,6,7,8,9,10,11,12,...,99].

Note
It's pretty easy to do recursion like:

recursion(i) 
    if i > largest number:
        return
    results.add(i)
    recursion(i + 1)

however this cost a lot of recursion memory as the recursion depth maybe very large.
Can you do it in another way to recursive with at most N depth?

Challenge
Do it in recursion, not for-loop.
'''

# 从小至大打印 N 位的数列
```
---