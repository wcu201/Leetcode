'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class LRUCache:
    cache = {}#OrderedDict()
    capacity = 0
    def __init__(self, capacity: int):
        self.cache = {}#OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            swp = self.cache[key]
            del self.cache[key]
            self.cache[key] = swp
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            del self.cache[next(iter(self.cache))]
            #self.cache.popitem(last=False)
            #del self.cache[list(self.cache.keys())[0]]
        if key in self.cache: del self.cache[key]
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
You want to have a data structure the allowes you access elements in O(1) and keep track of the order in which elements are inserted. 
In Python3 normal dictionaries are ordered and take less space than an OrderedDictionary.When you get a val at a key you move the key
val pair in the dict to the end by saving the val, deleting the key, then reinserting the key with the saved val. 
When putting a new key val pair we check capacity to see it's already at max. 
If it is we will delete the first value of the dictionary and then add our new value. 
If the key is already in the dicitonary we just update the val. 
Using next(iter(self.cache)) allows us to get the first key in a dictionary
'''
