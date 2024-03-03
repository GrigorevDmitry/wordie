#!/usr/bin/env python3
# Задание №1
# Студент: Иванов Иван Иванович
# Совместно с: Петров Петр Петрович, ...
# Затраты времени: 
import random
import time
# Константы программы
WORD_BASE_FILE = 'wordie_base.txt'
MAX_ATTEMPTS = 6
HELP_STRING = """
Добро пожаловать в игру.

Цель игры: угадать существительно слово из 5 букв.

При каждой попытке ввода нового слова игра дает подсказку есть ли такая буква
в загаданном слове (символ '*') и находится ли она помимо этого на правильном
месте в слове (символ '^').

Для завершения игры нажмите 'Enter' (т.е. введите пустую строку)

"""

def make_word_list(fname: str):
    """Функция чтения файла корректных существительных из 5 букв.

    """
    with open(fname, 'r', encoding='windows-1251') as f:
        words = f.read().split(', ')

    return words


all_words = make_word_list(WORD_BASE_FILE)
    
    # Загадываем приваильное слово случайным образом при помощи встроенного
    # пакета `random`
    
answer = random.choice(all_words)

print(HELP_STRING)    # Выводим приветствия и описания игры

print('Загаданное слово:', answer) #закомментировать


def check(user_word,answer):
    for x in user_word:
        print(x,end="")
    print()
    
        #Если буква на нужном месте - знак ^
      #если буква не на нужном месте - знак *
      #если буквы нет в данном слове - знак _
    for i in range(len(user_word)):
        if user_word[i] == answer[i]:
            print("^",end ="")
        elif user_word[i] in answer:
            print("*",end="")
        else:
            print("_",end="")
               
                #если отгадано - возвращаем TRUE
    if user_word == answer:
        return 1
    else:
        return 0
        


i = 6 # 6 попыток
used = [] # список для уже использованных слов

while i>0:
    user_word=input("\nВведите слово: ") #пользователь вводит слово
    user_word=user_word.lower().strip() #привожу слово к нижнему регистру, убираю лишние пробелы
    
    if user_word == '' or user_word == '     ': # если введен Enter или 5 пробелов - конец игры.
        print("Игра окончена, правильный ответ:",answer)
        break
     
    if (len(user_word)==5 and user_word.isalpha()) and user_word not in used and user_word in all_words: # в слове доложно быть 5 букв, 
                                                                #слово не должно быть в списке использованных слов
        
        used.append(user_word)
        print ('Использованные слова', used)    
        i = i-1 # минус одна попытка
        if check(user_word, answer):
                print("\n",'Вы назвали правильный ответ')
                time.sleep(10)
                break
        else:
            continue
    else:
        print("Пожалуйста, введите слово из 5 букв")
else:
    print("Игра окончена, правильный ответ:",answer)
    time.sleep(10)