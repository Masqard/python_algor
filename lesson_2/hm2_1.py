# 2.  Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# https://drive.google.com/file/d/1giTLScEcInxk-iT6GzDsM8W7prU8ZISk/view?usp=sharing

even = 0
odds = 0

number = input('Введите число: ')

for numbs in number:
    i = int(numbs)
    if i % 2 == 0:
        even += 1
    else:
        odds += 1

print(f'у числа {number} четных чисел {even} и не четных {odds}')
