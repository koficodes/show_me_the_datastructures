Find user's group this problem has two scenrios it's either the user is found
in the current group or in a subgroups of the currenct group.
This problem can be solved recursively for checking if a user is in a group or subgroup.
The worse case is when  a has to be found in a deep nested subgroup, there for the
run  time of the program can be considered as O(n).