# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.


string = "a a a b c a a d c d d".split()

dict = {}.fromkeys(string, 0)
print (dict)
for i in string:
    print(f"{i}_{dict[i]}" if dict[i] else i, end=" ")
    dict[i] += 1