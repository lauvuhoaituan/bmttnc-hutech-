from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\n===== CHUONG TRINH QUAN LY SINH VIEN =====")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep theo diem trung binh")
    print("6. Sap xep theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")

    key = input("Nhap tuy chon: ")

    if key == "1":
        qlsv.nhapSinhVien()

    elif key == "2":
        ID = int(input("Nhap ID sinh vien: "))
        qlsv.updateSinhVien(ID)

    elif key == "3":
        ID = int(input("Nhap ID can xoa: "))

        if qlsv.deleteById(ID):
            print("Xoa thanh cong!")
        else:
            print("Khong tim thay sinh vien!")

    elif key == "4":
        name = input("Nhap ten can tim: ")
        result = qlsv.findByName(name)
        qlsv.showSinhVien(result)

    elif key == "5":
        qlsv.sortByDiemTB()
        qlsv.showSinhVien()

    elif key == "6":
        qlsv.sortByName()
        qlsv.showSinhVien()

    elif key == "7":
        qlsv.showSinhVien()

    elif key == "0":
        print("Ket thuc chuong trinh!")
        break

    else:
        print("Lua chon khong hop le!")