# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


print('не рекомендуется вводить больше 3-4 чисел, устанете :D')
a = int(input('Введите кол-во чисел: '))
b = int(input('Введите цифру за какой будем следить: '))
count = 0
for i in range(1, a + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == b:
            count += 1
        m = m // 10

print("Было введено %d раз(а) цифра - %d" % (count, b))
