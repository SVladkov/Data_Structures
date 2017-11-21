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

    # heap indexes range from 1 to heap_size. If we want to convert a heap index
    # to list index, we should subtract 1 from the heap index
    def __left_index(self, i):
        return 2*i

    def __right_index(self, i):
        return 2*i + 1

    def __parent_index(self, i):
        return i//2

    def __left(self, i):
        left_index = self.__left_index(i)
        return self.heap[left_index-1]

    def __right(self, i):
        right_index = self.__right_index(i)
        return self.heap[right_index-1]

    def __parent(self, i):
        parent_index = self.__parent_index(i)
        return self.heap[parent_index-1]

    def __swap(self, first_index, second_index):
        temp = self.heap[first_index-1]
        self.heap[first_index-1] = self.heap[second_index-1]
        self.heap[second_index-1] = temp

    def __heapify(self, i):
        left_index = self.__left_index(i)
        right_index = self.__right_index(i)

        index_of_highest_element = i


        if left_index <= self.heap_size and self.heap[i-1] < self.heap[left_index-1]:
            index_of_highest_element = left_index

        if right_index <= self.heap_size and self.heap[index_of_highest_element-1] < self.heap[right_index-1]:
            index_of_highest_element = right_index
        
        if index_of_highest_element is not i:
            self.__swap(i, index_of_highest_element)
            self.__heapify(index_of_highest_element)

    def __build_max_heap(self):
        capacity = self.capacity()

        for i in range(capacity//2, 0, -1):
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
        else:
            return "opa"

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
    
    print(list)


heap_sort([20, 90, 40, 10, 30, 80, 70, 50, 60, 120, 110, 100])
