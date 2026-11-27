student = {
    "name": "Nguyen Van A",
    "age": 20,
    "major": "IT"
}

key = input("Nhap key muon xoa: ")

if key in student:
    del student[key]
    print("Da xoa key:", key)
else:
    print("Khong tim thay key")

print("Dictionary:", student)