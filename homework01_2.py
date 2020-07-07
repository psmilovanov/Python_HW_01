#Задание 2. Перевод числа секунд.

user_second = int(input("Введите количество секунд: "))

print(user_second, "секунд = ")
secs = user_second % 60
user_second = user_second // 60
mins = user_second % 60
hours = user_second // 60
print("{}чч:{}мм:{}cc".format(hours, mins, secs))
