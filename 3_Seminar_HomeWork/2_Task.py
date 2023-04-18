# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

N=int(input("Введите число элементов массива: "))
X= randint(-10,10)
list_nums=[randint(-10,10) for i in range (N)]

print (f"Массив: {list_nums}; Число: {X};")

delta=abs(list_nums[0]-X)
res=list_nums[0]
i=int (0)
while i<N and delta!=0:
    if delta>abs(list_nums[i]-X):
        delta=abs(list_nums[i]-X)
        res=list_nums[i]
    i+=1
print(res)
