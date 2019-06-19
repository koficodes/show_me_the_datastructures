Finding files in a directory with subdirectories is a recursive operation
so I chose to solve the problem recuresively. The recursive case is when there is a subdirectory and the base case is when files our found without any subdirectories.
The part that really affects the efficiency of the program is the recursive looping section of the program which depends on the number subdirectories discovered.
The order can be considered to be O(R*n) where R is the number of recursive calls and n is the size of directories to  seach through.

The space complexity includes the size of the variable to hold the found files O(size(f)) and also the recursize call stack O(size(s)) ie. O(size(f) + size(s)) where f is the number of files found and s is the number of recursize call stack.