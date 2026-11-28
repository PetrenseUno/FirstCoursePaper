# Это класс хеш-таблицы
# This is a class of chained hash-table
class ChainedHashTable:
    def __init__(self, capacity=8, max_load=1.0):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0
        self._max_load = max_load

    def __len__(self):
        return self._size

    def _index(self, key):
        return hash(key) % len(self._buckets)

    def contains(self, key):
        return any(k == key for k in self._buckets[self._index(key)])

    def add(self, key):
        bucket = self._buckets[self._index(key)]
        if any(k == key for k in bucket):
            return False

        if (self._size + 1) / len(self._buckets) > self._max_load:
            self._resize(2 * len(self._buckets))
            bucket = self._buckets[self._index(key)]

        bucket.append(key)
        self._size += 1
        return True

    def remove(self, key):
        bucket = self._buckets[self._index(key)]
        for i, k in enumerate(bucket):
            if k == key:
                bucket[i] = bucket[-1]
                bucket.pop()
                self._size -= 1
                return True
        return False

    def _resize(self, capacity):
        old = self._buckets
        self._buckets = [[] for _ in range(capacity)]
        for bucket in old:
            for key in bucket:
                self._buckets[self._index(key)].append(key)