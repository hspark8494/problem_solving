n = int(input())
odd = n - n // 2
even = n // 2

for _ in range(n):
        print("* " * odd)
        print(" *" * even)