class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for n in nodes:
                node.next = Node(data=n)
                node = node.next

    def append(self, data):
        node = self.head
        # Get to the end of the list
        while node is not None:
            node = node.next
        # Create new node; point end of list to new node
        new_node = Node(data=data)
        node.next = new_node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        values = " -> ".join(str(n) for n in nodes)
        return values


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

    def __str__(self):
        return str(self.data)
