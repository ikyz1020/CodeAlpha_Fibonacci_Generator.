def fibonacci_generator():
    """Generates an infinite Fibonacci sequence."""
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

n = int(input("How many Fibonacci numbers do you want to generate? "))

fib = fibonacci_generator()

print("The first", n, "Fibonacci numbers are:")
for _ in range(n):
    print(next(fib), end=" ")