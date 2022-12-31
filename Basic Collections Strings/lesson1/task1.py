words = [input('Введите слово: ').lower() for _ in range(3)]

text = input('Введите текст: ').lower()

words_count = [text.count(word) for word in words]
print(words_count)
