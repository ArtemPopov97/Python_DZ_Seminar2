# Напишите программу, которая принимает на вход число N и выдает набор 
# произведений (набор - это список)  чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

Number = int(input('Введите число: '))
sum = 1
    
for i in range(1, Number + 1):
    sum *= i
    print(sum, end=' ')