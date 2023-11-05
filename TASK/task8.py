# Посчитать количество цифр любого целого или вещественного числа,
# число вводит пользователь. Через строку решать нельзя.

# 123 -> 3
# 150.01 -> 5
# 0.0001 -> 5

# n = int(input("Введите число:"))
# count = 0
# while(n > 0):
#     count = count + 1
#     n = n // 10
# print("Количество цифр равно:", count)


number = float(input("Введите число: "))
if number < 0:
    number *= -1

sum_of_digits = 0
while number > 0:
    digit = int(number % 10)
    sum_of_digits += digit
    number //= 10

print("Сумма цифр числа:", sum_of_digits)