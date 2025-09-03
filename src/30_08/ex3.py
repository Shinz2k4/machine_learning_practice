
class Object:
    def __init__(self,id,ho_ten,sdt,gioi_tinh):
        self.id = id
        self.ho_ten = ho_ten
        self.sdt = sdt
        self.gioi_tinh = gioi_tinh
    def cap_nhat(self,ho_ten_moi,sdt_moi,gioi_tinh_moi):
        self.ho_ten = ho_ten_moi
        self.sdt = sdt_moi
        self.gioi_tinh = gioi_tinh_moi
    def hien_thi(self):
        print(f'id: {self.id}')
        print(f'ten: {self.ho_ten}')
        print(f'so dien thoai: {self.sdt}')
        print(f'gioi tinh: {self.gioi_tinh}')
class DanhBa:
    def __init__(self,list_db):
        self.list_db = list_db
    def them_lien_lac(self,object):
        self.list_db.append(object)
        print(f'them lien lac thanh cong')
    def sua_lien_lac(self,id,ho_ten_moi,sdt_moi,gioi_tinh_moi):
        for obj in self.list_db:
            if (obj.id == id):
                obj.cap_nhat(ho_ten_moi,sdt_moi,gioi_tinh_moi)
                print('cap nhat thanh cong')
    def xoa_lien_lac(self,id):
        for obj in self.list_db:
            if(obj.id == id):
                self.list_db.remove(obj)
    def hien_thi_db(self):
        for obj in self.list_db:
            obj.hien_thi()

per1 = Object("04","do_dang_minh","097443","nam")
per2 = Object("01","khai","94043434","nu")
per3 = Object("02","nam perfume","0392394324","nam")
danh_ba = [per1,per2]

db1 = DanhBa(danh_ba)

db1.them_lien_lac(per3)
db1.sua_lien_lac("01","hoang hoa","09324234","nam")
# db1.xoa_lien_lac("01")
db1.hien_thi_db()