RED = True
BLACK = False


class LLRBNode:
    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.link_left = None
        self.link_right = None


class LeftLeaningRedBlackTree:
    def __init__(self):
        self.root = None

    def _is_red(self, node):
        if node is None:
            return False
        return node.color == RED

    def _rotate_left(self, h):
        x = h.link_right
        h.link_right = x.link_left
        x.link_left = h
        x.color = h.color
        h.color = RED
        return x

    def _rotate_right(self, h):
        x = h.link_left
        h.link_left = x.link_right
        x.link_right = h
        x.color = h.color
        h.color = RED
        return x

    def _color_flip(self, h):
        h.color = not h.color
        if h.link_left is not None:
            h.link_left.color = not h.link_left.color
        if h.link_right is not None:
            h.link_right.color = not h.link_right.color

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.root.color = BLACK

    def _insert(self, h, value):
        if h is None:
            return LLRBNode(value, color=RED)

        if value < h.value:
            h.link_left = self._insert(h.link_left, value)
        elif value > h.value:
            h.link_right = self._insert(h.link_right, value)
        else:
            return h

        # Правило 1: правая красная связь поворачивается влево
        if self._is_red(h.link_right) and not self._is_red(h.link_left):
            h = self._rotate_left(h)

        # Правило 2: две левые красные связи подряд поворачиваются вправо
        if self._is_red(h.link_left) and self._is_red(h.link_left.link_left):
            h = self._rotate_right(h)

        # Правило 3: расщепление 4-узла (оба потомка красные)
        if self._is_red(h.link_left) and self._is_red(h.link_right):
            self._color_flip(h)

        return h

    def search(self, value):
        curr = self.root
        while curr is not None and curr.value != value:
            if value < curr.value:
                curr = curr.link_left
            else:
                curr = curr.link_right
        return curr

    def inorder(self, node=None, is_root_call=True):
        if is_root_call:
            node = self.root
        if node is None:
            return []
        res = []
        if node.link_left is not None:
            res.extend(self.inorder(node.link_left, False))
        res.append(node.value)
        if node.link_right is not None:
            res.extend(self.inorder(node.link_right, False))
        return res

    def display(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
            if node is None:
                print("Дерево пусто")
                return

        if node.link_right is not None:
            self.display(node.link_right, prefix + ("│   " if is_left else "    "), False)

        color_str = "RED" if node.color == RED else "BLK"
        print(f"{prefix}{'└── ' if is_left else '┌── '}{node.value} [{color_str}]")

        if node.link_left is not None:
            self.display(node.link_left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    # Базовый учебный массив из методички
    demo_keys = [10, 15, 9, 11, 16, 17, 18]

    llrb = LeftLeaningRedBlackTree()
    for key in demo_keys:
        llrb.insert(key)

    print("--- Левостороннее красно-черное дерево (демо из методички) ---")
    llrb.display()
    print("\nIn-order обход (отсортирован):", llrb.inorder())

    # Поиск узла
    target = 16
    found_node = llrb.search(target)
    status = "найден" if found_node is not None else "не найден"
    print(f"Поиск ключа {target}: {status}")

    # Проверка Варианта 1 из раздела исходных данных
    variant_1_keys = [27, 34, 17, 20, 10, 5, 15, 11, 14, 12, 16, 40, 33, 37]
    var_tree = LeftLeaningRedBlackTree()
    for k in variant_1_keys:
        var_tree.insert(k)

    print("\n--- Дерево для набора Варианта 1 ---")
    var_tree.display()
    print("In-order обход Варианта 1:", var_tree.inorder())