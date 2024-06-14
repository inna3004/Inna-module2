def fibonacci_iterative(n):
   a, b = 0, 1
   for _ in range(n):
       a, b = b, a + b

   return a

result = fibonacci_iterative(10)
print(f"10-е число Фибоначчи: {result}")
