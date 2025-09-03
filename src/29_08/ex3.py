class TaiKhoan:
    def __init__(self,so_tai_khoan,chu_tai_khoan,so_du):
        self.so_tai_khoan = so_tai_khoan
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du
    def nap_tien(self,so_tien):
        self.so_du = self.so_du + so_tien
        print(f"ban da nap thanh cong {so_tien} vnd, so du moi cua ban la: {self.so_du}")
    def rut_tien(self,so_tien):
        if(self.so_du >= so_tien):
            self.so_du = self.so_du - so_tien
            print(f"ban da rut thanh cong {so_tien} vnd, so du moi cua ban la: {self.so_du}")
        else:
            print(f"so du khong du")
    def chuyen_khoan(self,stk_nguoi_nhan,ten_nguoi_nhan,so_tien):
        if (self.so_du >= so_tien):
            self.so_du = self.so_du - so_tien
            print(f"da gui thanh cong {so_tien} vnd toi tai khoan {stk_nguoi_nhan} - {ten_nguoi_nhan}")
        else: 
            print(f"so du khong du")

def thong_ke(list_tk,maximum):
    for tk in list_tk:
        if (tk.so_du >= maximum):
            maximum = tk.so_du
    return maximum


tk1 = TaiKhoan(1708200486,"do dang minh",200000000000000000)
tk2 = TaiKhoan(9999999999,"alibaba",999999999999200000000000000000)
tk3 = TaiKhoan(000000000000,"cuop",10000)

list_tk = [tk1, tk2, tk3]

print(f"so du lon nhat la: {thong_ke(list_tk,0)}")
