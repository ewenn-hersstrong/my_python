from random import randint
L = ['самовар','весна','лето']
word = L[randint(0,2)]
char = word[randint(0,len(word)-1)]
ind = word.index(char)
hidden = word[:ind]+'?'+word[ind+1:]
print(hidden)
x = input('Введите букву:')
if x == char:
    print(f'Победа! \nСлово: {word}')
else:
    print(f'Увы! Попробуйте в другой раз.\nСлово: {word}')
