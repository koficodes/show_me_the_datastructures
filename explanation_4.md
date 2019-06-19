Finding user's group, This problem has two scenarios it's either the user is found
in the current group or in a subgroups of the currenct group.
This problem can be solved recursively for checking if a user is in a group or subgroup.
The worse case is when  a user has to be found in a deep nested subgroup, there for the
run  time of the program can be considered as O(R*n). Where R is the number of recursive call and n is the number of groups to search through which grows as more subgroups are discovered.

The space complexity is dependent on the size of groups and users held by a group instance which is 0(size(g) + size(u)) where g is list of groups and u is list of users. Also the call stack also contributes to the space compliexity of the program which can be considered as the size of individual stack times number of recursize calls ie. O(s*R). Where s is the stack size and R is the number of recursize calls. In total we get O(size(g) + size(u) + s * R)