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
        pass

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

myList = LinkedList()

myList.append_val(node1)
myList.append_val(node2)
myList.append_val(node3)
myList.append_val(node4)
myList.append_val(5)
myList.add_to_start(node6)

print(myList)

print(myList.search_val(5))
