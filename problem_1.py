import warnings
from collections import deque


class LRU_Cache:

    def __init__(self, capacity=5):
        # Initialize class variables
        if not capacity:
            warnings.warn("Cache size required, using 5 as default")
        self.capacity = capacity
        self.access_rank = deque(maxlen=capacity)
        self.bucket = {}

    def __str__(self):
        bucket_string = ""
        for key, item in self.bucket.items():
            bucket_string += f"\n{item}"
        return bucket_string

    def get(self, key=None):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if not key:
            return -1

        if key in self.bucket:
            self.access_rank.appendleft(key)
            return self.bucket[key]

        return -1

    def set(self, key=None, value=None):

        if not key and not value:
            return

        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.

        if self.capacity == len(self.bucket):
            least_used_key = self.access_rank.pop()
            del self.bucket[least_used_key]
        self.bucket[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set()
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
our_cache.get()        # return -1


our_cache = LRU_Cache(4)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)  # returns -1


our_cache = LRU_Cache()  # gives warning
