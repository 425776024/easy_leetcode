# L 146 LRU Cache
 
[https://www.bilibili.com/video/BV1h5411s7Tt](https://www.bilibili.com/video/BV1h5411s7Tt)

```

Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently 
used item before inserting a new item.

最近最少使用页面置换缓存器:
缓存器主要有两个成员函数，get 和 put，其中 get 函数是通过输入 key 来获得 value，
如果成功获得后，这对 (key, value) 升至缓存器中最常用的位置（顶部），如果 key 不存在，则返回 -1。
而 put 函数是插入一对新的 (key, value)，如果原缓存器中有该 key，则需要先删除掉原有的，将新的插入
到缓存器的顶部。
如果不存在，则直接插入到顶部。若加入新的值后缓存器超过了容量，则需要删掉一个最不常用的值，
也就是底部的值。
```