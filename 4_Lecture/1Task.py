# В списке хранятся числа. 
# Нужно получить только четные числа и составить список пар (число; квадрат числа)
# Пример: 1 2 3 5 8 15 23 38
# Получить [(2,4), (8,64), (38, 1444)]
nums = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in nums:
#     if i % 2 == 0:
#         res.append((i, i**2))


res = map(int, nums)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res=list(map(lambda x: (x, x**2), res))
print (res)