# Дан список целых чисел. Заменить отрицательные на -1, положительные - на число 1, ноль
# оставить без изменений.


list_of_trister = [84, -145, 34, 0, 40, 99, 46, -13, 11, 7]
print(list_of_trister)
for i in range(len(list_of_trister)):
    if list_of_trister[i] > 0:
        list_of_trister[i] = 1
    elif list_of_trister[i] < 0:
        list_of_trister[i] = -1
print(list_of_trister)