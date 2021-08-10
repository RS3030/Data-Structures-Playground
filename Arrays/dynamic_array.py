import ctypes

# Dynamic array is an array that automatically resize(increase) the capacity as per my need.
# Built-in array in Python is dynamic array
#
# creating an array needs contiguous space of memory,
# therefore the resizing is in reality implemented as following
# 1. make a new bigger array
# 2. copy items from the old array
# 3. assign the new array to the old array


class DynamicArray():

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)

    #  get the size of the array (number of items)
    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            return IndexError('Invalid index')
        return self.array[index]

    #  Push the item at the end of the array
    def append(self, item):
        if self.size == self.capacity:
            self._resize(self.capacity*2)  # double the capacity

        self.array[self.size] = item
        self.size += 1

    #  Insert item at ith position
    def insert(self, item, index):
        if not 0 <= index < self.size:
            return IndexError('Invalid index')
        if self.size == self.capacity:
            self._resize(self.capacity*2)  # double the capacity

        # slide items (after the index) by 1
        for i in range(self.size)[index::-1]:
            self.array[i+1] = self.array[i]
        self.array[index] = item
        self.size += 1

    #  Remove the item from end, return the value
    def pop(self):
        self.array[self.size] = None  # not sure this is correct
        self.size -= 1

    #  Remove ith item of the array
    def remove(self, index):
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]
        self.array[self.size] = None
        self.size -= 1

    #  Resize the array (make it a bigger array)
    def _resize(self, new_capacity):
        temp = self.make_array(new_capacity)
        for i in range(self.size):
            temp[i] = self.array[i]
        self.array = temp
        self.capacity = new_capacity

    #  Make a raw array (not Python built-in) using ctypes library
    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()


# -------test---------
# new_array = DynamicArray()
# new_array.append('Hello')
# new_array.append('world')
# new_array.insert('my', 1)
# new_array.remove(1)
# print(new_array.array[1])
# print(new_array.__len__())
