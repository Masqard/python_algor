# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

from random import random
print('Машина загадала число от 0 до 100, угадай за 10 попыток')
num = round(random() * 100)
count = 1
while count <= 10:
    a = int(input(str(count) + '-я попытка: '))
    if a == num:
        print(f'Поздравляю! Вы угадали число загаданное машиной')
        break
    elif a > num:
        print('перебор')
    else:
        print('мало')
    count += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано число: ', num)