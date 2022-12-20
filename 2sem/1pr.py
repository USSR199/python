#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11
number = float(input("Введите число: "))
while number != int(number):
    number *= 10
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print ('Сумма чисел:')
print(int(sum))
