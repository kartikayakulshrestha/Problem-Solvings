from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
       self.capacity=capacity
       self.stack=OrderedDict()
       return 


    def get(self, key: int) -> int:
        if key in self.stack:
            z=self.stack.pop(key)
            self.stack[key]=z
            return z
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.stack:
            self.stack.pop(key)
            self.stack[key]=value
            return 
        if len(self.stack)<self.capacity:
            self.stack[key]=value
        else:
            self.stack.popitem(last=False)
            
            self.stack[key]=value
        return 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)