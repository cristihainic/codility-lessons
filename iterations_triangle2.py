def triangle(n):
   nr_stars = 1
   indent = 0
   for i in range(n):
       print(f'{" " * indent}{"*" * (2 * n - nr_stars)}')
       nr_stars += 2
       indent += 1
