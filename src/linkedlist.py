class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def inBegin(self, data):
        nnode = Node(data)
        nnode.next = self.head
        self.head = nnode

    def inIndex(self, data, index):
        if index == 0:
            self.inBegin(data)
            return

        position = 0
        cnode = self.head 
        while cnode is not None and position + 1 != index:
            position += 1
            cnode = cnode.next

        if cnode is not None:
            nnode = Node(data)
            nnode.next = cnode.next
            cnode.next = nnode
        else:
            print("Index not present")
            
    def inEnd(self, data):
        nnode = Node(data)
        if self.head is None: 
            self.head = nnode
            return

        cnode = self.head
        while cnode.next:
            cnode = cnode.next
        
        cnode.next = nnode
    
    def udNode(self, val, index):
        cnode = self.head
        position = 0
        while cnode is not None and position != index:
            position += 1
            cnode = cnode.next
        
        if  cnode is not None:
            cnode.data = val
        else:
            print("Index not present")

    def rvFirstNode(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    def rvLastNode(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        cnode = self.head
        while cnode.next and cnode.next.next:
            cnode = cnode.next

        cnode.next = None
    
    def rvIndex(self, index):
        if self.head is None:
            return

        if index == 0:
            self.rvFirstNode()
            return
        
        cnode = self.head
        position = 0
        while cnode is not None and cnode.next is not None and position + 1 != index:
            position += 1
            cnode = cnode.next

        if cnode is not None and cnode.next is not None:
            cnode.next = cnode.next.next
        else:
            print("Index not present")

    def rvNode(self, data):
        cnode = self.head

        if cnode is not None and cnode.data == data:
            self.rvFirstNode()
            return

        while cnode is not None and cnode.next is not None:
            if cnode.next.data == data:
                cnode.next = cnode.next.next
                return
            cnode = cnode.next
        print("Node with the given data not found")

    def llsize(self):
        size = 0
        cnode = self.head
        while cnode:
            size += 1
            cnode = cnode.next
        return size

    def llprint(self):
        cnode = self.head
        while cnode:
            print(cnode.data)
            cnode = cnode.next

llist = LinkedList()

llist.inEnd('a')
llist.inEnd('b')
llist.inBegin('c')
llist.inEnd('d')
llist.inIndex('g', 2)

print("Node Data: ")
llist.llprint()

print("\nRemove First Node:")
llist.rvFirstNode()
llist.llprint()

print("\nRemove Last Node:")
llist.rvLastNode()
llist.llprint()

print("\nRemove Node at Index 1:")
llist.rvIndex(1)
llist.llprint()

print("\nLinked list after removing a node:")
llist.llprint()

print("\nUpdate node value at Index 0:")
llist.udNode('z', 0)
llist.llprint()

print("\nSize of linked list:", llist.llsize())