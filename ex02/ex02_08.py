numbers = input("Nhap cac so nhi phan, cach nhau bang dau phay: ")

result = []

for n in numbers.split(","):
    n = n.strip()

    if int(n, 2) % 5 == 0:
        result.append(n)

print(",".join(result))