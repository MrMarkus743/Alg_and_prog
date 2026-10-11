import random


# Задача 4: Сортировка выбором через дополнительный список
def selection_sort_two_arrays(arr):
    source = arr.copy()
    sorted_arr = []

    while source:
        min_idx = 0
        for i in range(1, len(source)):
            if source[i] < source[min_idx]:
                min_idx = i
        sorted_arr.append(source.pop(min_idx))

    return sorted_arr


# Задача 4: Сортировка выбором на месте через цикл for
def selection_sort_for(arr):
    res = arr.copy()
    n = len(res)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if res[j] < res[min_idx]:
                min_idx = j
        if min_idx != i:
            res[i], res[min_idx] = res[min_idx], res[i]
    return res


# Задача 4: Сортировка выбором на месте через цикл while
def selection_sort_while(arr):
    res = arr.copy()
    n = len(res)
    i = 0
    while i < n - 1:
        min_idx = i
        j = i + 1
        while j < n:
            if res[j] < res[min_idx]:
                min_idx = j
            j += 1
        if min_idx != i:
            res[i], res[min_idx] = res[min_idx], res[i]
        i += 1
    return res


# Задача 5: Сортировка пузырьком через цикл for с оптимизацией
def bubble_sort_for(arr):
    res = arr.copy()
    n = len(res)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                swapped = True
        if not swapped:
            break
    return res


# Задача 5: Сортировка пузырьком через цикл while с оптимизацией
def bubble_sort_while(arr):
    res = arr.copy()
    n = len(res)
    i = 0
    while i < n - 1:
        swapped = False
        j = 0
        while j < n - 1 - i:
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                swapped = True
            j += 1
        if not swapped:
            break
        i += 1
    return res


# Задачи 6 и 7: Сортировка выбором с логированием и направлением
def selection_sort(arr, verbose=False, reverse=False):
    res = arr.copy()
    n = len(res)
    comparisons = 0

    if verbose:
        print(f"Старт Selection Sort. Массив: {res}, по убыванию: {reverse}")

    for i in range(n - 1):
        target_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if reverse:
                condition = res[j] > res[target_idx]
            else:
                condition = res[j] < res[target_idx]

            if condition:
                target_idx = j

        if target_idx != i:
            res[i], res[target_idx] = res[target_idx], res[i]

        if verbose:
            print(f"Шаг {i + 1}: выбран {res[i]} -> {res}")

    if verbose:
        print(f"Итог: сравнений {comparisons}, результат {res}")

    return res, comparisons


# Задачи 6 и 7: Сортировка пузырьком с логированием и направлением
def bubble_sort(arr, verbose=False, reverse=False):
    res = arr.copy()
    n = len(res)
    comparisons = 0

    if verbose:
        print(f"Старт Bubble Sort. Массив: {res}, по убыванию: {reverse}")

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if reverse:
                need_swap = res[j] < res[j + 1]
            else:
                need_swap = res[j] > res[j + 1]

            if need_swap:
                res[j], res[j + 1] = res[j + 1], res[j]
                swapped = True

        if verbose:
            print(f"Проход {i + 1}: {res} (обмены: {swapped})")

        if not swapped:
            if verbose:
                print("Ранний выход: массив уже упорядочен")
            break

    if verbose:
        print(f"Итог: сравнений {comparisons}, результат {res}")

    return res, comparisons


if __name__ == "__main__":
    base_data = [6, 12, 4, 3, 8]
    print("Исходный массив:", base_data)

    print("\nБазовые реализации:")
    print("Selection Sort (2 массива):", selection_sort_two_arrays(base_data))
    print("Selection Sort (for):      ", selection_sort_for(base_data))
    print("Selection Sort (while):    ", selection_sort_while(base_data))
    print("Bubble Sort (for):         ", bubble_sort_for(base_data))
    print("Bubble Sort (while):       ", bubble_sort_while(base_data))

    print("\nПроверка расширенных функций:")
    selection_sort(base_data, verbose=True, reverse=False)
    bubble_sort(base_data, verbose=True, reverse=True)

    print("\nСтресс-тесты на случайных массивах:")
    random.seed(42)
    test_20 = [random.randint(0, 100) for _ in range(20)]
    test_50 = [random.randint(0, 100) for _ in range(50)]

    sorted_sel_20, cmp_sel_20 = selection_sort(test_20)
    sorted_bub_20, cmp_bub_20 = bubble_sort(test_20)
    print(f"N=20 -> Selection: {cmp_sel_20} сравнений, Bubble: {cmp_bub_20} сравнений")

    sorted_sel_50, cmp_sel_50 = selection_sort(test_50)
    sorted_bub_50, cmp_bub_50 = bubble_sort(test_50)
    print(f"N=50 -> Selection: {cmp_sel_50} сравнений, Bubble: {cmp_bub_50} сравнений")