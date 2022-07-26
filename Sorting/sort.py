from typing import List

class Sort:

    def bubbleSort(self, l: List) -> List:
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] < l[j]:
                    temp = l[j]
                    l[j] = l[i]
                    l[i] = temp
        return l

    def selectionSort(self, l: List):
        for i in range(len(l)):
            min_index = i
            for j in range(i + 1, len(l) - 1):
                if l[j] < l[min_index]:
                    min_index = j
            temp = l[i]
            l[i] = l[min_index]
            l[min_index] = temp
        return l

    def insertionSort(self, l: List):
        n = len(l)
        for i in range(1, n - 1):
            key = l[i]
            j = i - 1
            while j >= 0 and l[j] > key:
                l[j + 1] = l[j]
                j = j - 1
                l[j + 1] = key
        return l

sort_ = Sort()
list_ = [2, 4, 3, 8, 0, 5]

assert sort_.bubbleSort(list_) == [0, 2, 3, 4, 5, 8]
assert sort_.insertionSort(list_) == [0, 2, 3, 4, 5, 8]
assert sort_.selectionSort(list_) == [0, 2, 3, 4, 5, 8]
