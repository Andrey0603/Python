# Посчитать сумму цифр любого целого или вещественного числа, 
# число вводит пользователь. Через строку решать нельзя.

number = abs(int(input("Введите целое или вещественное число: ")))

# Инициализируем переменные
sum_digits = 0

# Перебираем цифры числа
while number > 0:
    digit = number % 10  # Получаем последнюю цифру числа
    sum_digits += digit  # Добавляем цифру к сумме
    number //= 10  # Удаляем последнюю цифру числа

print("Сумма цифр числа:", sum_digits)


