# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

ticketNumber=str(input("Введите номер билета: "))
firstPart=int(ticketNumber[:len(ticketNumber)//2])
secondPart=int(ticketNumber[len(ticketNumber)//2:])
sumFirst=int(0)
sumSecond=int(0)
count=int(0)
while (count<len(ticketNumber)//2):
    sumFirst=sumFirst+firstPart%10
    firstPart//=10
    sumSecond=sumSecond+secondPart%10
    secondPart//=10
    count+=1

print('У Вас счастливый билет!') if sumFirst==sumSecond else print('Обычный билет. Повезет в следующий раз!=)')

