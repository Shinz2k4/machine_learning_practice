import numpy as np
import pandas as pd 

dataset = pd.read_csv("https://raw.githubusercontent.com/thieu1995/csv-files/refs/heads/main/data/python-course/Salary_Data.csv")

print(f'{dataset.info()}')


### hàm vẽ kết quả dự đoán 

## drawing the fitting line

def draw_pred(a,b,x,y):
  x0 = np.linspace(np.min(x),np.max(x),2)