# Leetcode_233_Number_of_Digit_One

---

```

'''
Count the number of k's between 0 and n. k can be 0 - 9.

Example
if n=12, k=1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
we have FIVE 1's (1, 10, 11, 12)

找出从0至整数 n 中出现数位k的个数，与整数有关的题大家可能比较容易想到求模求余等方法，
但其实很多与整数有关的题使用字符串的解法更为便利。将整数 i 分解为字符串，然后遍历之，自增 k 出现的次数即可。
'''

```
---