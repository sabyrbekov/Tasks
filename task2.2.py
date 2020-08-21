# Дан список, состоящая ровно из двух строк. Переставьте эти слова местами. Результат запишите
# в список и выведите получившийся список.

abc = input()
word_num_1 = abc[:abc.find(' ')]
word_num_2 = abc[abc.find(' ') + 1:]
print("Last word : " + word_num_2 + ' ' + "First word: " + word_num_1)