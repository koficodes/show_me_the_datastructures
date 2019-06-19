Least Recently Used Cache.
An LRU cache is a type of cache from which we remove the least recently used entry when the cache memory reaches its limit.
From the above explanation we need a way to keep ranking order of the entries recently used, so I decided to use a queue to keep track of the ranks.

The main container of the catch items is a dictionary/Hashmap. It is a suitable datastructure
for this problems and it also keeps the operations at least at the order of O(1).

The pop and append operation of the queue are both 0(1)
All get operations is always O(1). 
The set operations is mostl 0(1).

In conclusion, all operation are Order of O(1).

The space complexity is determined by capacity of the catch bucket.
hence it will have the order 0(c) where c is the size of the capacity of the Cache bucket.