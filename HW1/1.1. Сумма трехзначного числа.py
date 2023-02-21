# Найдите сумму цифр трехзначного числа.
# 123 -> 6(1+2+3)
# 100 -> 1(1+0+0)

number = int(input("Введите трехзначное число: "))

while number > 1000 or number < 99:
    print("Вы ввели неверное число.")
    number = int(input("Введите трехзначное число: "))

number1 = number % 10
number2 = number % 100 // 10
number3 = number // 100

print(f"Сумма цифр в числе {number} равна: {number1 + number2 + number3}." )
