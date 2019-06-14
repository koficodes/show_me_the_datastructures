import time


class CacheItem:

    def __init__(self, key, value):
        self.last_used = time.time()
        self.value = value
        self.key = key

    def __str__(self):
        return f"key:{self.key}, value: {self.value} ,last_used:{self.last_used}"


class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
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
            self.bucket[key].last_used = time.time()
            return self.bucket[key].value

        return -1

    def set(self, key=None, value=None):

        if not key and not value:
            return

        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.

        cache_item = CacheItem(key, value)
        if self.capacity == len(self.bucket):
            least_used = min(self.bucket.items(), key=lambda x: x.last_used)
            del self.bucket[least_used.key]

        self.bucket[key] = cache_item


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
our_cache.get()        # return -1
print(our_cache.get())
