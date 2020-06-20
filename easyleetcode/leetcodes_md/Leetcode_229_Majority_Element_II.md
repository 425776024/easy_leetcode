# L 229 Majority Element II
 
--- 
 
``` 
'''
Given an array of integers,
the majority number is the number that occurs more than 1/3 of the size of the array.

Find it.

Example
Given [1, 2, 1, 2, 1, 3, 3], return 1.

Note
There is only one majority number in the array.

Challenge
O(n) time and O(1) extra space.
'''

'''
经过举了很多例子分析得出，任意一个数组出现次数大于 n/3 的数最多有：3个
那么有了这个信息，使用投票法的核心是找出两个候选数进行投票，需要两遍遍历，
第一遍历找出两个候选数，
第二遍遍历重新投票验证这两个候选数是否为符合题意
'''


 ```