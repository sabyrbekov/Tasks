# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого
# элемента в списке. Если наибольших элементов несколько, выведите индекс первого из
# них.(input: 1, 2, 3, 2, 1 output: 3, 2)


index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)
