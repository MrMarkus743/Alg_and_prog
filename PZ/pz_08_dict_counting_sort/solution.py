# Задача 1: Базовые операции со словарями (создание, доступ, безопасное получение)
def demonstrate_dict_basics():
    student_scores = {"Анна": 85, "Борис": 92, "Виктор": 78}
    student_scores["Дарья"] = 95
    viktor_score = student_scores.get("Виктор", 0)
    unknown_score = student_scores.get("Глеб", 0)
    return student_scores, viktor_score, unknown_score


# Задача 2: Частотный анализ текста (подсчет вхождений слов через словарь)
def count_word_frequencies(text):
    clean_text = text.lower()
    for char in ",.!?:;-\n\t":
        clean_text = clean_text.replace(char, " ")

    words = clean_text.split()
    frequency_dict = {}

    for word in words:
        if word:
            frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict


# Задача 3: Классическая сортировка подсчетом (Counting Sort) для целых чисел
def counting_sort(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    count_arr = [0] * range_size

    for num in arr:
        count_arr[num - min_val] += 1

    sorted_arr = []
    for offset, count in enumerate(count_arr):
        val = offset + min_val
        sorted_arr.extend([val] * count)

    return sorted_arr


# Задача 4: Сортировка подсчетом через словарь (для разреженных диапазонов)
def counting_sort_dict(arr):
    if not arr:
        return []

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    sorted_arr = []
    for key in sorted(freq.keys()):
        sorted_arr.extend([key] * freq[key])

    return sorted_arr


# Задача 5: Проверка взаимного боя ладей на шахматной доске за O(n)
def check_rooks_threaten_each_other(rooks_coords):
    row_counts = {}
    col_counts = {}

    for r, c in rooks_coords:
        row_counts[r] = row_counts.get(r, 0) + 1
        col_counts[c] = col_counts.get(c, 0) + 1

    for count in row_counts.values():
        if count > 1:
            return True

    for count in col_counts.values():
        if count > 1:
            return True

    return False


# Задача 6: Объединение словарей с суммированием числовых значений
def merge_and_sum_dicts(dict_a, dict_b):
    result = dict_a.copy()
    for key, value in dict_b.items():
        result[key] = result.get(key, 0) + value
    return result


if __name__ == "__main__":
    scores, viktor, unknown = demonstrate_dict_basics()
    print("Задача 1: Словарь студентов:", scores)
    print(f"  Оценка Виктора: {viktor}, Неизвестный: {unknown}")

    sample_text = "Яблоко груша яблоко слива вишня груша яблоко"
    freq = count_word_frequencies(sample_text)
    print("\nЗадача 2: Частоты слов:", freq)

    numbers = [4, 2, 2, 8, 3, 3, 1]
    sorted_numbers = counting_sort(numbers)
    print("\nЗадача 3: Исходный массив:", numbers)
    print("  Counting Sort (массив):", sorted_numbers)

    sparse_numbers = [1000, 5, 1000, 20, 5]
    sorted_sparse = counting_sort_dict(sparse_numbers)
    print("  Counting Sort (словарь):", sorted_sparse)

    rooks_safe = [(1, 1), (2, 3), (3, 5), (4, 2)]
    rooks_threat = [(1, 1), (2, 3), (1, 7)]
    print("\nЗадача 5: Ладьи безопасны:", not check_rooks_threaten_each_other(rooks_safe))
    print("Задача 5: Ладьи бьют друг друга:", check_rooks_threaten_each_other(rooks_threat))

    warehouse_a = {"яблоки": 50, "груши": 30, "сливы": 15}
    warehouse_b = {"яблоки": 20, "бананы": 40, "сливы": 10}
    merged_stock = merge_and_sum_dicts(warehouse_a, warehouse_b)
    print("\nЗадача 6: Объединенный склад:", merged_stock)