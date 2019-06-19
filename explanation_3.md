Huffman Coding is a lossless compression algrothrim that uses the frequency of characters in a given information. This results in tree structure with the highest frequency at the root of the tree.

The choice of data structure for the problem is a binary Tree. Each of the tree has a frequency and a char instance variable in addition to the usual left and right nodes variable.
Heap is used to hold the nodes before the merging phase of the algorithm since the goal is to merge nodes with smaller frequency into nodes with higher fregquency.

The tree is traversed with recursion when generation the codes for the characters.
After the codes are generated they are stored/cached in a HashMap/Dictionary for efficient access for both encoding and decoding.

The run time of most intance methods involves one looping but creat_heap and merge_node involves extra heappush or heappop operation which adds extra O(log n) to the runtime of such methods.
The method with the worse run time is merge_node. This method
does two heappop operations O(2*log n) plus one heappush O(log n) and one while loop of Order O(n) in total we have O(2*log h + log h + h) making O(3logn+n). where h is the size of the heap

The space complexity of this algorithm includes the size of the HuffmanTree which is the sum of size the heap(h),codes hashmap(c) and reverse code hashmap (r) ie O(size(h) + size(c) +size(r))