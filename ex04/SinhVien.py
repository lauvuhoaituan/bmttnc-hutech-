class SinhVien:
    next_id = 1

    def __init__(self, name, sex, major, diemTB):
        self._id = SinhVien.next_id
        SinhVien.next_id += 1

        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""

        self.xepLoaiHocLuc()

    def xepLoaiHocLuc(self):
        if self._diemTB >= 8:
            self._hocLuc = "Gioi"
        elif self._diemTB >= 6.5:
            self._hocLuc = "Kha"
        elif self._diemTB >= 5:
            self._hocLuc = "Trung binh"
        else:
            self._hocLuc = "Yeu"