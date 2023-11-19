# Timur Islamgulov
# Администратор
# sp = []
# sp = [5,3,6,7,True,False, "Hello", 9.99," world "]

# t = tuple(sp)

# t[0] = 123

# print(len(sp))
# print(10 in sp) 
# print(5 in set(sp))
# sp.extend( [777,888])
# sp.insert(0, 123)
# # print(sp)
# del sp[0]
# a = sp.pop()
# sp.remove(True)
# print(sp, a)
# print(sp[1:4])
# s = {1,1,1,1,2,2,2,7,7,7}
# print(s)
# d = {"Ваня": 4564654, "Вася": 56123131}
# d["Виталий"] = 77777
# print(d.keys())
# print(d.values())
# for key, value in d.items():
#     print(f"{key} - {value}")

# 12:26
# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# 12:27
# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# input_list = [1, 1, 2, 0, -1, 3, 4, 4]

# def get_set(list):
#     return len(set(list))

# print(
#     get_set(
#         input_list))




# def move(input_list, pivot):
#     pivot = pivot % len(input_list)

#     left_list = input_list[:-pivot]
#     right_list = input_list[-pivot:]
#     moved_list = right_list + left_list 
#     return moved_list

# input_list = [1, 2, 3, 4, 5]
# k = 7

# print(move(input_list, k))



# def move(input_list, pivot):
#     pivot = pivot % len(input_list)

#     for i in range(pivot):
#         input_list.insert(
#             0, input_list.pop())


# def move(input_list, pivot):
#     pivot = pivot % len(input_list)

#     moved_list = 
#       input_list[-pivot:] + input_list[:-pivot]
#     return moved_list

# input_list = [1, 2, 3, 4, 5]
# k = 7

# move(input_list, k)
# print(input_list)

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит


# # Юлия Чикалева
# dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#         {"VI": "S005"}, {"VII": " S005 "}, {"V":"S009"}, {"VIII":"S007"}]

# res = []

# for dict in dict_list:
#     for key in dict:
#         if dict[key].strip() not in res:
#             res.append(dict[key])
# print(res)





# Андрей Муругов
# def get_unique_values(array):
#     result = []
#     for item in array:
#         result.extend(item.values())
#     result = [value.strip() for value in result]

#     return set(result)

# input_list = [
# {"V": "S001"}, {"V": "S002"}, 
# {"VI": "S001"}, {"VI": "S005"}, 
# {"VII": " S005 "}, {" V ":" S009 "}, 
# {" VIII":" S007 "}
# ]

# print(
#     get_unique_values(input_list))



# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

Aitugan Saktaganov
def fibs(num):
    nums_pos = [0, 1]
    nums_neg = [0, 1]
    for i in range(num - 1):
        nums_pos.append(nums_pos[i] + nums_pos[i + 1])
        nums_neg.append(nums_neg[i] - nums_neg[i + 1])
    return (nums_neg[::-1] + nums_pos)

print(fibs(8))

13:39
def fibs(num):
    nums_pos = [0, 1]
    nums_neg = [0, 1]
    for i in range(num - 1):
        nums_pos.append(nums_pos[i] + nums_pos[i + 1])
        nums_neg.append(nums_neg[i] - nums_neg[i + 1])
    return (nums_neg[:1:-1] + nums_pos)

print(fibs(8))




Виктория Коробьина
def print_value(dicts):
    my_list_without_spaces = []
    for i in dicts:
        for key, value in i.items():
            my_list_without_spaces.append(value.strip())

    return set(my_list_without_spaces)


dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
         {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
         {" VIII":" S007 "}]
print((print_value(dicts)))


