# L 027 Remove Element
 
--- 
 
``` 

Given an array and a value, remove all occurrences of that value in place and
 return the new length.

The order of elements can be changed, and the elements after the new length 
don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]



一句话总结：拿两个指示变量i,j从0开始，i只负责遍历所有的值，j负责保存不包含elem的索引，
i循环完了j的长度就是新的数组长度，新的数组内容就是0:j

 ```