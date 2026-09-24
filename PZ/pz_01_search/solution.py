a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

#6a. Бинарный поиск
print("\n6a. Бинарный поиск:")
left, right = -1, len(a)
step = 0

while right - left > 1:
    mid = (left + right) // 2
    print(f"\nШаг {step}")
    print(f"Индекс среднего элемента: {mid}")
    print(f"Средний элемент: {a[mid]}")
    
    if a[mid] == 0:
        left = mid
    else:
        right = mid
        
    print(f"left = {left}, right = {right}")
    step += 1

print(f"\nРезультат найден за {step} шагов!")
print(f"Индексы на границе 0 и 1: {left}, {right}")
print(f"Индекс первой единицы: {right}")
print(f"Элемент с этим индексом: {a[right]}")

# 6b. Линейный поиск для сравнения
linear_steps = 0
for i in range(len(a)):
    linear_steps += 1
    if a[i] == 1:
        print(f"\nЛинейный поиск: первая единица на индексе {i} найдена за {linear_steps} шагов")
        break


# Исходный массив для задач 7a, 7b, 7c
arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6]
X = 5
print(f"\nМассив: {arr}")
print(f"Искомое X = {X}\n")

#7a. Первое вхождение X
def first_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

first = first_occurrence(arr, X)
print(f"7a. Первое вхождение {X}: индекс {first}" if first != -1 else f"7a. {X} не найден")

#7b. Последнее вхождение X
def last_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

last = last_occurrence(arr, X)
print(f"7b. Последнее вхождение {X}: индекс {last}" if last != -1 else f"7b. {X} не найден")

#7c. Количество вхождений X
def count_occurrences(arr, x):
    first = first_occurrence(arr, x)
    if first == -1:
        return 0
    last = last_occurrence(arr, x)
    return last - first + 1

count = count_occurrences(arr, X)
print(f"7c. Количество вхождений {X}: {count}")

#7d. Индекс первого четного (граница нечетные/четные)
print("7d. Поиск индекса первого четного числа:")
odd_even_arr = [1, 3, 5, 7, 9, 2, 4, 6, 8]
print(f"  Массив: {odd_even_arr}")

left, right = -1, len(odd_even_arr)
while right - left > 1:
    mid = (left + right) // 2
    if odd_even_arr[mid] % 2 == 1:  #нечетное
        left = mid
    else:                            #четное
        right = mid

print(f"  Индекс первого четного: {right}")
print(f"  Элемент: {odd_even_arr[right]}")


def find_closest(A, B):
    A_sorted = sorted(A)  # сортируем для бинарного поиска
    
    for x in B:
        # Поиск позиции вставки x в A_sorted
        left, right = 0, len(A_sorted) - 1
        pos = len(A_sorted)
        
        while left <= right:
            mid = (left + right) // 2
            if A_sorted[mid] == x:
                pos = mid
                break
            elif A_sorted[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        else:
            pos = left
        
        # Проверяем соседние элементы
        candidates = []
        if pos > 0:
            candidates.append(A_sorted[pos - 1])
        if pos < len(A_sorted):
            candidates.append(A_sorted[pos])
        
        # Выбираем ближайшие
        min_diff = min(abs(x - val) for val in candidates)
        result = sorted(set(val for val in candidates if abs(x - val) == min_diff))
        
        print(f"{x} - {' '.join(map(str, result))}")

# Пример
A = [65, 43, 23, 11, 7]
B = [3, 54, 23, 9, 65]
find_closest(A, B)

print()  # разделитель

A2 = [100, 87, 76, 54, 32, 18, 5]
B2 = [20, 55, 90, 5, 100, 33, 0]
find_closest(A2, B2)