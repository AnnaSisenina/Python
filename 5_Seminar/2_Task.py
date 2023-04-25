# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# 8
# 5 4 2 2 4 2 2 5

numbers = list(map(int, input().split()))
max_l = max(numbers)
min_l = min(numbers)
result = [i if i != max_l else min_l for i in numbers]
print(result)