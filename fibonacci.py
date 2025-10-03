#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.


while True:
  try:
    user_input = input("Please enter a value:\n")
    user_input_int = int(user_input) 
    if (user_input_int > 0):
        print("Calculating Fibonacci Sequence")
        a, b = 0, 1
        print(a)  # Print the first term (0)
        print(b)  # Print the second term (1)
    
        for _ in range(2, user_input_int):  # Start from the 3rd term
            next_term = a + b
            print(next_term)
            a = b
            b = next_term
        break
    else:
        print("Invalid number, try agian")

  except ValueError:
        print("Invalid input.")
