x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

if x == 1:
    S = n + 1
else:
    S = (1 - x**(n + 1)) / (1 - x)

print(f"Tổng S = {S}")