# Это класс динамического массива
# This is a class of dynamic array

class DynamicArray():

    def __init__(self):
        self._size = 0 # Изначальный размер / Primordial size
        self._capacity = 1 # Изначальная вместимость / Primordial capacity
        self._data = [None] * self._capacity # Изначальные данные / Primordial data

    def __len__(self): 
        return self._size 

    @property #Геттер для вместимости / Capacity getter
    def spacity(self):
        return self._capacity

    def _check_index(self, index): # Проверка на правильность индекса / Checking the index for correctness
        if (0 <= index < self._size) == 0:
            raise IndexError("Индекс вне границ массива | Index out of array bounds")

    def __getitem__(self, index): # Получить данные по индексу / Index getting data
        self._check_index(index)
        return self._data[index]

    def __setitem__(self, index, value): # Присваивание данных по индексу / Set data for index
        self._check_index(index)
        self._data[index] = value

    def _resize(self, new_capacity): # Изменить вместимость массива / Change capacity of array
        new_data = [None] * new_capacity

        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
        self._capacity = new_capacity

    def append(self, value): # Добавление элемента / Adding element
        if self._size == self._capacity:
            self._resize(self._capacity * 2) # Увеличение вместимости в 2 раза / Doubling capacity

        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value): # Вставить новый элемент / Insert a new element
        if not 0 <= index <= self._size:
            raise IndexError("Недопустимая позиция вставки | Invalid insertion position")

        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = value
        self._size += 1

    def pop(self, index=None): # Удаление по индексу / Deletion by index
        if self._size == 0:
            raise IndexError("Массив пуст | Array is empty")

        if index is None:
            index = self._size - 1 

        self._check_index(index)
        value = self._data[index]

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._size -= 1
        self._data[self._size] = None
        return value

    def find(self, value): # Найти индекс значения / Find index of value
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1 # Если нет такого значения в массива / If there is not that value in array