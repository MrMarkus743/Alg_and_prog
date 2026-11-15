# Задача 1: Базовые операции с множествами (set и frozenset)
def demonstrate_set_basics():
    raw_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    unique_set = set(raw_numbers)

    unique_set.add(6)
    unique_set.discard(2)

    frozen = frozenset([10, 20, 30])
    group_dict = {frozen: "Группа констант"}

    return unique_set, frozen, group_dict[frozen]


# Задача 2: Операции кругов Эйлера над множествами
def calculate_set_relations(set_a, set_b):
    union_res = set_a | set_b
    intersect_res = set_a & set_b
    diff_a_b = set_a - set_b
    sym_diff = set_a ^ set_b
    return union_res, intersect_res, diff_a_b, sym_diff


# Задача 3: Подсчет уникальных символов и пересечение слов текста
def analyze_text_characters(word1, word2):
    chars_1 = set(word1.lower())
    chars_2 = set(word2.lower())

    common_chars = chars_1 & chars_2
    unique_to_first = chars_1 - chars_2

    return common_chars, unique_to_first


# Задача 4: Проверка суммы двух чисел Two-Sum за O(n)
def has_pair_with_sum(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return True, (complement, num)
        seen.add(num)
    return False, None


# Задача 5: Поиск дубликатов в списке за O(n) по времени
def find_all_duplicates(arr):
    seen = set()
    duplicates = set()

    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates


# Задача 6: Проверка на подмножество и надмножество
def check_subsets(small_set, large_set):
    is_sub = small_set.issubset(large_set)
    is_sup = large_set.issuperset(small_set)
    return is_sub and is_sup


if __name__ == "__main__":
    u_set, f_set, f_val = demonstrate_set_basics()
    print("Задача 1: Множество после add/discard:", u_set)
    print(f"  Frozenset: {f_set} | Значение из словаря: {f_val}")

    group_1 = {1, 2, 3, 4, 5}
    group_2 = {4, 5, 6, 7, 8}
    u, inter, d, sym = calculate_set_relations(group_1, group_2)
    print("\nЗадача 2 (Круги Эйлера):")
    print("  Объединение (A | B):", u)
    print("  Пересечение (A & B):", inter)
    print("  Разность (A - B):", d)
    print("  Симметрическая разность (A ^ B):", sym)

    w1, w2 = "алгоритм", "логарифм"
    common, uniq = analyze_text_characters(w1, w2)
    print(f"\nЗадача 3: Анализ слов '{w1}' и '{w2}':")
    print("  Общие буквы:", common)
    print("  Только в первом слове:", uniq)

    nums = [10, 15, 3, 7]
    target = 17
    found, pair = has_pair_with_sum(nums, target)
    print(f"\nЗадача 4 (Two-Sum): сумма {target} в {nums} ->", found, f"пара: {pair}")

    data_with_dups = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 3]
    print("\nЗадача 5: Найденные дубликаты:", find_all_duplicates(data_with_dups))

    subset_a = {1, 2}
    subset_b = {1, 2, 3, 4}
    print("\nЗадача 6: Вхождение подмножества:", check_subsets(subset_a, subset_b))