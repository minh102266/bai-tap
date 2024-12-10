import math

a = float(input("Nhập a (a ≠ 0): "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    print("a phải khác 0, đây không phải là phương trình bậc hai.")
else:
    # Tính delta
    delta = b**2 - 4*a*c
    print(f"Delta (Δ) = {delta}")
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        print("Phương trình vô nghiệm.")
