# Напишите функцию, которая будет определять является ли введенный год,
# високосным или нет.

year = int(input('Введите год и узнайте високосный он или нет: '))


#По юлианскому календарю:
if year % 4 == 0:
    print('По юлианскому календарю этот високосный год')
else:
    print('По юлианскому каледарю этот год невисокосный')


#По григорианскому календарю:
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('По григорианскому календарю этот год високосный')
else:
    print('По григорианскому календарю этот год невисокосный')
        

