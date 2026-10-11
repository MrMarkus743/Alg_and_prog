# Задача 1: Суммирование цифр числа
def task1_funct(n):
    if n < 10:
        return n
    else:
        return n % 10 + task1_funct(n // 10)


# Задача 2: Построение числовой строки
def task2_funct(k, n):
    if k < n:
        return str(k) + " " + str(task2_funct(k + 1, n))
    else:
        return str(n)


# Задача 3а: Рекурсивное суммирование всех чисел списка
def recursive_sum(arr):
    if not arr:
        return 0
    return arr[0] + recursive_sum(arr[1:])


# Задача 3б: Рекурсивное суммирование только положительных чисел
def recursive_sum_plus(arr):
    if not arr:
        return 0
    current = max(0, arr[0])
    return current + recursive_sum_plus(arr[1:])


# Задача 4: Подсчет нечетных элементов через цикл
def count_odd_iterative(arr):
    count = 0
    for x in arr:
        if x % 2 != 0:
            count += 1
    return count


# Задача 4: Подсчет нечетных элементов через рекурсию
def count_odd_recursive(arr):
    if not arr:
        return 0
    is_odd = 1 if arr[0] % 2 != 0 else 0
    return is_odd + count_odd_recursive(arr[1:])


# Задача 5: Проверка правильности скобочной последовательности через стек
def is_valid_brackets(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# Задача 6: Минимальное количество скобок для удаления (итеративно)
def min_remove_brackets_iter(s):
    open_count = 0
    to_remove = 0

    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                to_remove += 1

    return to_remove + open_count


# Задача 6: Минимальное количество скобок для удаления (рекурсивно)
def min_remove_brackets_rec(s, open_count=0):
    if not s:
        return open_count

    first = s[0]
    rest = s[1:]

    if first == '(':
        return min_remove_brackets_rec(rest, open_count + 1)
    elif first == ')':
        if open_count > 0:
            return min_remove_brackets_rec(rest, open_count - 1)
        else:
            return 1 + min_remove_brackets_rec(rest, 0)
    else:
        return min_remove_brackets_rec(rest, open_count)


# Задачи 7 и 8: Добавление недостающих скобок до правильной строки
def complete_bracket_sequence(s):
    stack = []
    needed_left = []
    pairs = {')': '(', ']': '[', '}': '{'}
    open_for_close = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                needed_left.append(pairs[char])

    needed_right = [open_for_close[ch] for ch in reversed(stack)]
    fixed_s = "".join(needed_left) + s + "".join(needed_right)
    return len(needed_left) + len(needed_right), fixed_s


if __name__ == "__main__":
    print("Задача 1: funct(230) =", task1_funct(230))
    print("Задача 2: funct(4, 12) =", task2_funct(4, 12))

    data_all = [10, 5, 5, 20]
    data_with_neg = [10, -5, 5, -20, 15]
    print(f"Задача 3а: сумма {data_all} =", recursive_sum(data_all))
    print(f"Задача 3б: сумма положительных {data_with_neg} =", recursive_sum_plus(data_with_neg))

    arr_test = [2, 5, 8, 11, 13, 14]
    print(f"Задача 4: нечетных в {arr_test} (цикл) =", count_odd_iterative(arr_test))
    print(f"Задача 4: нечетных в {arr_test} (рекурсия) =", count_odd_recursive(arr_test))

    case_a = "{}[()](())"
    case_b = "()]()()[]"
    print(f"Задача 5: '{case_a}' корректна ->", is_valid_brackets(case_a))
    print(f"Задача 5: '{case_b}' корректна ->", is_valid_brackets(case_b))

    unbalanced_str = "(()))("
    print(f"Задача 6: удалить из '{unbalanced_str}' (итеративно) =", min_remove_brackets_iter(unbalanced_str))
    print(f"Задача 6: удалить из '{unbalanced_str}' (рекурсивно) =", min_remove_brackets_rec(unbalanced_str))

    my_bad_seq = "()[{]("
    add_count, fixed = complete_bracket_sequence(my_bad_seq)
    print(f"Задачи 7-8: строка '{my_bad_seq}' -> добавить {add_count} -> '{fixed}'")