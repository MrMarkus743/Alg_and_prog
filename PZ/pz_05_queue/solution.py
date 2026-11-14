from collections import deque
from queue import LifoQueue, Queue


# Задача 1: Стек (N чисел, извлечь все элементы и вывести количество N)
def task_1_list(numbers):
    stack = []
    for x in numbers: 
        stack.append(x)
    count = 0
    extracted = []
    while len(stack) > 0:
        extracted.append(stack.pop())
        count += 1
    return extracted, count


def task_1_deque(numbers):
    stack = deque()
    for x in numbers:
        stack.append(x)
    count = 0
    extracted = []
    while len(stack) > 0:
        extracted.append(stack.pop())
        count += 1
    return extracted, count


def task_1_lifo(numbers):
    stack = LifoQueue()
    for x in numbers:
        stack.put(x)
    count = 0
    extracted = []
    while not stack.empty():
        extracted.append(stack.get())
        count += 1
    return extracted, count


# Задача 2: Переместить все элементы из первого стека во второй
def task_2(stack1, stack2):
    while len(stack1) > 0:
        stack2.append(stack1.pop())


# Задача 3: Разложить непустой стек на четные и нечетные значения
def task_3_deque(source_stack):
    even_stack = deque()
    odd_stack = deque()
    while len(source_stack) > 0:
        val = source_stack.pop()
        if val % 2 == 0:
            even_stack.append(val)
        else:
            odd_stack.append(val)
    return even_stack, odd_stack


def task_3_lifo(source_stack):
    even_stack = LifoQueue()
    odd_stack = LifoQueue()
    while not source_stack.empty():
        val = source_stack.get()
        if val % 2 == 0:
            even_stack.put(val)
        else:
            odd_stack.put(val)
    return even_stack, odd_stack


# Задача 4: Очередь (N чисел, извлечь все элементы и вывести количество N)
def task_4_list(numbers):
    q = []
    for x in numbers:
        q.append(x)
    count = 0
    extracted = []
    while len(q) > 0:
        extracted.append(q.pop(0))
        count += 1
    return extracted, count


def task_4_deque(numbers):
    q = deque()
    for x in numbers:
        q.append(x)
    count = 0
    extracted = []
    while len(q) > 0:
        extracted.append(q.popleft())
        count += 1
    return extracted, count


def task_4_queue(numbers):
    q = Queue()
    for x in numbers:
        q.put(x)
    count = 0
    extracted = []
    while not q.empty():
        extracted.append(q.get())
        count += 1
    return extracted, count


# Задача 5: Две очереди по четным и нечетным индексам исходного набора
def task_5(numbers):
    q_odd_idx = deque()
    q_even_idx = deque()
    for i in range(len(numbers)):
        if i % 2 != 0:
            q_odd_idx.append(numbers[i])
        else:
            q_even_idx.append(numbers[i])
    return q_odd_idx, q_even_idx


# Задача 6: Две очереди по нечетным и четным значениям чисел
def task_6(numbers):
    q_odd = deque()
    q_even = deque()
    for x in numbers:
        if x % 2 != 0:
            q_odd.append(x)
        else:
            q_even.append(x)
    return q_odd, q_even


# Задача 7: Добавить число D в конец очереди и извлечь первый элемент
def task_7(q, d):
    q.append(d)
    return q.popleft()


# Задача 8: Извлечь N начальных элементов из очереди
def task_8(q, n):
    extracted = []
    count = 0
    while len(q) > 0 and count < n:
        extracted.append(q.popleft())
        count += 1
    return extracted


# Задача 9: Извлекать элементы, пока начальный элемент не станет четным
def task_9(q):
    extracted = []
    while len(q) > 0:
        first = q.popleft()
        extracted.append(first)
        if first % 2 == 0:
            break
    return extracted


# Задача 10: Переместить все элементы первой очереди в конец второй
def task_10(q1, q2):
    while len(q1) > 0:
        q2.append(q1.popleft())


# Задача 11: Переместить N начальных элементов первой очереди в конец второй
def task_11_deque(q1, q2, n):
    count = 0
    while len(q1) > 0 and count < n:
        q2.append(q1.popleft())
        count += 1


def task_11_queue(q1, q2, n):
    count = 0
    while not q1.empty() and count < n:
        q2.put(q1.get())
        count += 1


# Задача 12: Объединить очереди одинаковой длины с чередованием элементов
def task_12(q1, q2):
    result = deque()
    while len(q1) > 0 and len(q2) > 0:
        result.append(q1.popleft())
        result.append(q2.popleft())
    return result


# Задача 13: Слияние двух упорядоченных очередей с сохранением порядка
def task_13_deque(q1, q2):
    result = deque()
    while len(q1) > 0 and len(q2) > 0:
        val1 = q1.popleft()
        val2 = q2.popleft()
        if val1 <= val2:
            result.append(val1)
            q2.appendleft(val2)
        else:
            result.append(val2)
            q1.appendleft(val1)

    while len(q1) > 0:
        result.append(q1.popleft())
    while len(q2) > 0:
        result.append(q2.popleft())

    return result


def task_13_queue(q1, q2):
    result = Queue()
    v1 = None
    v2 = None

    while not q1.empty() or v1 is not None or not q2.empty() or v2 is not None:
        if v1 is None and not q1.empty():
            v1 = q1.get()
        if v2 is None and not q2.empty():
            v2 = q2.get()

        if v1 is not None and v2 is not None:
            if v1 <= v2:
                result.put(v1)
                v1 = None
            else:
                result.put(v2)
                v2 = None
        elif v1 is not None:
            result.put(v1)
            v1 = None
        elif v2 is not None:
            result.put(v2)
            v2 = None

    return result


if __name__ == "__main__":
    nums = [10, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125]
    print(f"Базовый массив (N={len(nums)}): {nums}")

    # Проверка Задачи 1
    res1, n1 = task_1_deque(nums[:5])
    print("\nЗадача 1 (извлечение из стека):", res1, f"| Всего: {n1}")

    # Проверка Задачи 2
    s1 = [1, 2, 3]
    s2 = [10, 20]
    task_2(s1, s2)
    print("Задача 2 (перенос стека): s1 опустел, s2 =", s2)

    # Проверка Задачи 3
    s_orig = deque([1, 2, 3, 4, 5, 6])
    ev, od = task_3_deque(s_orig)
    print("Задача 3 (чет/нечет стек): четные =", list(ev), "нечетные =", list(od))

    # Проверка Задачи 4
    res4, n4 = task_4_deque(nums)
    print("\nЗадача 4 (очередь deque):", res4, f"| Извлечено: {n4}")

    # Проверка Задач 5 и 6
    ten_nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    q_odd_i, q_ev_i = task_5(ten_nums)
    print("Задача 5 (по индексам): нечетные индексы =", list(q_odd_i))
    q_odd_v, q_ev_v = task_6(ten_nums)
    print("Задача 6 (по значениям): нечетные числа =", list(q_odd_v))

    # Проверка Задач 7, 8, 9
    test_q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    out7 = task_7(test_q, 999)
    print("\nЗадача 7: добавлен 999 в хвост, извлечен из головы:", out7)

    out8 = task_8(test_q, 4)
    print("Задача 8: извлечено 4 элемента:", out8)

    q_until_even = deque([1, 3, 5, 7, 8, 9, 11])
    out9 = task_9(q_until_even)
    print("Задача 9: извлечение до первого четного:", out9)

    # Проверка Задач 10 и 11
    q_a = deque([1, 2, 3])
    q_b = deque([10, 20])
    task_10(q_a, q_b)
    print("\nЗадача 10: слияние очередей q_b =", list(q_b))

    q_c = deque([100, 200, 300, 400])
    q_d = deque([10, 20])
    task_11_deque(q_c, q_d, 2)
    print("Задача 11: перенос 2 элементов из q_c в конец q_d =", list(q_d))

    # Проверка Задачи 12
    q_first = deque([1, 3, 5])
    q_second = deque([2, 4, 6])
    interleaved = task_12(q_first, q_second)
    print("\nЗадача 12 (чередование):", list(interleaved))

    # Проверка Задачи 13
    sorted_q1 = deque([2, 5, 10, 15])
    sorted_q2 = deque([1, 4, 8, 20])
    merged_sorted = task_13_deque(sorted_q1, sorted_q2)
    print("Задача 13 (слияние отсортированных):", list(merged_sorted))