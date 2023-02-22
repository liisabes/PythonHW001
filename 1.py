# Задача 1: 
# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трехзначное число: "))

units = number % 10#единицы
print("Единицы: ", units)

tens = number // 10 % 10#десятки
print("Десятки: ", tens)

hundreds = number // 10 // 10#сотни
print("Сотни: ", hundreds)

summ = units + tens + hundreds
print("Сумма: ", summ)