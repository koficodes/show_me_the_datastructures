import warnings
from collections import OrderedDict


class LRU_Cache(OrderedDict):

    def __init__(self, capacity=None):
        # Initialize class variables
        if not capacity:
            capacity = 5
            warnings.warn("Cache size required, using 5 as default")
        self.capacity = capacity

    def get(self, key=None):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if not key:
            return -1

        try:
            value = super().__getitem__(key)
            self.move_to_end(key)
            return value
        except KeyError:
            return -1

        return -1

    def set(self, key=None, value=None):

        if not key and not value:
            return

        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        super().__setitem__(key, value)
        if len(self) > self.capacity:
            oldest_item = next(iter(self))
            del self[oldest_item]


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set()
print(our_cache.get(1))     # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return -1
print(our_cache.get())        # return -1


our_cache = LRU_Cache(4)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1


our_cache = LRU_Cache()  # gives warning
print(our_cache.get(1))  # return -1
our_cache.set(2, 2)
print(our_cache.get(2))  # 2

# output
# 1
# 2
# -1
# -1
# 1
# 2
# -1
# -1
# -1
# 2
