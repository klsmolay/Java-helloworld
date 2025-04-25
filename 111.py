class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def iterate_item(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            print(val)
            current_item = current_item.next
    
    def append_item(self, data):
        new_node = Node(data)  
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node  
        else:
            self.head = new_node
            self.tail = new_node  
        self.count += 1

items = Singly_Linked_List()
items.append_item("PHP")
items.append_item("#")
items.append_item("C++")
items.append_item("Python")
print("List items:")
items.iterate_item()
print("\nHead data:", items.head.data)
print("Tail data:", items.tail.data)
