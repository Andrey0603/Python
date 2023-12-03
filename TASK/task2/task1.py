# посчитать сумму всех натуральных чисел от 1 до n, где n вводится пользователем.

# def summa_cycle(n:int)->int:

#     res=0

#     while True:

#         if n == 0:

#             break

#         res += n

#         n -= 1

#     return res

# def summa_rec(n: int)-> int:

#     if n == 0:

#         return 0

#     return n + summa_rec(n-1)

#    

# n = int(input("Введите натуральное число "))

# print (summa_cycle(n))

# print (summa_rec(n))

#        

# def get_count_all(sp:list)-> int:

#     res = 0

#     for item in sp:

#         if isinstance(item, list):

#             res += get_count_all(item)

#         else:

#             res += item

#     return res

#     

#     

#     

# count_angola = 18

# count_new_york = [20,[10,7]]

# count_chicago = 15

# count_usa = [count_new_york, count_chicago]

# count_all = [count_usa, count_angola]

# print(count_all)

#  

#Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию



#  

# def fi(n, memo={}):

#     if n in [1,2]:

#         return 1

#     if n not in memo:

#         memo[n] = fi(n-1, memo)+fi(n-2, memo)

#     return memo[n]

# print(fi(n:5, memo={}))

#  

# def fib(n):

#     if n in (0, 1):

#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
# list_1 = []
# for i in range (0,10):
#     list_1.append(fib(i))
# print(list_1)    


# print(fib(7))

#  

#  

# Хакер Василий получил доступ к классному журналу и

# хочет заменить все свои минимальные оценки на

# максимальные. Напишите программу, которая

# заменяет оценки Василия, но наоборот: все

# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

#  

#  

#  

#  

# def mark (list, index, max_num):

#     if index == len(list):

#         return

#     if list[index] == max_num:

#         list[index] = min(list)

#     return mark(list, index+1, max_nam)


# list = [1, 4, 4, 3, 4]

# max_nam = max(list)

# mark(list, 0, max_nam)

# print(list)

#  

# def simple_num(num,index = None):

#     if index is None:

#         index = num-1

#     if index == 1:

#         return "YES"

#     if num % index == 0:

#         return " NO"

#     return simple_num(num, index-1) 

# print(simple_num(11))

#    

#     

# def sum_of_digits(n):

#     if n < 10:

#         return n

#     else:

#         return sum_of_digits(n // 10) + sum_of_digits(n % 10)

#  

# result = sum_of_digits(2212)

# print(result)

# Эта функция принимает число и возвращает сумму цифр этого числа.

# Если число меньше 10, то функция просто возвращает это число.

# Иначе функция рекурсивно вызывает себя сначала с целой частью числа (n // 10),

# а затем с остатком (n % 10) и возвращает их сумму.

#  

# def factorial(n):

#     if n == 0:
#         return 1

#     else:
#         return n * factorial(n - 1)



# num = 5

# result = factorial(num)

# print("Факториал числа", num, "равен", result)



# В этой программе функция factorial принимает число n и возвращает его факториал.

# Если число n равно нулю, то функция возвращает 1 (факториал нуля равен 1).

# Если число не равно нулю, функция возвращает само число, умноженное на результат вызова factorial с аргументом, уменьшенным на 1.


# Программа сначала вызывает функцию factorial с аргументом 5. Функция вызывает сама себя с аргументом 4,

# затем с аргументом 3 и т.д. Каждый раз результат умножения возвращается в качестве значения для следующего вызова. В итоге получается ответ 120 (факториал числа 5).
