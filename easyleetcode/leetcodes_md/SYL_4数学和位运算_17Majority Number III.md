# SYL_4数学和位运算_17Majority Number III

---

```
'''
Given an array of integers and a number k,
the majority number is the number that occurs more than 1/k of the size of the array.

Find it.

Example
Given [3,1,2,3,2,3,3,4,4,4] and k=3, return 3.

Note
There is only one majority number in the array.

Challenge
O(n) time and O(k) extra space
'''

'''
对 K-1个数进行相互抵消，这里不太可能使用 key1, key2...等变量，用数组使用上不太方便，
且增删效率不高，故使用哈希表较为合适，当哈希表的键值数等于 K 时即进行清理
'''
```
----
