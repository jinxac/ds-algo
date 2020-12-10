from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1
        self.move_to_end(key)
        print("get", self)
        return self[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self: 
            self.move_to_end(key)
        self[key] = value
        print("put", self)
        if len(self) > self.capacity:
            self.popitem(last=False)
            print("evict", self)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
