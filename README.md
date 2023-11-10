# CodeAlpha
Task 1 Exploitation Binaire
Task 2 FIBONACCI GENERATOR 
# Explanation of the code: 
We can write a computer program for printing the Fibonacci sequence in 2 different ways:
Iteratively, and
Recursively.
Iteration means repeating the work until the specified condition is met. Recursion, on the other hand, means performing a single task and proceeding to the next for performing the remaining task. 

In the above code, first we have defined a function that will print the Fibonacci series. It accepts a parameter for the length, and the function needs to print the Fibonacci series.
Next, we have created 2 variables that contain the initial 2 Fibonacci values, that is 0 and 1.
Then we printed the first 2 values [0, 1] and decremented the length by 2, because 2 values were already been printed.
We will run a loop for the remaining length time, and each time print the next Fibonacci value by adding the previous 2 terms that are stored in the first and second variables (that we created initially to keep track of the previous 2 values).
Update the first and second values that will point to the previous 2 values [first = second, and second = previous first + second].
The loop will run until the length becomes 0, which states that the required length of the Fibonacci sequence is printed.
Then we call the function defined for printing Fibonacci from the main function by passing the argument of the required length to be printed. And there you have it!
