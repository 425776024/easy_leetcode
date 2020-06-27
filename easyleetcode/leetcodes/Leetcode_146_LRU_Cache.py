

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # key:value
        self.cache = {}
        # 维护key顺序
        self.queue = []

    # def updateQueue(self, key):
    #     # 如果原缓存器中有该 key，则需要先删除掉原有的，将新的插入到缓存器的顶部。
    #     self.queue.remove(key)
    #     self.queue.insert(0, key)

    def get(self, key):
        if key in self.cache:
            # 如果原缓存器中有该 key，则需要先删除掉原有的，将新的插入到缓存器的顶部。
            self.queue.remove(key)
            self.queue.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if not key or not value:
            return None
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.queue) == self.capacity:
            # 若加入新的值后缓存器超过了容量，则需要删掉一个最不常用的值，也就是底部的值。
            del self.cache[self.queue.pop(-1)]

        self.cache[key] = value
        self.queue.insert(0, key)
