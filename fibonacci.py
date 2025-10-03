#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

user_input = input("Please enter a value:\n")
if (user_input > 0):
  print("Calculating Fibonacci Sequence")
else:
  print("Invaild, Try again")
