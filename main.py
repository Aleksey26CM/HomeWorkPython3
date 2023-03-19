import random

# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

count = 0
s1 = int(input("Введите кол-во чисел в массиве: "))
a = [random.randint(1, 100) for i in range(s1)]
n = int(input("Введите число для поиска его совпадений в нашем массиве: "))

for i in range(s1):
    if n == a[i]:
        count += 1
print(a)
print(f'Число совпадений с нашим число = {count}')

# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

n = int(input("Введите длину массива "))
z = int(input("Введите максимальное число в массиве: "))
a = [random.randint(1, z) for i in range(n)]
x = int(input("Введите число для нахождения самого ближайшего к нему в массиве, от 1 до 100: "))
print(a)
num1 = []  # массив с минимумом
num2 = []  # массив с максимумом

for num in a:
    if num < x:
        num1.append(num)
    if num > x:
        num2.append(num)

maxMin = max(num1, default = 0)
minMax = min(num2)
q = maxMin - x
w = (minMax - x) * -1

if q > w and maxMin != 0:
    print(f'Самое близкое число к {x} - {maxMin}')
elif w > q:
    print(f'Самое близкое число к {x} - {minMax}')
elif maxMin == 0 or q == w:
    print(f'Самое близкое число к {x} - {minMax}')

print('минимум -', q)
print("максимум -", w)


# Пример
# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● 'Д', 'К', 'Л', 'М', 'П', 'У' – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

def searchWord():  # Разделил словари для что бы исключить совпадения, ну и к сожалению Русские буквы
    # он может читать как английские так и наоборот, хотя можно было бы подгрузить библиотеки и сверять уже на язык
    dicWord_RU = { 1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
                   3: ['Б', 'Г', 'Ё', 'Ь', 'Я'], 4: ['Й', 'Ы'], 5: ['Ж', 'З', 'Ч', 'Ц', 'Ч'], 8: ['Ш', 'Э', 'Ю'],
                   10: ['Ф', 'Щ', 'Ъ'] }
    print('Привет, давай выберем язык: ')
    a = int(input("Выберите язык ввода:\n1 - Русский язык\n2 - English language\nВведите цифру: - "))
    result = 0
    dicWord_EN = { 1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
                   4: ['F', 'H', 'V', 'W', 'Y'], 5: ['K'], 8: ['J', 'X'], 10: ['Q', 'Z'] }
    if a == 2:
        words1 = input("Enter word: ")
        word1 = words1.upper()
        for letter in word1:  # letter это буква нашего слова, здесь мы проходимся по каждой буквы
            for key, item in dicWord_EN.items():  # заходим в наш словарь,
                # Пример (KEY - 1) : (ITEM - ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']), мы заходим в каждый ключ
                # и проверяем каждую букву ниже на совпадение с нашей буквой, нашего слова
                if letter in item:
                    result += key
        print(result)
    if a == 1:
        words1 = input("Введите слово: ")
        word1 = words1.upper()
        for letter in word1:  # letter это буква для, здесь мы проходимся по каждой буквы
            for key, item in dicWord_RU.items():  # здесь мы обращаемся к ключу и элементам находящимся в данном ключе
                if letter in item:  # и проверяем есть ли искомая буква в нашем словаре N-ключа
                    result += key  # сюда записываем "очки" № ключа в котором находится наша буква
        print(result)
    else:
        print("Вы делаете очень глупые ошибики, написанно выше выбрать 1 или 2 !!!\nНам не стоит тратить время друг на "
              "друга, До свидания !")


searchWord()
# вызываем нашу функцию без аргумента она будет работать
