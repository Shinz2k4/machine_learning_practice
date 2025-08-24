# Momentum Gradient Descent Example

X = [2000, 800, 850, 550, 2000]
Y = [250000, 300000, 150000, 70000, 150000]

m = 2.0
b = 4.0

alpha = 1e-7   
mu = 0.9       # momentum
epsilon = 1e-6
max_epochs = 10000

v_m = 0.0
v_b = 0.0

for epoch in range(max_epochs):
    total_dm = 0.0
    total_db = 0.0

    for i in range(len(X)):
        y_pred = m * X[i] + b
        error = Y[i] - y_pred

        dm = -2 * error * X[i]
        db = -2 * error

        total_dm += dm
        total_db += db

    dm_avg = total_dm / len(X)
    db_avg = total_db / len(X)

    # cập nhật momentum
    v_m = mu * v_m - alpha * dm_avg
    v_b = mu * v_b - alpha * db_avg

    # cập nhật tham số
    m += v_m
    b += v_b

    if abs(dm_avg) < epsilon and abs(db_avg) < epsilon:
        print(f"Hội tụ sau {epoch+1} epochs")
        break

print(f"m = {m:.4f}, b = {b:.4f}")


# output: m = 124.4031, b = 587.7961