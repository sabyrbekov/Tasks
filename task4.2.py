# Напишите программу, которая принимает от пользователя цифру и присваивает его
# переменной given_number.
# Далее, нужно чтобы было следующее:
# a. если given_number делится на цифру 3 и на цифру 5 без остатка, выведите(print())
# "HahaHoo"
# b. если given_number делится на цифру 3 без остатка, выведите(print())"Haha"
# c. если given_number делится на цифру 5 без остатка, выведите(print())"Hoo".
# d. если given_number не делится без остаткf ни на одну из вышеуказанных цифр (т.е. 3 и 5),
# то выведите(print()) "Aaaaa"

given_number = int(input('Введите число: '))

if given_number % 3 == 0:
    if given_number % 5 ==0:
        print('HahaHoo')
if given_number % 3 == 0:
    print('Haha')
elif given_number % 5 == 0:
    print('Hoo')
elif given_number % 3 != 0:
    print('Aaaaa')
elif given_number % 5 != 0:
    print('Aaaaa')

