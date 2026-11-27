from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        return SinhVien.next_id

    def nhapSinhVien(self):
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap chuyen nganh: ")

        diemTB = float(input("Nhap diem trung binh: "))

        sv = SinhVien(name, sex, major, diemTB)
        self.listSinhVien.append(sv)

        print("Them sinh vien thanh cong!")

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)

        if sv is not None:
            sv._name = input("Nhap ten moi: ")
            sv._sex = input("Nhap gioi tinh moi: ")
            sv._major = input("Nhap chuyen nganh moi: ")
            sv._diemTB = float(input("Nhap diem moi: "))

            sv.xepLoaiHocLuc()
            print("Cap nhat thanh cong!")
        else:
            print("Khong tim thay sinh vien!")

    def deleteById(self, ID):
        sv = self.findByID(ID)

        if sv is not None:
            self.listSinhVien.remove(sv)
            return True

        return False

    def findByName(self, keyword):
        result = []

        for sv in self.listSinhVien:
            if keyword.lower() in sv._name.lower():
                result.append(sv)

        return result

    def sortByDiemTB(self):
        self.listSinhVien.sort(
            key=lambda sv: sv._diemTB
        )

    def sortByName(self):
        self.listSinhVien.sort(
            key=lambda sv: sv._major.lower()
        )

    def showSinhVien(self, listSV=None):
        if listSV is None:
            listSV = self.listSinhVien

        if len(listSV) == 0:
            print("Danh sach sinh vien trong!")
            return

        print("-" * 85)
        print("{:<5} {:<20} {:<12} {:<15} {:<10} {:<15}".format(
            "ID", "Ten", "Gioi tinh",
            "Chuyen nganh", "Diem TB", "Hoc luc"
        ))

        print("-" * 85)

        for sv in listSV:
            print("{:<5} {:<20} {:<12} {:<15} {:<10} {:<15}".format(
                sv._id,
                sv._name,
                sv._sex,
                sv._major,
                sv._diemTB,
                sv._hocLuc
            ))

        print("-" * 85)