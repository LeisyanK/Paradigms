print("Введите число до 9:")
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(str(i), "*", str(j), "=", str(i*j))