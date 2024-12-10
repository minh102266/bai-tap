a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

# Kiểm tra điều kiện và tính nghiệm
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Nghiệm của phương trình là: {x}")
