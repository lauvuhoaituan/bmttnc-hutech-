hours = float(input("Nhap so gio lam: "))
salary = float(input("Nhap luong moi gio: "))

if hours <= 44:
    total = hours * salary
else:
    total = 44 * salary + (hours - 44) * salary * 1.5

print("Luong thuc nhan:", total)