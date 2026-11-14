import time


# Задача 1: Однонаправленный связный список (Singly Linked List)
class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.link_next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(curr.value)
            curr = curr.link_next
        return elements

    def append(self, value):
        new_node = SinglyNode(value)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.link_next is not None:
            curr = curr.link_next
        curr.link_next = new_node

    def prepend(self, value):
        new_node = SinglyNode(value)
        new_node.link_next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        if self.head.link_next is None:
            val = self.head.value
            self.head = None
            return val
        curr = self.head
        while curr.link_next.link_next is not None:
            curr = curr.link_next
        val = curr.link_next.value
        curr.link_next = None
        return val

    def pop_first(self):
        if self.head is None:
            return None
        val = self.head.value
        self.head = self.head.link_next
        return val

    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.link_next
        return None

    def insert_after(self, target_value, value):
        node = self.find(target_value)
        if node is None:
            return False
        new_node = SinglyNode(value)
        new_node.link_next = node.link_next
        node.link_next = new_node
        return True

    def remove(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.link_next
            return True
        curr = self.head
        while curr.link_next is not None:
            if curr.link_next.value == value:
                curr.link_next = curr.link_next.link_next
                return True
            curr = curr.link_next
        return False


# Задача 2: Двунаправленный связный список (Doubly Linked List)
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.link_next = None
        self.link_prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(curr.value)
            curr = curr.link_next
        return elements

    def append(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.link_next is not None:
            curr = curr.link_next
        curr.link_next = new_node
        new_node.link_prev = curr

    def prepend(self, value):
        new_node = DoublyNode(value)
        if self.head is not None:
            self.head.link_prev = new_node
            new_node.link_next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        if self.head.link_next is None:
            val = self.head.value
            self.head = None
            return val
        curr = self.head
        while curr.link_next is not None:
            curr = curr.link_next
        val = curr.value
        curr.link_prev.link_next = None
        return val

    def pop_first(self):
        if self.head is None:
            return None
        val = self.head.value
        self.head = self.head.link_next
        if self.head is not None:
            self.head.link_prev = None
        return val

    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.link_next
        return None

    def insert_after(self, target_value, value):
        node = self.find(target_value)
        if node is None:
            return False
        new_node = DoublyNode(value)
        new_node.link_next = node.link_next
        new_node.link_prev = node
        if node.link_next is not None:
            node.link_next.link_prev = new_node
        node.link_next = new_node
        return True

    def remove(self, value):
        node = self.find(value)
        if node is None:
            return False
        if node == self.head:
            self.pop_first()
            return True
        if node.link_next is not None:
            node.link_next.link_prev = node.link_prev
        if node.link_prev is not None:
            node.link_prev.link_next = node.link_next
        return True


# Задача 3: Циклический связный список (Circular Linked List)
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            return []
        elements = [self.head.value]
        curr = self.head.link_next
        while curr != self.head:
            elements.append(curr.value)
            curr = curr.link_next
        return elements

    def append(self, value):
        new_node = SinglyNode(value)
        if self.head is None:
            self.head = new_node
            new_node.link_next = new_node
            return
        curr = self.head
        while curr.link_next != self.head:
            curr = curr.link_next
        curr.link_next = new_node
        new_node.link_next = self.head

    def pop(self):
        if self.head is None:
            return None
        if self.head.link_next == self.head:
            val = self.head.value
            self.head = None
            return val
        curr = self.head
        while curr.link_next.link_next != self.head:
            curr = curr.link_next
        val = curr.link_next.value
        curr.link_next = self.head
        return val


# Задача 4: Очередь на базе связного списка с фиксацией хвоста за O(1)
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = SinglyNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.link_next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        val = self.head.value
        self.head = self.head.link_next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return val

    def display(self):
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(curr.value)
            curr = curr.link_next
        return elements


def task_4_process(numbers):
    q = LinkedQueue()
    for x in numbers:
        q.enqueue(x)
    extracted = []
    count = 0
    while not q.is_empty():
        extracted.append(q.dequeue())
        count += 1
    return extracted, count


def task_4_move_all(q1, q2):
    while not q1.is_empty():
        q2.enqueue(q1.dequeue())


def task_4_move_n(q1, q2, n):
    count = 0
    while not q1.is_empty() and count < n:
        q2.enqueue(q1.dequeue())
        count += 1


# Задачи 5* и 6*: Симуляция системы обработки заявок
def simulate_single_worker(tasks):
    q = LinkedQueue()
    for t in tasks:
        q.enqueue(t)
    start_time = time.time()
    while not q.is_empty():
        task = q.dequeue()
        time.sleep(task["duration"])
    return round(time.time() - start_time, 2)


def simulate_three_workers(tasks):
    workers = [
        {"id": 1, "speed": 1.00, "busy_until": 0.0},
        {"id": 2, "speed": 1.01, "busy_until": 0.0},
        {"id": 3, "speed": 2.00, "busy_until": 0.0},
    ]
    current_time = 0.0
    for task in tasks:
        next_worker = min(workers, key=lambda w: w["busy_until"])
        start = max(current_time, next_worker["busy_until"])
        finish = start + next_worker["speed"]
        next_worker["busy_until"] = finish

    total_time = max(w["busy_until"] for w in workers)
    return round(total_time, 2)


if __name__ == "__main__":
    print("--- Проверка однонаправленного списка (Задача 1) ---")
    s_list = SinglyLinkedList()
    s_list.append(10)
    s_list.append(20)
    s_list.prepend(5)
    print("После append и prepend:", s_list.display())
    s_list.insert_after(10, 15)
    print("После вставки 15 после 10:", s_list.display())
    s_list.remove(20)
    print("После удаления 20:", s_list.display())

    print("\n--- Проверка двунаправленного списка (Задача 2) ---")
    d_list = DoublyLinkedList()
    d_list.append(1)
    d_list.append(2)
    d_list.prepend(0)
    print("Двунаправленный список:", d_list.display())
    d_list.insert_after(1, 100)
    print("После вставки 100 после 1:", d_list.display())
    d_list.remove(100)
    print("После удаления 100:", d_list.display())

    print("\n--- Проверка циклического списка (Задача 3) ---")
    c_list = CircularLinkedList()
    c_list.append(10)
    c_list.append(20)
    c_list.append(30)
    print("Циклический список:", c_list.display())
    c_list.pop()
    print("После pop:", c_list.display())

    print("\n--- Проверка очереди на связном списке (Задача 4) ---")
    test_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    extracted, count = task_4_process(test_nums)
    print(f"Извлечено: {extracted} (N={count})")

    q1 = LinkedQueue()
    q2 = LinkedQueue()
    for val in [100, 200, 300]:
        q1.enqueue(val)
    for val in [10, 20]:
        q2.enqueue(val)
    task_4_move_n(q1, q2, 2)
    print("Очередь q2 после перемещения 2 элементов из q1:", q2.display())

    print("\n--- Моделирование обработки 20 заявок (Задачи 5*-6*) ---")
    task_list = [{"id": i + 1} for i in range(20)]
    total_sec = simulate_three_workers(task_list)
    print(f"Обработано 20 заявок тремя обработчиками: {total_sec} сек")