lines = []

while True:
    s = input("Nhap chuoi (Enter de ket thuc): ")

    if s == "":
        break

    lines.append(s.upper())

for line in lines:
    print(line)