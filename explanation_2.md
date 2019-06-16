Finding Files.
Finding files in a directory with subdirectories is a recursive operation
so I chose to solve the problem recuresively. The recursive case is when there is a subdirectory and the base case is when files our found without any subdirectories.
The part that really affects the efficiency of the program is the recursive looping 
section of the program which depends on the number subdirectories discovered.
The order can be considered to O(n)