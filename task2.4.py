# Исходный список содержит положительные и отрицательные числа. Требуется положительные
# поместить в один список, а отрицательные - в другой.


list_of_numbers = [-5, 8, -1, 6, -8, 6, 4, -7]
 
negative = [j for j in list_of_numbers if j < 0]
positive = [j for j in list_of_numbers if j >= 0]
 
print(f'Положительные числа:{positive}\nОтрицательные числа:{negative}')