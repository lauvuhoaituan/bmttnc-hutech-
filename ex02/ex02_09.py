def kiemTraNguyenTo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input("Nhap mot so: "))

if kiemTraNguyenTo(n):
    print(n, "la so nguyen to")
else:
    print(n, "khong phai so nguyen to")