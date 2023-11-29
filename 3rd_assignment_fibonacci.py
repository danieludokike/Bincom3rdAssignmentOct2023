def generate_fibonacci_recursive(n, fib_series=[0, 1]):
    if len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
        generate_fibonacci_recursive(n, fib_series)
    return fib_series


# Example: Generate the first 10 Fibonacci numbers
result = generate_fibonacci_recursive(10)
print(result)
