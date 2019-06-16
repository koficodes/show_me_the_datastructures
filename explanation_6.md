Finding unions and intersections are set operations so the best data structure is having your data in sets.
In order to do this the values of the linkedlist are traversed and stored in a  set for the operations to be performed on.
After, the linkedlist in reconstructed. This is ideal because the order of the nodes are not required.
The union method has set operation with an order 	
O(len(s)+len(t)) plus a loop to reconstruct the resulting linkedlist O(r) where 'r' is the size of result.

The intersection also involves a set operration with average order of O(len(s) * len(t)) plus the reconstruction loop ie. O(r)