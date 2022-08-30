import linked_list
import LIFO_Stack
import FIFO_Queue

#LINKED LIST
def testLinkedlist():
    list_ = linked_list.LinkedList()

    #ASSERT 1
    assert list_.head == None

    #ASSERT 2
    list_.push(1)
    list_.push(0)

    assert str(list_) == '0 -> 1'

    #ASSERT 3
    list_.append(9)
    list_.append(10)

    assert str(list_) == '0 -> 1 -> 9 -> 10'

    #ASSERT 4
    middle_node = list_.node(at=1)
    list_.insert(5, after=middle_node)

    assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

    #ASSERT 5
    first_element = list_.node(at=0)
    returned_first_element = list_.pop()

    assert first_element.value == returned_first_element
    assert str(list_) == '1 -> 5 -> 9 -> 10'

    #ASSERT 6
    last_element = list_.node(at=3)
    returned_last_element = list_.remove_last()

    assert last_element.value == returned_last_element
    assert str(list_) == '1 -> 5 -> 9'

    #ASSERT 7
    second_node = list_.node(at=1)
    list_.remove(second_node)

    assert str(list_) == '1 -> 5'

    #ASSERT 8
    assert len(list_) == 2

    list_.show()


#LIFO
def testLIFO():
    stack = LIFO_Stack.Stack()

    #ASSERT 1
    assert len(stack) == 0
    stack.push(3)
    stack.push(10)
    stack.push(1)

    #ASSERT 2
    assert len(stack) == 3

    top_value = stack.pop()

    #ASSERT 3
    assert top_value == 1
    assert len(stack) == 2

    print(str(stack))

#FIFO
def testFIFO():
    queue = FIFO_Queue.Queue()

    #ASSERT 1
    assert len(queue) == 0

    #ASSERT 2
    queue.enqueue('client1')
    queue.enqueue('client2')
    queue.enqueue('client3')

    assert str(queue) == 'client1, client2, client3'

    #ASSERT 3
    client_first = queue.dequeue()

    assert client_first == 'client1'
    assert str(queue) == 'client2, client3'
    assert len(queue) == 2

    assert queue.is_empty() == False
