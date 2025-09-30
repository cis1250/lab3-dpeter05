#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

n = input("How many terms? ")

if n.isdigit() and int(n) > 0:
    n = int(n)
    a, b = 0, 1
    for i in range(n):
        if i == n - 1:
            print(a)
        else:
            print(a, end=" ")
        a, b = b, a + b
else:
    print("Please enter a positive integer.")
