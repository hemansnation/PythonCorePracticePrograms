# Defining the class which will create nodes for our linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Defining the class which will create our linked list and also defining utility methods
class LinkedList:
    def __init__(self):
        self.root = None

# Defining method which checks whether the linked list or stack is empty or not
    def isEmpty(self):
        return True if self.root is None else False

# Defining method to push data in stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
        print (str(data) + " successfully pushed to stack")

# Defining method to pop data in stack
    def pop(self):
        if self.isEmpty():
            print ("Stack is empty, 'Underflow'")
            return
        popped = self.root.data
        self.root = self.root.next
        print ("The popped value is: " + str(popped))


# The main logic starts from here
if __name__ == '__main__':

    stack = LinkedList()        # Creating our stack in form of linked list

    stack.push(10)              # Pushing values in stack
    stack.push(20)
    stack.push(30)

    stack.pop()                 # Poping values from stack
    stack.pop()
    stack.pop()
    stack.pop()
