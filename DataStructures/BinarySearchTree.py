# Это класс дерева поиска
# This is a class of search tree
class Node: # Класс узла / Node Class
    __slots__ = ("key", "left", "right")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree: # Класс бинарного дерева поиска / Class of binary search tree
    def __init__(self, keys=()):
        self.root = None
        self._size = 0

        for key in keys:
            self.add(key)

    def __len__(self):
        return self._size

    def contains(self, key):
        node = self.root

        while node is not None:
            if key == node.key:
                return True

            node = node.left if key < node.key else node.right

        return False

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            self._size = 1
            return True

        node = self.root

        while True:
            if key == node.key:
                return False

            if key < node.key:
                if node.left is None:
                    node.left = Node(key)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(key)
                    break
                node = node.right

        self._size += 1
        return True

    def remove(self, key):
        parent = None
        node = self.root

        while node is not None and node.key != key:
            parent = node
            node = node.left if key < node.key else node.right

        if node is None:
            return False

        if node.left is not None and node.right is not None:
            successor_parent = node
            successor = node.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            node.key = successor.key
            parent = successor_parent
            node = successor

        child = node.left if node.left is not None else node.right

        if parent is None:
            self.root = child
        elif parent.left is node:
            parent.left = child
        else:
            parent.right = child

        self._size -= 1
        return True

    def minimum(self):
        if self.root is None:
            raise ValueError("Дерево пусто | Tree is empty")

        node = self.root

        while node.left is not None:
            node = node.left

        return node.key

    def maximum(self):
        if self.root is None:
            raise ValueError("Дерево пусто | Tree is empty")

        node = self.root

        while node.right is not None:
            node = node.right

        return node.key

    def __iter__(self):
        stack = []
        node = self.root

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            yield node.key
            node = node.right

    def height(self):
        if self.root is None:
            return -1

        result = 0
        stack = [(self.root, 0)]

        while stack:
            node, depth = stack.pop()
            result = max(result, depth)

            if node.left is not None:
                stack.append((node.left, depth + 1))

            if node.right is not None:
                stack.append((node.right, depth + 1))

        return result