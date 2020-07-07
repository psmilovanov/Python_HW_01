# Задание 3. Вывести n+nn+nnn.

n = int(input("Введите положительное число n: "))
digit_number = 0
m = n

while (m > 0):
    m = m // 10
    digit_number += 1

print("Сумма n + nn + nnn = ", n + (n + n * 10 ** digit_number) + (n + n * 10 ** digit_number + n * 10 ** (2 * digit_number)))
