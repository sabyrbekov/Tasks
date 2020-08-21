# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: suitcase = [ ]. Однако он
# может вместить всего 5 вещей.
# a. Положите 5 вещей в чемодан с помощью метода .append()
# b. Вы передумали, и решили убрать последнюю вещь. Вспомните, какой метод
# помогает удалить последний элемент.
# c. Вы решили положить в чемодан другую вещь, только в первое место (т.е. по
# индексу 0). Вспомните метод, который ставит элементы по индексу.

suitcase = []
#a
suitcase.append('kalpak')
suitcase.append('tarak')
suitcase.append('tabak')
suitcase.append('barak')
suitcase.append('baypak')
print(suitcase)

#b
suitcase.pop(4)
print(suitcase)

#c
suitcase.insert(0, 'byshtak')
print(suitcase)