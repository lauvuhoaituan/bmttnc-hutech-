numbers = input("Nhap cac phan tu, cach nhau bang dau phay: ")

myTuple = tuple(numbers.split(","))

if len(myTuple) > 0:
    print("Phan tu dau tien:", myTuple[0])
    print("Phan tu cuoi cung:", myTuple[-1])
else:
    print("Tuple rong")