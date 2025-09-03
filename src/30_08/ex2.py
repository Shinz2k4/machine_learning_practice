import random as rd

state = False
goat = rd.randint(1,100)
dem = 1
while not (state):
    guess = int(input("nhap so ban doan \n"))
    if (guess == goat):
        print(f"lan thu {dem} doan dung roi")
        state = True
    elif(guess > goat):
        print('goat nho hon')
    else:
        print('goat lon hon')
    dem += 1