# SYL_4数学和位运算_4Check Power of 2


```
'''

Using O(1) time to check whether an integer n is a power of 2.

Example
For n=4, return true;

For n=5, return false;

Challenge
O(1) time

简单点来考虑可以连除2求余，看最后的余数是否为1，但是这种方法无法在
O(1)O(1)
O(1)
'''

'''
0100 ==> 4
0011 ==> 3

两个数进行按位与就为0了！如果不是2的整数幂则无上述关系

'''
```