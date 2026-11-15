class BSTNode:
    def __init__(self, value, link_parent=None):
        self.value = value
        self.link_left = None
        self.link_right = None
        self.link_parent = link_parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return self.root

        curr = self.root
        while True:
            if value < curr.value:
                if curr.link_left is None:
                    curr.link_left = BSTNode(value, link_parent=curr)
                    return curr.link_left
                curr = curr.link_left
            elif value > curr.value:
                if curr.link_right is None:
                    curr.link_right = BSTNode(value, link_parent=curr)
                    return curr.link_right
                curr = curr.link_right
            else:
                return curr

    def search(self, value):
        curr = self.root
        while curr is not None and curr.value != value:
            if value < curr.value:
                curr = curr.link_left
            else:
                curr = curr.link_right
        return curr

    def find_min(self, node=None):
        curr = node if node is not None else self.root
        if curr is None:
            return None
        while curr.link_left is not None:
            curr = curr.link_left
        return curr

    def find_max(self, node=None):
        curr = node if node is not None else self.root
        if curr is None:
            return None
        while curr.link_right is not None:
            curr = curr.link_right
        return curr

    def successor(self, node):
        if node is None:
            return None

        if node.link_right is not None:
            return self.find_min(node.link_right)

        curr = node
        parent = curr.link_parent
        while parent is not None and curr == parent.link_right:
            curr = parent
            parent = parent.link_parent
        return parent

    def _transplant(self, u, v):
        if u.link_parent is None:
            self.root = v
        elif u == u.link_parent.link_left:
            u.link_parent.link_left = v
        else:
            u.link_parent.link_right = v

        if v is not None:
            v.link_parent = u.link_parent

    def remove(self, value):
        target = self.search(value)
        if target is None:
            return False

        # Случай 1 и 2: нет левого потомка
        if target.link_left is None:
            self._transplant(target, target.link_right)
        # Случай 2: нет правого потомка
        elif target.link_right is None:
            self._transplant(target, target.link_left)
        # Случай 3: узел имеет обоих потомков
        else:
            succ = self.find_min(target.link_right)
            if succ.link_parent != target:
                self._transplant(succ, succ.link_right)
                succ.link_right = target.link_right
                succ.link_right.link_parent = succ

            self._transplant(target, succ)
            succ.link_left = target.link_left
            succ.link_left.link_parent = succ

        return True

    def display(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
            if node is None:
                print("Дерево пусто")
                return

        if node.link_right is not None:
            self.display(node.link_right, prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        if node.link_left is not None:
            self.display(node.link_left, prefix + ("    " if is_left else "│   "), True)

    def inorder(self, node=None):
        if node is None:
            node = self.root
            if node is None:
                return []
        res = []
        if node.link_left is not None:
            res.extend(self.inorder(node.link_left))
        res.append(node.value)
        if node.link_right is not None:
            res.extend(self.inorder(node.link_right))
        return res


if __name__ == "__main__":
    # Вариант 1
    items_to_add = [27, 34, 17, 20, 10, 5, 15, 11, 14, 12, 16, 40, 33, 37]
    items_to_remove = [33, 15, 14]

    bst = BinarySearchTree()
    for val in items_to_add:
        bst.insert(val)

    print("--- Дерево после построения (Вариант 1) ---")
    bst.display()
    print("\nСимметричный обход (In-order):", bst.inorder())

    min_node = bst.find_min()
    max_node = bst.find_max()
    print(f"Минимум: {min_node.value if min_node else None}")
    print(f"Максимум: {max_node.value if max_node else None}")

    succ_17 = bst.successor(bst.search(17))
    print(f"Последователь узла 17: {succ_17.value if succ_17 else None}")

    print("\n--- Поэтапное удаление узлов: 33, 15, 14 ---")
    for r_val in items_to_remove:
        bst.remove(r_val)
        print(f"\nПосле удаления {r_val}:")
        bst.display()

    print("\nИтоговый обход после удалений:", bst.inorder())