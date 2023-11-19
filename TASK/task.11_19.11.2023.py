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



def move(input_list, pivot):
    pivot = pivot % len(input_list)

    for i in range(pivot):
        input_list.insert(
            0, input_list.pop())

# def move(input_list, pivot):
#     pivot = pivot % len(input_list)

#     moved_list = 
#       input_list[-pivot:] + input_list[:-pivot]
#     return moved_list

input_list = [1, 2, 3, 4, 5]
k = 7

move(input_list, k)
print(input_list)