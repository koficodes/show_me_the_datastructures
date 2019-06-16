Huffman Coding is a lossless compression algrothrim that uses the frequency of characters in a given information. This results in tree structure with the highest frequency at the root of the tree.

The choice of data structure for the problem is a binary Tree. Each of the tree has a frequency and a char instance variable in addition to the usual left and right nodes variable.
Heap is used to hold the nodes before the merging phase of the algorithm since the goal is to merge nodes with smaller frequency into nodes with higher fregquency.

The tree is traversed with recursion when generation the codes for the characters.
After the codes are generated they are stored/cached in a HashMap/Dictionary for efficient access for both encoding and decoding.
