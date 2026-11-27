X = int(input("Nhap X: "))
Y = int(input("Nhap Y: "))

arr = []

for i in range(X):
    row = []
    for j in range(Y):
        row.append(i * j)
    arr.append(row)

print(arr)