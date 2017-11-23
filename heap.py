import math

class Heap():
    heap = []
    heap_size = 0

    def __init__(self, initial_heap):
        self.heap = initial_heap[:]
        self.heap_size = len(self.heap)
        self.__build_max_heap()

    def __str__(self):
        return str(self.heap[:self.heap_size])

    def __left_index(self, i):
        if i != 0:
            return 2*i - 1
        else:
            return 1

    def __right_index(self, i):
        if i != 0:
            return 2*i
        else:
            return 2

    def __parent_index(self, i):
        return i//2 - 1

    def __left(self, i):
        left_index = self.__left_index(i)
        return self.heap[left_index]

    def __right(self, i):
        right_index = self.__right_index(i)
        return self.heap[right_index]

    def __parent(self, i):
        parent_index = self.__parent_index(i)
        return self.heap[parent_index]

    def __swap(self, first_index, second_index):
        temp = self.heap[first_index]
        self.heap[first_index] = self.heap[second_index]
        self.heap[second_index] = temp

    def __heapify(self, i):
        left_index = self.__left_index(i)
        right_index = self.__right_index(i)

        index_of_highest_element = i

        if left_index < self.heap_size and self.heap[i] < self.heap[left_index]:
            index_of_highest_element = left_index

        if right_index < self.heap_size and self.heap[index_of_highest_element] < self.heap[right_index]:
            index_of_highest_element = right_index
        
        if index_of_highest_element is not i:
            self.__swap(i, index_of_highest_element)
            self.__heapify(index_of_highest_element)

    def __build_max_heap(self):
        capacity = self.capacity()

        for i in range(capacity//2, -1, -1):
            self.__heapify(i)

    def push(self, value):
        self.heap.append(value)
        self.heap_size += 1
        parent_index = self.__parent_index(self.heap_size)
        self.__build_max_heap()

    def pop(self):
        if self.heap_size >= 1:
            top = self.heap[0]
            self.heap[0] = self.heap[self.heap_size - 1]
        
            self.heap_size -= 1
            if self.heap_size > 0:
                self.__build_max_heap()
            return top

    def height(self):
        return int(math.log(self.heap_size, 2)) + 1

    def capacity(self):
        return 2 ** self.height() - 1


def heap_sort(list):
    heap = Heap(list)
    size = len(list)

    for i in range(size-1, -1, -1):
        max = heap.pop()
        list[i] = max
    
    return list


my_list = [20, 90, 40, 10, 30, 80, 70, 50, 60, 120, 110, 100]
sorded_list = heap_sort(my_list)
print(sorded_list)
