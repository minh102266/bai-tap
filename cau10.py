import math

x = float(input("Nhập x "))
n = int(input("Nhập n"))

S = x
for i in range(n):
    S = math.sqrt(x + S)

print(f"Giá trị của S là: {S}")