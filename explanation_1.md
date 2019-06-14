Least Recently Used Cache.
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.
From the above explanation we need a way to keep track of the times the entries are used, so 
I decided to use a CatchItem class to keep track of the times.

The main container of the catch items is a dictionary/Hashmap. It is a suitable datastructure
for this problems and it also keeps the operations at least at the order of O(1).

All get operations is always O(1). 
The set operations is mostly 0(1) but when the capicity of the catch bucket is full the least used
catch item has to be removed. This involves using the 'min' function which has an order of O(n) and also del function with an order of O(1) for average case or 0(n) for Amortized Worst Case. since we considering a dict of at most five items we will consider the average case.

In conclusion, averagely all operation are Order of O(1).