class SinhVien():
    def __init__(self, mahocsinh, hovaten, diem):
        self.mahocsinh = mahocsinh
        self.hovaten = hovaten
        self.diem = diem
        self.diemtrungbinh = 0
        self.xeploai = ""

    def tinhdiemtrungbinh(self):
        tong = dem =0
        for i in self.diem:
            tong = tong + i
            dem +=1
        self.diemtrungbinh = tong / dem

    def xephang(self):
        if self.diemtrungbinh >= 9:
            self.xeploai = "Xuat sac"
        elif self.diemtrungbinh >= 8:
            self.xeploai = "Gioi"
        elif self.diemtrungbinh >= 7:
            self.xeploai = "Kha"
        elif self.diemtrungbinh >= 5:
            self.xeploai = "TB"
        else:
            self.xeploai = "Yeu"

    def __str__(self):
        return self.mahocsinh + ' ' + self.hovaten + ' ' + "%.1f" % self.diemtrungbinh +' '+self.xeploai

lis = []
n = int(input("Nhập số lượng học sinh: "))
for i in range(n):
    name = input("Nhập tên học sinh: ")
    a = [float(x) for x in input("Nhập điểm: ").split()]
    id = i + 1
    sv = SinhVien("HS%02d" % id, name, a)
    sv.tinhdiemtrungbinh()
    sv.xephang()
    lis.append(sv)

list_new = sorted(lis,key=lambda x:x.diemtrungbinh,reverse=True)

print("___________XUAT DANH SACH_____________")
for sv in list_new:
    print(sv)

