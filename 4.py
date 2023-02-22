# Задача 4: 
# Требуется определить, 
# можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите количество долек по вертикали: "))

m = int(input("Введите количество долек по горизонтали: "))

k = int(input("Введите количество долек: "))

if k > n*m:
    print("no")
elif k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")