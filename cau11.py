import math

n = int(input("Nhập n: "))

S = 0
for i in range(1, n + 1):
    S += math.factorial(i)

print(f"Tổng S = {S}")