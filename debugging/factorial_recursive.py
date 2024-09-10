#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the factorial is to be computed.
    
    Returns:
    int: The factorial of the integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if the script is being run directly (as opposed to being imported)
if __name__ == "__main__":
    # Get the integer input from command-line arguments
    f = factorial(int(sys.argv[1]))
    # Print the result to the console
    print(f)
