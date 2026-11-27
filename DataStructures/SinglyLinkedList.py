# Это класс односвязного списка
# This is a class of singly linked list
class Node(): # Класс узла / Node class
    __slots__ = ("value", "next")

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class SinglyLinkedList(): # Класс связного списка / Class of linked list

    def __init__(self, values=()):
        self.head = None
        self.tail = None
        self._size = 0 

        for value in values:
            self.append(value)

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current.value
            current = current.next

    def prepend(self, value): 
        node = Node(value, self.head)
        self.head = node

        if self.tail is None:
            self.tail = node

        self._size += 1

    def append(self, value):
        node = Node(value)

        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self._size += 1

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
            current = current.next

        return None

    def get(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Индекс вне границ списка | Index out of list")

        current = self.head

        for _ in range(index):
            current = current.next

        return current.value

    def pop_front(self):
        if self.head is None:
            raise IndexError("Список пуст | List is empty")

        node = self.head
        self.head = node.next
        self._size -= 1

        if self.head is None:
            self.tail = None

        node.next = None
        return node.value

    def remove(self, value):
        previous = None
        current = self.head

        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if current is self.tail:
                    self.tail = previous

                current.next = None
                self._size -= 1
                return True

            previous = current
            current = current.next

        return False

    def reverse(self):
        previous = None
        current = self.head

        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
        