#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np

number = np.random.randint(1, 101)    # Загадываем число от 1 до 100.
print("Загадано число от 1 до 100")

        
def score_game(game_core_v2):  # Функция для запуска игры 1000 раз, чтобы узнать,
                               # как быстро алгоритм угадывает число.
    count_ls = []
    np.random.seed(1)  # Фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим.
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток.")
    
    return(score)


def game_core_v2(number): # Определяем функцию "угадывания" числа.
    count = 1 # Устанавливаем счетчик попыток на единицу, чтобы исключить вариант
              # с нулём попыток при угадывании с первого раза.
    int_start = 1 # Задаем начало интервала.
    int_end = 100 # Задаем конец текущего интервала.
    predict = (int_start+int_end) // 2 # Задаем переменную predict как результат вычислений середины текущего интервала.
    
    while predict != number:
        count +=1 # Включаем счетчик попыток.

        if predict < number: # Если число predict меньше угадываемого числа number, то делим текущий интервал
                             # пополам и добавляем это значение к числу predict.
            int_end //= 2
            predict += (int_start+int_end) // 2

        elif predict > number: # Если число predict больше угадываемого числа number, то делим текущий интервал
                               # пополам и отнимаем это значение от числа predict.
            int_end //= 2
            predict -= (int_start+int_end) // 2
          
    return(count) # Выход из цикла, если угадали.

score_game(game_core_v2) # Проверяем результат.

