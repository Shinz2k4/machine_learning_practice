class HinhChuNhat:
    def __init__(self,chieudai,chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def dientich(self):
        dientich = self.chieudai*self.chieurong
        return dientich
hcn = HinhChuNhat(4,5)
print(f"dien tich cua hcn la {hcn.dientich()}")
