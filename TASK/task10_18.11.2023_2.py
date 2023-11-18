# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# 12:56

n = int(input("Введите количество арбузов: "))
array = []
for i in range(n):
    temp = int(input(f"введите вес арбуза № {i+1}: "))
    array.append(temp)
print(min(array), max(array))



Владимир Астапенко
import random
def number():
    n = int(input("Введите количество дней: "))
    print(n)
    days = []
    for i in range(n):
        days.append(
            random.randint(-50, 50)
        )
    print(*days)
    return days

def find_longest_thaw(temperatures):
    longest_thaw = 0
    current_thaw = 0

    for temperature in temperatures:
        if temperature > 0:
            current_thaw += 1
        else:
            current_thaw = 0

        if current_thaw > longest_thaw:
            longest_thaw = current_thaw

    return longest_thaw

days = number()
print(find_longest_thaw(days))

13:46
Михаил Умнов
n = 6
numbers = "-20 30 -40 50 10 -10".split(" ")

length = 0  # Текущая длина последовательности тёплых дней
max_length = 0  # Максимальная длина последовательности тёплых дней

for i in range(n):
    el = int(numbers[i])

    if el > 0:
        length += 1
    else:
        length = 0

    if length > max_length:
        max_length = length


print(max_length)





from random import randint


def length_days(days):
    temp_days = []
    for i in range(days):
        temp_days.append(randint(-50, 50))
    return temp_days


def max_thaw_days(array):
    thaw_now = 0
    thaw_big = 0
    for i in array:
        if i >= 0:
            thaw_now += 1
            if thaw_big < thaw_now:
                thaw_big = thaw_now
        else:
            thaw_now = 0
    return thaw_big


list_days = length_days(5)

print(list_days)
print(max_thaw_days(list_days))




import random


MIN_TEMPER, MAX_TEMPT = -50, 50


def create_list_days(n):
    days = []
    for i in range(n):
        days.append(
            random.randint(MIN_TEMPER, MAX_TEMPT)
        )
    print(*days)
    return days

def find_longest_thaw(temperatures):
    longest_thaw = 0
    current_thaw = 0

    for temperature in temperatures:
        if temperature > 0:
            current_thaw += 1
        else:
            current_thaw = 0

        if current_thaw > longest_thaw:
            longest_thaw = current_thaw

    return longest_thaw

n = int(input("Введите количество дней: "))
days = create_list_days(n)
print(find_longest_thaw(days))