a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a == 0:
    if b > 0:
        print("Bất phương trình đúng với mọi x (x ∈ ℝ).")
    elif b == 0:
        print("Bất phương trình không có nghiệm (vô lý).")
    else:
        print("Bất phương trình vô nghiệm.")
else:
    nghiem_phan_chia = -b / a
    if a > 0:
        print(f"Bất phương trình có nghiệm khi x > {nghiem_phan_chia}.")
        print(f"Khoảng nghiệm: (x ∈ ({nghiem_phan_chia}, ∞)).")
    else:
        print(f"Bất phương trình có nghiệm khi x < {nghiem_phan_chia}.")
        print(f"Khoảng nghiệm: (x ∈ (-∞, {nghiem_phan_chia})).")