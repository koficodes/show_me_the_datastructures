Finding unions and intersections are set operations so the best data structure is having your data in sets.
In order to do this the values of the linkedlist are traversed and stored in a  set for the operations to be performed on.
After, the linkedlist in reconstructed. This is ideal because the order of the nodes are not required.
The union method has set operation with an order 	
O(len(s)+len(t)) plus a loop to reconstruct the resulting linkedlist O(r) where 'r' is the size of result.

The intersection also involves a set operration with average order of O(len(s) * len(t)) plus the reconstruction loop ie. O(r)

The space required to store the result of the union operation is equal to the size of the sum of the unique elements in each list O(len(s1) + len(s2)) and also there is a space required for generating the new linkedlist which is 0(xn) where x is the size of each integer and n is the size of the union_list. In total the space required is O(len(s1) + len(s2)+ xn), the largest term is xn, therefore the space complexity can be considered as O(xn).
The intersection operation also has similar workflow and will also has similar space complexity ie. O(xn)