import numpy as np
import torch 

# -----
# cau hinh thiet bi
# -----

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Thiet bi dang dung la: ",device)

x = torch.rand(3,3)

print("Tensor: \n",x)
print("kich thuoc: ",x.shape)
print("loai",x.dtype)
print("gia tri lon nhat la: ",torch.max(x))
print("gia tri nho nhat la: ",torch.min(x))
