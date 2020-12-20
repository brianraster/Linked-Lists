class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''
        if not isinstance(x, Node):
            x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        toPrint = ''
        curr = self.head
        while curr is not None:
            toPrint += str(curr.data) + '->'
            curr = curr.next
        if toPrint:
            return '[' + toPrint[:-2] + ']'
        return '[]'

    def add_to_start(self, x):
        '''add x to the left of the list making it the head'''
        if not isinstance(x, Node):
            x = Node(x)
        x.next = self.head
        self.head = x

    def search_val(self, x):
        '''return indices where x was found'''
        count = 0
        curr = self.head
        while curr != None:
            if curr.data == x:
                return count
            curr = curr.next
            count += 1
        return 'Node not found'

    def remove_val_by_index(self, x):
        '''remove and return value at index x provided as parameter'''
        pass

    def length(self):
        '''return the length of the list, rep'd by number of nodes'''
        pass

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        if self.head == None:
            return
        elif current.next == None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            self.reverse_list_recur(next, current)

myList = LinkedList()

myList.append_val(1)
myList.append_val(2)
myList.append_val(3)
myList.append_val(4)
myList.append_val(5)

print(myList)

myList.reverse_list_recur(myList.head, None)

print(myList)
