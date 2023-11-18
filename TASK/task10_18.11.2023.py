# Второй семинар 18.11.2023
# k = 0
# while k < 10:
#     # print(k := k + 1)
#     k = k + 1
#     print(k)

# k = 0
# while True:
#     k += 1
#     print(k)
#     if k == 10:
#         break

# for i in range(10):
#     print(i, end = ", ")

# print(end = '\n')

# for i in (5,9,1,True):
#     print(i)

# for i in range(100, 10, -5):
#     print(i, end = ", ")
# print(end = '\n')
# for i in "Hello, world":
#     print(i, end = ", ")

# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# Задача №11. Общее обсуждение
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# n = int(input("Введите число N: "))
# N=1
# while n>=1:
#     N*=n
#     n-=1

# print(N )

Виктория Коробьина
n = int(input("Введите число: "))

res = 1
while n > 0:
    res = res * n
    n -= 1
print(res)

12:19



m = int(input("Введите число больше 1: "))
f_0 = 0
f_1 = 1
f_2 = 1
n = 3
while f_2 < m:
    f_0 = f_1
    f_1 = f_2
    f_2 = f_0 + f_1
    n += 1
    if m == f_2:
        print(n)
    elif f_2 > m:
        print(-1)

12:25
m = int(input("Введите число больше 1: "))
f_0 = 0
f_1 = 1
f_2 = 1
n = 3
while f_2 < m:
    f_0 = f_1
    f_1 = f_2
    f_2 = f_0 + f_1
    n += 1
    if m == f_2:
        print(n)
    elif f_2 > m:
        if abs(m - f_2) > abs(m - f_1):
            print(f"Это не число Фибоначчи, но ближайшее к нему {f_1}")
        else:
            print(f"Это не число Фибоначчи, но ближайшее к нему {f_2}")

12:30
try:
    m = int(input("Введите число больше 1: "))
    f_0 = 0
    f_1 = 1
    f_2 = 1
    n = 3
    while f_2 < m:
        f_0 = f_1
        f_1 = f_2
        f_2 = f_0 + f_1
        n += 1
        if m == f_2:
            print(n)
        elif f_2 > m:
            if abs(m - f_2) > abs(m - f_1):
                print(f"Это не число Фибоначчи, но ближайшее к нему {f_1}")
            elif abs(m - f_2) < abs(m - f_1):
                print(f"Это не число Фибоначчи, но ближайшее к нему {f_2}")
            else:
                print(f"Это не число Фибоначчи, но ближайшие к нему {f_2} и {f_1}")
except:
    print("Вы ввели неверные данные")



12:39


n = int(input("Input digit: "))

fi = [0, 1]

for i in range(0, n+1):
    fi.append(fi[i]+fi[i+1])
print(fi)


if n in fi:
    print(fi.index(n)+1)
else:
    print(-1)
  
    
    
fib1 = 0
fib2 = 1
n = int(input("Введите число: "))
index = 2
while fib2 < n:
    fib1, fib2 = fib2, fib1 + fib2
    index += 1
if n != fib2:
    index = -1 
print("Индекс этого элемента:", index)
