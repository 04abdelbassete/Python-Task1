class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():

    def __init__(self):
        self.head = None

    def add_at_begining(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def add_at_position(self, data, position):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        current = self.head
        forward = self.head
        for n in range(0, position):
            forward = forward.next
        for n in range(0, position-1):
            current = current.next
        current.next = new_node
        new_node.next = forward


    def delete_at_position(self, position):
        if self.head == None:
            print('This list is empty')
            return
        current = self.head
        if position == 0:
            self.head = current.next
        else:
            i = 0
            for n in range(0, position):
                if current.next != None:
                    previous = current
                    current = current.next
                else:
                    print('position is out of bounds')
                    return
            previous.next = current.next

    def display(self):
        linked_list = []
        current = self.head
        while True:
            linked_list.append(current.data)
            current = current.next
            if current.next == None:
                linked_list.append(current.data)
                break
        print(linked_list)
    
    def reverse(self):
        prev = None
        nxt = None
        while self.head != None:
            nxt = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = nxt
        self.head = prev

new_list = LinkedList()
new_list.add_at_begining('first')
new_list.add_at_end('second')
new_list.add_at_end('third')
new_list.add_at_end('forth')
new_list.add_at_begining('zeroth')
new_list.add_at_position('position',2)
new_list.delete_at_position(2)
new_list.reverse()
new_list.display()
