# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n=int (input('Введите ширину шоколадки n: '))
m=int (input('Введите длину шоколадки m: '))
k = int(input('Введите кол-во долек, которое Вы хотите отломить: '))

if k==n*m or k==0:
    print('Похоже Вы ничего не отломили')
elif k%n==0 or k%m==0:
    print('Вы разломили шоколадку на два прямоугольника')
else:
    print('Так Вы не сможете разломить шоколадку на два прямоугольника')