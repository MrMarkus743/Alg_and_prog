import random


# Задача 2: Рекурсивный подсчет элементов списка (аналог len)
def recursive_count(arr):
    if not arr:
        return 0
    return 1 + recursive_count(arr[1:])


# Задача 3: Рекурсивный поиск наибольшего числа в списке (аналог max)
def recursive_max(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    sub_max = recursive_max(arr[1:])
    return max(sub_max, arr[0])


# Задача 5: Быстрая сортировка с выбором опорного элемента и логированием
def quick_sort(arr, pivot_type="random", reverse=False, verbose=False, depth=0):
    if len(arr) <= 1:
        return arr

    if pivot_type == "first":
        pivot_idx = 0
    elif pivot_type == "last":
        pivot_idx = len(arr) - 1
    elif pivot_type == "random":
        pivot_idx = random.randint(0, len(arr) - 1)
    else:
        pivot_idx = len(arr) // 2

    pivot = arr[pivot_idx]

    less = []
    equal = []
    greater = []

    for item in arr:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equal.append(item)

    if verbose:
        indent = "  " * depth
        print(f"{indent}Разбиение (глубина {depth}): массив={arr}, pivot={pivot} (тип: {pivot_type})")
        print(f"{indent}  Меньше: {less}, Равные: {equal}, Больше: {greater}")

    sorted_less = quick_sort(less, pivot_type=pivot_type, reverse=reverse, verbose=verbose, depth=depth + 1)
    sorted_greater = quick_sort(greater, pivot_type=pivot_type, reverse=reverse, verbose=verbose, depth=depth + 1)

    if reverse:
        result = sorted_greater + equal + sorted_less
    else:
        result = sorted_less + equal + sorted_greater

    if verbose and depth == 0:
        print(f"Итог Quick Sort: {result}")

    return result


# Задача 5: Вспомогательная функция слияния двух упорядоченных списков
def merge(left, right, reverse=False):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if reverse:
            condition = left[i] >= right[j]
        else:
            condition = left[i] <= right[j]

        if condition:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Задача 5: Сортировка слиянием с пошаговой визуализацией
def merge_sort(arr, reverse=False, verbose=False, depth=0):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    if verbose:
        indent = "  " * depth
        print(f"{indent}Разделение (глубина {depth}): {arr} -> Левая: {left_part}, Правая: {right_part}")

    sorted_left = merge_sort(left_part, reverse=reverse, verbose=verbose, depth=depth + 1)
    sorted_right = merge_sort(right_part, reverse=reverse, verbose=verbose, depth=depth + 1)

    result = merge(sorted_left, sorted_right, reverse=reverse)

    if verbose:
        indent = "  " * depth
        print(f"{indent}Слияние (глубина {depth}): {sorted_left} + {sorted_right} -> {result}")

    return result


# Задача 6: Сортировка по модулю отсортированного массива за линейное время O(n)
def sort_by_absolute_value(arr):
    n = len(arr)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[pos] = abs(arr[left])
            left += 1
        else:
            result[pos] = abs(arr[right])
            right -= 1
        pos -= 1

    return result


if __name__ == "__main__":
    test_list = [14, 2, 88, 3, 42, 9]
    print(f"Исходный тестовый список: {test_list}")
    print("Задача 2 (длина списка через рекурсию):", recursive_count(test_list))
    print("Задача 3 (максимальный элемент через рекурсию):", recursive_max(test_list))

    print("\nПроверка демонстрации шагов Quick Sort:")
    sample = [45, 67, 79, 40, 23, 15, 29]
    quick_sort(sample, pivot_type="first", verbose=True)

    print("\nПроверка демонстрации шагов Merge Sort:")
    merge_sort(sample, verbose=True)

    print("\nПроверка задачи 6 (сортировка по модулю за O(n)):")
    mixed_sorted = [-12, -7, -3, 0, 2, 5, 9, 15]
    print("Исходный:", mixed_sorted)
    print("По модулю:", sort_by_absolute_value(mixed_sorted))

    print("\nСтресс-тестирование на 5 обязательных наборах данных:")
    random.seed(42)
    datasets = {
        "Вариант 1 (исходные данные)": [45, 67, 79, 40, 40, 23, 15, 29, 47],
        "10 чисел без повторов [0; 100]": random.sample(range(101), 10),
        "20 чисел с повторами [0; 100]": [random.randint(0, 100) for _ in range(20)],
        "30 чисел [-100; 100]": [random.randint(-100, 100) for _ in range(30)],
        "50 чисел [-1000; 1000]": [random.randint(-1000, 1000) for _ in range(50)],
    }

    for name, data in datasets.items():
        res_qs_asc = quick_sort(data, pivot_type="random", reverse=False)
        res_qs_desc = quick_sort(data, pivot_type="random", reverse=True)
        res_ms_asc = merge_sort(data, reverse=False)
        res_ms_desc = merge_sort(data, reverse=True)

        expected_asc = sorted(data)
        expected_desc = sorted(data, reverse=True)

        assert res_qs_asc == expected_asc, f"Ошибка QS asc на {name}"
        assert res_qs_desc == expected_desc, f"Ошибка QS desc на {name}"
        assert res_ms_asc == expected_asc, f"Ошибка MS asc на {name}"
        assert res_ms_desc == expected_desc, f"Ошибка MS desc на {name}"

        print(f"Набор [{name}]: Успешно (Quick Sort и Merge Sort валидны в обоих направлениях)")