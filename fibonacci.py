def generate_fibonacci(n):
    """
    Generates a Fibonacci sequence of length n.
    """
    fib_sequence = [0, 1]  # Initialize the sequence with the first two numbers
    
    # Start the loop from index 2 because the first two numbers are already set
    for i in range(2, n):
        # Compute the next Fibonacci number by summing the last two numbers in the sequence
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    
    return fib_sequence  # Return the generated Fibonacci sequence

# Generate the first 20 Fibonacci numbers
fibonacci_numbers = generate_fibonacci(20)

# Print the generated Fibonacci sequence
print(fibonacci_numbers)
