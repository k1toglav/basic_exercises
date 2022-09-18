# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
counter = 0
for i in range(len(word)):
    if word.upper()[i] == 'А':
        counter += 1
print(counter)


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel = 'ауоыэяюёие'
counter = 0
for letter in word.lower():
    if letter in vowel:
        counter += 1
print('Количество гласных', counter)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for i in range(len(words)):
    print(words[i][0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
counter = 0
words = sentence.split()
for i in range(len(words)):
    counter += len(words[i])
print(counter / len(words))