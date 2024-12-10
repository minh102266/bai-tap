# Nhập các hệ số
a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))

D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1

if D == 0:
    if Dx == 0 and Dy == 0:
        print("Hệ phương trình có vô số nghiệm (các phương trình trùng nhau).")
    else:
        print("Hệ phương trình vô nghiệm (các phương trình song song).")
else:
    x = Dx / D
    y = Dy / D
    print(f"Hệ phương trình có nghiệm duy nhất:")
    print(f"x = {x}")
    print(f"y = {y}")