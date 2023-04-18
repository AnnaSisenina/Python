# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов.  Определите,  сколько различных слов содержится в
# этом тексте.

# Input:She sells sea shells on the sea shore The shellsthat she sells 
# are sea shells I'm sure.So if she sells seashells on the sea shore
# I'm sure that the shells are seashore shells

Output: 13


text = input('Введите текст: ').upper()
print(f'Количество различных слов в тексте: ', len(set(text.split())))