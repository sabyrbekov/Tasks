# Дан список стран и городов каждой страны. Затем даны названия городов. Для
# каждого города укажите, в какой стране он находится.

m = {}                                  
for i in range(int(input())):           
    country, *cities = input().split()                                         
                                        
    for city in cities:                 
        m[city] = country               
 
 
for i in range(int(input())):           
    print(m[input()])                   