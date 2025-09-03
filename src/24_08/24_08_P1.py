# basic gradient example

X = [2000,800,850,550,2000]
Y = [250000,300000,150000,70000,150000]

m = 2.0
b = 4.0

alpha = 1e-7  # learning_rate
epsilon = 1e-6  # ngưỡng hội tụ
max_epoch = 10000

for i in range(len(X)):
    x = X[i] 
    y = Y[i]

    for epoch in range(max_epoch):
        y_pred = m*x + b
        error = y - y_pred 

        dm = -2*x*error
        db = -2*error

        m -= alpha * dm
        b -= alpha * db 

        if abs(dm) < epsilon and abs(db) < epsilon: # khi đạo hàm riêng của cả 2 bé hơn epsilon thì đạt hội tụ ∇J(m,b)≈0
            print(f'Điểm {i} hội tụ tại epoch thứ {epoch}')
            break
print(f'\b Kết quả cuối cùng:')
print(f'm = {m:.6f}')
print(f'b = {b:.6f}')

# Kết quả khi chạy

# Điểm 0 hội tụ tại epoch thứ 22
# Điểm 1 hội tụ tại epoch thứ 244
# Điểm 2 hội tụ tại epoch thứ 214
# Điểm 3 hội tụ tại epoch thứ 497
# Điểm 4 hội tụ tại epoch thứ 21

#  Kết quả cuối cùng:
# m = 74.997988
# b = 4.024842