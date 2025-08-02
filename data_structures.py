class DynamicArray:
    """A simple dynamic array (resizable array)."""
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if 0 < self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._data[index]

    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._data[index] = value

    def size(self):
        return self._size


class Matrix:
    """A simple 2D matrix implementation with row/column insertion and deletion."""
    def __init__(self, rows, cols, fill=0):
        self._rows = rows
        self._cols = cols
        self._data = [[fill for _ in range(cols)] for _ in range(rows)]

    def get(self, r, c):
        if not (0 <= r < self._rows and 0 <= c < self._cols):
            raise IndexError("Index out of bounds")
        return self._data[r][c]

    def set(self, r, c, val):
        if not (0 <= r < self._rows and 0 <= c < self._cols):
            raise IndexError("Index out of bounds")
        self._data[r][c] = val

    def insert_row(self, index, row):
        if len(row) != self._cols:
            raise ValueError("Row length mismatch")
        self._data.insert(index, row)
        self._rows += 1

    def delete_row(self, index):
        if not (0 <= index < self._rows):
            raise IndexError("Index out of bounds")
        self._data.pop(index)
        self._rows -= 1

    def insert_col(self, index, col):
        if len(col) != self._rows:
            raise ValueError("Column length mismatch")
        for i in range(self._rows):
            self._data[i].insert(index, col[i])
        self._cols += 1

    def delete_col(self, index):
        if not (0 <= index < self._cols):
            raise IndexError("Index out of bounds")
        for row in self._data:
            row.pop(index)
        self._cols -= 1


class Stack:
    """Stack using DynamicArray."""
    def __init__(self):
        self._arr = DynamicArray()

    def push(self, val):
        self._arr.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        val = self._arr.get(self._arr.size() - 1)
        self._arr.delete(self._arr.size() - 1)
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._arr.get(self._arr.size() - 1)

    def is_empty(self):
        return self._arr.size() == 0


class Queue:
    """Queue implemented as a circular buffer using a Python list."""
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity
        self._head = 0

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._capacity]
        self._data = new_data
        self._capacity = new_cap
        self._head = 0

    def enqueue(self, val):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        idx = (self._head + self._size) % self._capacity
        self._data[idx] = val
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        val = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        if 0 < self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._data[self._head]

    def is_empty(self):
        return self._size == 0


class LinkedListNode:
    """Node for singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Singly linked list with head reference."""
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        node = LinkedListNode(val)
        node.next = self.head
        self.head = node

    def insert_at_tail(self, val):
        node = LinkedListNode(val)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def delete(self, val):
        curr = self.head
        prev = None
        while curr:
            if curr.value == val:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def traverse(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.value)
            curr = curr.next
        return vals


class TreeNode:
    """Node for a general rooted tree."""
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def traverse_preorder(self):
        """Return a list of values in pre-order traversal."""
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse_preorder())
        return result


# Example usage for rooted tree
if __name__ == "__main__":

    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    E = TreeNode("E")
    F = TreeNode("F")
    A.add_child(B)
    A.add_child(C)
    A.add_child(D)
    C.add_child(E)
    C.add_child(F)

    print("Preorder traversal of tree:", A.traverse_preorder())
