# задача 1 сложная необязательная Посчитать 
# сумму цифр любого целого или вещественного числа, 
# число вводит пользователь. Через строку решать нельзя.


from math import ceil

n = 700
m = 750

# решение 1
print((n + m - 1) // n)

# решение 2
print(ceil(m / n))


