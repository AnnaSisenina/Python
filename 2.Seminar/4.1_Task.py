num = int(input("Введите число: "))
max = 0
min = 100
for i in range(num):
    count = int(input(f"{i+1} - арбуз: "))
    if count>max:
        max = count
    if count<min:
          min = count
print(f"Max: {max}, Min: {min}")