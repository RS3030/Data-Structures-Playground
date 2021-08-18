# for any types of linked lists, you need a node class
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# each node has the pointer to the next node only (one-way traversing)
# WITHOUT TAIL POINTER version
class SinglyLinkedList():
    def __init__(self):
        self.head = None

    # returns true if empty
    def is_empty(self):
        return self.head == None

    # returns number of data elements in list  : Big O(n) time because you are traversing whole list
    def get_size(self):
        if self.head == None:
            return 0
        count = 1
        node = self.head
        while node.next != None:
            node = node.next
            count += 1
        return 'Number of data: ' + str(count)

    # returns the value of the nth item  : Bog O(n) time in the worst case
    def data_at(self, index):
        if index < 0:
            return IndexError('Invalid index')
        count = 0
        node = self.head
        while node != None:
            if index == count:
                return 'index[' + str(index) + ']: ' + str(node.data)
            elif node.next != None:
                node = node.next
                count += 1
            else:
                return IndexError('Out of length')

    # adds an item to the front of the list  : Big O(1) time
    def push_front(self, data):
        node = Node(data, self.head)
        # move the head pointer to the new_node
        self.head = node
        self.print_list()

    # removes the last item  : Big O(n) time where n is the length of the list
    def push_back(self):
        # if it's empty
        if self.head == None:
            return 'No data'
        node = self.head
        # if there's only one item
        if node.next == None:
            self.head = None
            return
        # more than 2 items
        while node.next.next != None:
            node = node.next
        node.next = None
        self.print_list()

    # removes end item and returns its value  : Big O(n) time where n is the length of the list
    def pop_back(self):
        # if it's empty
        if self.head == None:
            return 'No data'
        node = self.head
        # if there's only one item
        if node.next == None:
            self.head = None
            return node.data
        # more than 2 items
        while node.next.next != None:
            node = node.next
        # store the data to pop, then remove the link, and then return
        temp_node = node.next.data
        node.next = None
        self.print_list()
        return temp_node

    def print_list(self):
        if self.head == None:
            print('Empty')
            return
        node = self.head
        list_to_output = ''
        while node != None:
            list_to_output += (str(node.data) + ' => ')
            node = node.next

        print(list_to_output)


# -------test---------
# new_list = SinglyLinkedList()
# new_list.push_front(4)
# new_list.push_front(6)
# print(new_list.get_size())
# new_list.push_front(8)
# print(new_list.data_at(1))


# TODO implement following:
#
#  insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
#  erase(index) - removes node at given index
#  value_n_from_end(n) - returns the value of the node at nth position from the end of the list
#  reverse() - reverses the list
#  remove_value(value) - removes the first item in the list with this value
