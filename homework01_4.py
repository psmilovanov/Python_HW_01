# Задача 4. Самая большая цифра.

n = int(input("Введите положительное число: "))
m = n
max_digit = 0
while (m > 0):
    n = m % 10
    if (n > max_digit):
        max_digit = n
    m = m // 10

print("Наибольшая цифра равна ", max_digit)
