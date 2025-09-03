# Cập nhật cho toàn bộ dữ liệu ( đôi một hoặc batch size 2 không trộn)

import random

data = [(3, 250000), (2, 300000), (2, 150000), (1, 78000), (4, 150000)]
m, b = 0.0, 0.0
lr, eps, max_epoch = 1e-3, 1e-6, 1000 #learning_rate,epsilon

for epoch in range(max_epoch):
    random.shuffle(data)
    for i in range(0, len(data), 2):
        batch = data[i:i+2] #chia 1 batch gồm 2 mẫu dữ liệu

        dm = sum(2 * (m*x + b - y) * x for x, y in batch) / len(batch)
        db = sum(2 * (m*x + b - y)     for x, y in batch) / len(batch)

        m -= lr * dm
        b -= lr * db

    if max(abs(dm), abs(db)) < eps:
        print(f"Epoch {epoch+1}: m = {m:.4f}, b = {b:.2f}")
        break

print(f"m = {m:.4f}, b = {b:.2f}")


# output: m = 38538.5304, b = 87766.66