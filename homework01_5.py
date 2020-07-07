# Задание 5. Прибыль и рентабелность

income = float(input("Введите сумму выручки: "))
outcome = float(input("Введите сумму расходов: "))

if (income > outcome):
    print("Ваша фирма работает с прибылью: ", round(income - outcome,2))
    print("Рентабельность бизнеса составляет: ", round((income - outcome) / income, 4))
    job_numb = int(input("Введите количество работников в вашей фирме: "))
    print("Прибыль на одного работника составила:", round((income - outcome) / job_numb, 2))

else:
    print("Ваша фирма прибыль не приносит. Убыток сотставил: ", outcome - income)
