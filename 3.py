# Задача 3: 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number = int(input("Введите шестизначное число: "))
firstPosition = number//100000
secondPosition = number//10000%10
thirdPosition = number//1000%10
fourthPosition = number//100%10
fifthPosition = number//10%10
sixthPosition = number%10

summ1 = firstPosition + secondPosition + thirdPosition
summ2 = fourthPosition + fifthPosition + sixthPosition

print("Сумма первых трех чисел: ", summ1)
print("Сумма последних трех чисел: ", summ2)

if summ1 == summ2:
    print("Билет счастливый: yes")
else:
    print("Билет несчастливый: no")