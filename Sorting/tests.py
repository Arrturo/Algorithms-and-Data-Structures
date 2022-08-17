import sort

sort_ = sort.Sort()
list_ = [2, 4, 3, 8, 0, 5]

assert sort_.bubbleSort(list_) == [0, 2, 3, 4, 5, 8]
assert sort_.insertionSort(list_) == [0, 2, 3, 4, 5, 8]
assert sort_.selectionSort(list_) == [0, 2, 3, 4, 5, 8]
