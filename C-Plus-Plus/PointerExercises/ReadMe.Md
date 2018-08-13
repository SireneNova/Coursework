
# Pointer Exercises
I needed to code in C++ for a work project, and the concept of pointers was new to me, so I sought out to gain a better understanding partly by doing challenge questions. These are some of the challenge questions and my solutions. I placed them in this "Coursework" section rather than the "Portfolio" section because the posted solutions helped get through a few parts.
___
## Objective
Complete pointer exercises from http://www.worldbestlearningcenter.com/index_files/cpp-pointer-max-exercise.htm to gain a better understanding of pointers.

1. Find the max value of a number of data values set by the user.
2. Write a C# program to accept 5 integer values from the console and print them on the screen.
3. Write a function to sort an array of ten integer values in ascending order. 

## Steps Taken
### Max Value
Made a function that loops through an array to find the max value.
Allowed the user to create the array with inputs for number of values and array values.
The array was of type int* in order to pass it to the max value function by reference.

### Display Input
Made an array with 5 slots.
Made a pointer int* p to the array.
Allowed the user to poplulate the array by pointing to each slot in the array ( * (p+1) etc. ).

### Sort
Wrote code that displays the values of an array of numbers to the console in ascending and descending order. The array is one that has been passed as a pointer through a sort function that arranges numbers from smallest to largest. Attempted to just use a built-in C++ sort function from a library, but it didn't work. Used the sort function from the solutions for the sake of time. It appears to be a selection sort.

## Results
### Max Value
Was able to get through this one without the solutions. Grasped how pointers are used to pass values by reference.

### Display Input
Grasped how to use pointers to access specific values in an array.

### Sort
Observed a sort function that dereferenced a pointer multiple times. This made it look complex on the outside, but was able to get a better understanding of it.
