# Задача 2:
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
s = int(input("Введите количество сделанных журавликов: "))
print(s)

average = s/3
peter = average/2
sergey = average/2
kate = average*2

print("Количество журавликов, сделанных Петей: ", peter)
print("Количество журавликов, сделанных Катей: ", kate)
print("Количество журавликов, сделанных Серёжей: ", sergey)
