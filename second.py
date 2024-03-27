from fnmatch import fnmatch

def sum(list):  # Функция суммирования элементов списка, которые были под знаком ?
  return list[1] + list[3] + list[4] + list[5] + list[8] + list[9] + list[11] + list[13]

mas = []
for i in range(39199903990950, 30129903990959 - 1, -1):  # Обратный отсчёт от 
                  #максимального возможного значения к минимальному возможному
    tmpMas = list(map(int, str(i)))    # Список цифр рассматриваемого числа
    if (fnmatch(str(i), "3?1???03??0?5?") and sum(tmpMas) > 55 and sum(tmpMas) < 64 and 
        i % 31 == 0):  # Условия задачи
        mas.append(i)
        if len(mas) == 10:  # Проверяем, что мы нашли 10 чисел
            break

mas.sort()  # Сортируем список по возрастанию
for i in mas:
    print(i)