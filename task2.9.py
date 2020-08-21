# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих
# соседей и выведите количество таких элементов.(input: 1, 2, 3, 4, 5, output: 0)

a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)