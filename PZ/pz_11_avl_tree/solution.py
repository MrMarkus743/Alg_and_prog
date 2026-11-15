from collections import deque


class AVLNode:
    def __init__(self, value):
        self.value = value
        self.link_left = None
        self.link_right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.link_right) - self.get_height(node.link_left)

    def _update_height(self, node):
        if node is not None:
            left_h = self.get_height(node.link_left)
            right_h = self.get_height(node.link_right)
            node.height = 1 + max(left_h, right_h)

    def _rotate_right(self, y):
        x = y.link_left
        t2 = x.link_right

        x.link_right = y
        y.link_left = t2

        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        y = x.link_right
        t2 = y.link_left

        y.link_left = x
        x.link_right = t2

        self._update_height(x)
        self._update_height(y)
        return y

    def _balance_node(self, node):
        self._update_height(node)
        balance = self.get_balance(node)

        # Перевес влево (Left-...)
        if balance < -1:
            if self.get_balance(node.link_left) > 0:
                node.link_left = self._rotate_left(node.link_left)
            return self._rotate_right(node)

        # Перевес вправо (Right-...)
        if balance > 1:
            if self.get_balance(node.link_right) < 0:
                node.link_right = self._rotate_right(node.link_right)
            return self._rotate_left(node)

        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.link_left = self._insert(node.link_left, value)
        elif value > node.value:
            node.link_right = self._insert(node.link_right, value)
        else:
            return node

        return self._balance_node(node)

    def search(self, value):
        curr = self.root
        while curr is not None and curr.value != value:
            if value < curr.value:
                curr = curr.link_left
            else:
                curr = curr.link_right
        return curr

    def _find_min_node(self, node):
        curr = node
        while curr.link_left is not None:
            curr = curr.link_left
        return curr

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.link_left = self._remove(node.link_left, value)
        elif value > node.value:
            node.link_right = self._remove(node.link_right, value)
        else:
            if node.link_left is None:
                return node.link_right
            elif node.link_right is None:
                return node.link_left

            succ = self._find_min_node(node.link_right)
            node.value = succ.value
            node.link_right = self._remove(node.link_right, succ.value)

        return self._balance_node(node)

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

    def preorder(self, node=None, is_root_call=True):
        if is_root_call:
            node = self.root
        if node is None:
            return []
        res = [node.value]
        if node.link_left is not None:
            res.extend(self.preorder(node.link_left, False))
        if node.link_right is not None:
            res.extend(self.preorder(node.link_right, False))
        return res

    def postorder(self, node=None, is_root_call=True):
        if is_root_call:
            node = self.root
        if node is None:
            return []
        res = []
        if node.link_left is not None:
            res.extend(self.postorder(node.link_left, False))
        if node.link_right is not None:
            res.extend(self.postorder(node.link_right, False))
        res.append(node.value)
        return res

    def bfs(self):
        if self.root is None:
            return []
        res = []
        q = deque([self.root])
        while q:
            curr = q.popleft()
            res.append(curr.value)
            if curr.link_left is not None:
                q.append(curr.link_left)
            if curr.link_right is not None:
                q.append(curr.link_right)
        return res

    def display(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
            if node is None:
                print("Дерево пусто")
                return

        if node.link_right is not None:
            self.display(node.link_right, prefix + ("│   " if is_left else "    "), False)

        bal = self.get_balance(node)
        print(f"{prefix}{'└── ' if is_left else '┌── '}{node.value} (b={bal}, h={node.height})")

        if node.link_left is not None:
            self.display(node.link_left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    # Вариант 1 из методички
    elements_to_add = [27, 34, 17, 20, 10, 5, 15, 11, 14, 12, 16, 40, 33, 37]

    avl = AVLTree()
    for val in elements_to_add:
        avl.insert(val)

    print("--- АВЛ-дерево после вставки всех элементов (Вариант 1) ---")
    avl.display()

    print("\n--- Проверка алгоритмов обхода ---")
    print("In-order (LNR, отсортировано):", avl.inorder())
    print("Pre-order (NLR):              ", avl.preorder())
    print("Post-order (LRN):             ", avl.postorder())
    print("BFS (обход в ширину):         ", avl.bfs())

    # Задача 2: Удаление 4 узлов для демонстрации случаев 1a, 1b, 2a, 2b
    demo_tree = AVLTree()
    for item in [50, 20, 70, 10, 30, 60, 80, 5, 25, 35, 75, 85]:
        demo_tree.insert(item)

    print("\n--- Демонстрация балансировки при удалении (Случаи 1a, 1b, 2a, 2b) ---")
    demo_tree.remove(5)
    demo_tree.remove(85)
    demo_tree.remove(10)
    demo_tree.remove(80)
    print("Дерево после удалений:")
    demo_tree.display()