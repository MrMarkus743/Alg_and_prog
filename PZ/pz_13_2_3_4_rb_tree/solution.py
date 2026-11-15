RED = "RED"
BLACK = "BLACK"


class RBNode:
    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.link_left = None
        self.link_right = None
        self.link_parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def _rotate_left(self, x):
        y = x.link_right
        x.link_right = y.link_left
        if y.link_left is not None:
            y.link_left.link_parent = x

        y.link_parent = x.link_parent
        if x.link_parent is None:
            self.root = y
        elif x == x.link_parent.link_left:
            x.link_parent.link_left = y
        else:
            x.link_parent.link_right = y

        y.link_left = x
        x.link_parent = y

    def _rotate_right(self, y):
        x = y.link_left
        y.link_left = x.link_right
        if x.link_right is not None:
            x.link_right.link_parent = y

        x.link_parent = y.link_parent
        if y.link_parent is None:
            self.root = x
        elif y == y.link_parent.link_right:
            y.link_parent.link_right = x
        else:
            y.link_parent.link_left = x

        x.link_right = y
        y.link_parent = x

    def _get_color(self, node):
        if node is None:
            return BLACK
        return node.color

    def insert(self, value):
        new_node = RBNode(value, color=RED)
        if self.root is None:
            new_node.color = BLACK
            self.root = new_node
            return new_node

        curr = self.root
        parent = None
        while curr is not None:
            parent = curr
            if value < curr.value:
                curr = curr.link_left
            elif value > curr.value:
                curr = curr.link_right
            else:
                return curr

        new_node.link_parent = parent
        if value < parent.value:
            parent.link_left = new_node
        else:
            parent.link_right = new_node

        self._fix_insert(new_node)
        return new_node

    def _fix_insert(self, node):
        while node != self.root and self._get_color(node.link_parent) == RED:
            parent = node.link_parent
            grandparent = parent.link_parent

            if parent == grandparent.link_left:
                uncle = grandparent.link_right
                # Случай 2.1: Дядя красный -> смена цветов
                if self._get_color(uncle) == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED
                    node = grandparent
                else:
                    # Случай 2.3: Дядя черный, зигзаг (LR)
                    if node == parent.link_right:
                        node = parent
                        self._rotate_left(node)
                        parent = node.link_parent
                    # Случай 2.2: Дядя черный, прямая линия (LL)
                    parent.color = BLACK
                    grandparent.color = RED
                    self._rotate_right(grandparent)
            else:
                uncle = grandparent.link_left
                # Случай 2.1 симметричный: Дядя красный
                if self._get_color(uncle) == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED
                    node = grandparent
                else:
                    # Случай 2.3 симметричный: Дядя черный, зигзаг (RL)
                    if node == parent.link_left:
                        node = parent
                        self._rotate_right(node)
                        parent = node.link_parent
                    # Случай 2.2 симметричный: Дядя черный, прямая линия (RR)
                    parent.color = BLACK
                    grandparent.color = RED
                    self._rotate_left(grandparent)

        self.root.color = BLACK

    def search(self, value):
        curr = self.root
        while curr is not None and curr.value != value:
            if value < curr.value:
                curr = curr.link_left
            else:
                curr = curr.link_right
        return curr

    def black_height(self, node=None, is_root_call=True):
        if is_root_call:
            node = self.root
        if node is None:
            return 0
        left_bh = self.black_height(node.link_left, False)
        add = 1 if node.color == BLACK else 0
        return left_bh + add

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

        tag = "RED" if node.color == RED else "BLK"
        print(f"{prefix}{'└── ' if is_left else '┌── '}{node.value} [{tag}]")

        if node.link_left is not None:
            self.display(node.link_left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    demo_keys = [10, 15, 9, 11, 16, 17, 18]

    tree = RedBlackTree()
    for key in demo_keys:
        tree.insert(key)

    print("--- Классическое КЧ-дерево (демо из методички) ---")
    tree.display()
    print("\nIn-order обход (отсортирован):", tree.inorder())
    print("Черная высота дерева:", tree.black_height())

    target = 15
    found = tree.search(target)
    print(f"Поиск ключа {target}: {'найден' if found else 'не найден'}")

    # Вариант 1 из методички
    var1_keys = [27, 34, 17, 20, 10, 5, 15, 11, 14, 12, 16, 40, 33, 37]
    var_tree = RedBlackTree()
    for k in var1_keys:
        var_tree.insert(k)

    print("\n--- Классическое КЧ-дерево (Вариант 1) ---")
    var_tree.display()
    print("In-order обход Варианта 1:", var_tree.inorder())
    print("Черная высота Варианта 1:", var_tree.black_height())