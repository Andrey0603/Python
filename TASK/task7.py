# Посчитать сумму цифр любого целого или вещественного числа,
# число вводит пользователь. Через строку решать нельзя.

number = input("Введите число: ")
sum_of_digits = sum(int(digit) for digit in 
str(number) if digit.isdigit())

print("Сумма цифр числа:", sum_of_digits)