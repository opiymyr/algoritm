while True:
    N = input("Введите целое число N: ")
    if N("-").isdigit():
        N = int(N)
        break
    else:
        print("Ошибка! Введите целое число.")

for i in range(1, N + 1):
    print(i)
