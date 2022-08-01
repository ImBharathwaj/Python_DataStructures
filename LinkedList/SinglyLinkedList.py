class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        # Initiating new node
        new_node = Node(new_data)

        # adding to the list
        new_node.next = self.head

        # Setting new_node as first node
        self.head = new_node 

    def insertAfter(self, prev_node, new_data):
        # Check if the given prev_node exists
        if prev_node is None:
            print('The given previous node must be in the LinkedList!')
            return
        
        # Create new node & put into data
        new_node = Node(new_data)

        # Make next of new node as next of prev_node
        new_node.next = prev_node.next

        # Make next of previous node as new_node
        prev_node.next = new_node

    def append(self, new_data):
        # Initiating new_node with new_data
        new_node = Node(new_data)

        # If the linked list is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return
        
        # Else traverse till the last node
        # The last node in the element will be traversed
        last = self.head
        while last.next:
            last = last.next
        
        # Change the next of last node
        last.next = new_node


    def delete(self, key):
        # Store node head
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
            
        # Search for the key t be deleted, keep track of the prev_node
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key was not present in linked list
        if(temp == None):
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
        
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            

if __name__ == '__main__':
    ll = LinkedList()
    
    ll.head = Node('First')
    second = Node('2nd')
    third = Node('3rd')
    fourth = Node('4th')

    ll.head.next = second
    second.next = third
    third.next = fourth

    ll.push('5th')
    ll.append(8)

    print('-'*30)
    ll.printList()
