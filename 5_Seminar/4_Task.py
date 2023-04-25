# Дано натуральное число N и последовательность
# из N элементов. Требуется вывести эту
# последовательность в обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать
# циклы (даже для ввода и вывода).

from random import randint

n = int(input("Введите кол-во чисел в последовательности: "))
def input(n):
    if n==0:
        return randint (1,5)
    randint(1, 5)
    n-=1
    def(n)

print (list)

def num_s(n):
    if n == 0:
        return ''
    res = input()
    return num_s(n - 1) + f'{res} '

print(num_s(5))