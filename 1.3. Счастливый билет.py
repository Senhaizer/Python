number = int(input("Введите номер билета: "))

while number > 1000000 or number < 99999:
    print("Вы ввкли неверный номер билета - в нем должно бють 6 цифр.")
    number = int(input("Введите номер билета: "))

number1 = number % 10
number2 = number % 100 // 10
number3 = number % 1000 // 100
numberA = number1 + number2 + number3

# print(numberA)

number4 = number % 10000 // 1000
number5 = number % 100000 // 10000
number6 = number // 100000
numberB = number4 + number5 + number6

# print(numberB)

if numberA == numberB:
    print(f"Ура! Билет с номером {number} - счастливый! Вам повезло!!!")

else:
    print(f"Очень жаль. Билет с номером {number} не является счастливым. Повезет в другой раз.")
