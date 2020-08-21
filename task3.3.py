# Дан словарь, состоящий из элементов типа: слово-синоним. Все слова в словаре
# различны. Выведите синоним для последнего слова.

# n = int(input())
# dict_ = {}

# for _ in range(n):
# ____k, v = input().split()
# ____dict_[k] = v

# synonim = input()

# print(dict_.get(synonim) or ''.join([k for k, v in dict_.items() if v == synonim]) or 'No synonim')


abc = int(input())
dictionary = {}

for b in range(abc):
    k, v = input().split()
    dictionary[k] = v

synonim = input()

print(dictionary.get(synonim) or ''.join([k for k, v in dictionary.items() if v == synonim]) or 'No synonim')



# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye