
hsgioi = []

class SinhVien:
    def __init__(self,ten,tuoi,diem_tb):
        self.ten = ten
        self.tuoi = tuoi 
        self.diem_tb = diem_tb
    def print_info(self):
        print(f"Ten hoc sinh la: {self.ten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"diem trung binh: {self.diem_tb}")
    def xep_hoc_luc(self):
        if (self.diem_tb >= 8):
            hsgioi.append(self.ten)
        

def tim_sv_gioi(list_sv):
    print(f"danh sach hoc sinh gioi gom: {list_sv}")

sv1 = SinhVien("do dang minh",21,5)
sv2 = SinhVien("alibaba",22,9)
sv3 = SinhVien("cuop",35,8)

sv1.print_info()
sv2.print_info()
sv3.print_info()

sv1.xep_hoc_luc()
sv2.xep_hoc_luc()
sv3.xep_hoc_luc()

tim_sv_gioi(hsgioi)