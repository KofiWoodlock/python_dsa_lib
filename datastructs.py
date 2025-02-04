# Common & custom data structures interface & implementation (C) KFW 2025 


# static array - A structure consisting of elements of the same type, identified by an index, 
#              stored contiguosly in memory. It's size is not changeable 
class Array:
    def __init__(self, size: int, type: any) -> None:
        self.arr = [None] * size
        self.type = type
        self.size = size
        self.length = 0

    def append(self, val) -> None:
        if type(val) != self.type:
            raise TypeError("Value must be of same type declared when initialising array.")
        
        if self.isFull():
            raise Exception("Cannot append to full array")
        
        self.arr[self.length] = val
        self.length += 1
        
        
    def insertAt(self, index: int, val) -> None:
        if type(val) != self.type:
            raise TypeError("Value must be of same type declared when initialising array.")

        self.arr[index] = val

    def removeAt(self, index: int) -> None:
        if self.isEmpty():
            raise Exception("Cannot remove from empty array")
        
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
    
        self.arr[index] = None
        self.__shiftLeft(index)
        self.length -=1
                
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from empty array")
        
        val = self.arr[self.length-1]
        self.arr[self.length-1] = None
        self.length -= 1
        return val


    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size
    
    def length(self) -> int:
        return self.length
    
    def size(self) -> int:
        return self.size

    def print(self) -> None:
        print(self.arr[:self.length])

    def __shiftLeft(self, i: int):
        for index in range(i+1, self.size):
            self.arr[index-1] = self.arr[index]


# dynamic array - A structure consisting of elements of the same type, identified by an index, 
#              stored contiguosly in memory. It's size is changeable during runtime
class DynamicArray:
    def __init__(self, type: any) -> None:
        self.type = type
        self.size = 2
        self.length = 0
        self.arr = [None] * self.size


    def append(self, val) -> None:
        if type(val) != self.type:
            raise TypeError("Value must be of same type declared when initialising array.")
        
        if self.length == self.size:
            self.__resize()
        
        self.arr[self.length] = val
        self.length += 1

    def pop(self):
        value = self.arr[self.length-1]
        self.arr[self.length-1] = None
        self.length -= 1
        return value 
    
    def get(self, index: int) -> any:
        if self.isEmpty():
            raise IndexError("Cannot use get on empty array")
        
        return self.arr[index]
    
    def print(self) -> None:
        print(self.arr[:self.length])


    def isEmpty(self) -> bool:
        return self.length == 0

    
    def __resize(self) -> None:
        self.size *= 2
        new_arr = [None] * self.size

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        
# stack - A structure consiting of elements that can be of different types. 
#         Operates in the last-in-first-out (LIFO) principle.            
class Stack:
    def __init__(self):
        self.stack = [] 

    def push(self, val: any) -> None:
        self.stack.append(val)

    def pop(self) -> any:
        self.stack.pop()

    def peek(self) -> None:
        print(self.stack[-1])

    def print(self) -> None:
        print(self.stack)

# linked list - A structure similar to an array but the elements are not stored contiguosly in memory, in fact 
#               They are linked together via pointers to ones memory address 
class ListNode:
    def __init__(self, val: any) -> None:
            self.val = val
            self.next = None
            self.prev = None
    
class SinglyLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Inserts an element at the front (head) of the list 
    def insertHead(self, val: any) -> None:
        new_node = ListNode(val)

        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    # Inserts an element at the end (tail) of the list 
    def insertTail(self, val: any) -> None:
        new_node = ListNode(val)

        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = self.tail.next

    # Removes first (head) element from the list
    def removeHead(self) -> None:
        if self.__isEmpty():
            raise Exception("Cannot remove from empty list")
        
        self.head = self.head.next

    # Removes element at an arbitrary index 
    def removeAt(self, index: int) -> None:
        i = 0 
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

    # Checks to see if some element is in the linked list & returns position
    def find(self, target: any) -> int:
        index = 0
        curr = self.head
        while curr:
            if curr.val == target:
                return index
            else:
                curr = curr.next
                index += 1
        return -1

    def print(self) -> None:
        curr = self.head
        while curr != None:
            print(f"{curr.val}->",end="")
            curr = curr.next
        print()

    def __isEmpty(self) -> bool:
        return not self.head

# doubly linked list - A structure similar to a singly linked list but each element within the list is connected to the previous
#                      and next node via pointers 
class DoublyLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    # Inserts an element at the head (front) of the linked list 
    def insertHead(self, val: any) -> None:
        new_node = ListNode(val)
        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
        else:            
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1 

    # Inserts an element at the tail (end) of the linked list
    def insertTail(self, val: any) -> None:
        new_node = ListNode(val)
        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # Inserts an element at a given index 
    def insertAt(self, val: any, index: int) -> None:
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.insertHead(val)
            return
        elif index == self.length:
            self.insertTail(val)
            return

        new_node = ListNode(val)
        curr = self.head
        i = 0
        while i < index -1:
            curr = curr.next
            i += 1
        
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        self.length += 1
        
    # Removes the element at the head (front) of the linked list
    def removeHead(self) -> None:
        if self.__isEmpty():
            raise Exception("Cannot remove from empty list")
        
        self.head.next.prev.val = None
        self.head = self.head.next

    # Removes the element at the tail (end) of the linked list
    def removeTail(self) -> None:
        pass

    # Removes the element at a given index 
    def removeAt(self) -> None:
        pass

    # Removes all elements from the linked list
    def clear(self) -> None:
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = None
            curr.prev = None
            curr = next_node
        
        self.head = None
        self.tail = None
        self.length = 0
    
    # Checks to see if some element is in the linked list & returns position
    def find(self, target: any) -> int:
        index = 0
        curr = self.head
        while curr:
            if curr.val == target:
                return index
            else:
                curr = curr.next
                index += 1
        return -1

    def print(self) -> None:
        curr = self.head
        while curr != None:
            print(f"{curr.val}<->",end="")
            curr = curr.next
        print()

    def __isEmpty(self) -> bool:
        return not self.head

# Queue - A structure consiting of elements that can be of different types. 
#         Operates in the first-in-first-out (FIFO) meaning the first element added will be the first element removed
class Queue:
    def __init__(self) -> None:
        self.first = self.last = None
        self.length = 0

    # Adds an item to the front of the queue 
    def enqueue(self, val: any) -> None:
        new_node = ListNode(val)
        
        if self.__isEmpty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next
        self.length += 1

    # Removes the first item from the queue 
    def dequeue(self) -> any:
        if self.__isEmpty():
            raise Exception("Cannot dequeue from empty queue")
        
        if self.length == 1:
            val = self.first.val
            self.first = self.last = None
            self.length -= 1
            return val
        
        val = self.first.val
        self.first = self.first.next
        self.length -= 1
        return val
    
    # Prints the first item in the queue
    def front(self) -> None:
        print(self.first.val)


    # Prints the last item in the queue
    def end(self) -> None:
        print(self.last.val) 

    # Prints the entire queue 
    def print(self) -> None:
        curr = self.first
        while curr != None:
            print(f"{curr.val}->",end="")
            curr = curr.next
        print()

    def __isEmpty(self) -> int:
        return self.length == 0
    
class Deque:
    def __init__(self) -> None:
        self.front = None
        self.back = None
        self.length = 0
    
    def append(self, val: any) -> None:
        new_node = ListNode(val)
        if self.__isEmpty():
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            new_node.prev = self.back
            self.back = new_node
        self.length += 1

    def appendLeft(self, val: any) -> None:
        new_node = ListNode(val)
        if self.__isEmpty():
            self.front = new_node
            self.back = new_node
        else:            
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.length +=1

    def pop(self) -> any:
        pass

    def popLeft(self) -> any:
        if self.__isEmpty():
            raise Exception("Cannot remove from empty list")
        
        val = self.front.val
        self.front = self.front.next
        return val

    def print(self) -> None:
        curr = self.front
        while curr != None:
            print(f"{curr.val}<->",end="")
            curr = curr.next
        print()

    def __isEmpty(self) -> bool:
        return not self.front

class CircularQueue:
    pass

class PriorityQueue:
    pass

# Helper class for BinaryTree & Binary Search Tree classes 
class TreeNode:
    def __init__(self, val: any) -> None:
        self.val = val
        self.left = None
        self.right = None

# Binary tree - A subset of graphs in which data is arranged in a tree-like structure
#               consiting of a root node, branch nodes and leaf nodes. Each node can have
#               a maximum of two child nodes. 
class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    # Adds a new node to the tree in the next non-complete layer from left to right  
    def insert(self, val: any) -> None:
        if self.__isEmpty():
            self.root = TreeNode(val)   
            return 

        q = Deque()
        q.append(self.root)

        while q:
            curr = q.popLeft()
            if curr.left:
                q.append(curr.left)
            else:
                curr.left = TreeNode(val)
                return
            
            if curr.right:
                q.append(curr.right)
            else:
                curr.right = TreeNode(val)
                return 


    def remove(self) -> None:
        pass

    def search(self):
        pass
    
    
    def print(self) -> None:
        if self.__isEmpty():
            print("Tree is empty")
            return 
        
        height = self.__getHeight(self.root)
        max_width = 2**height
        level_nodes = [(self.root, max_width // 2)]

        for level in range(height):
            new_level_nodes = []
            line = [" "] * max_width

            for node, pos in level_nodes:
                if node:
                    line[pos] = str(node.val)
                    new_level_nodes.append((node.left, pos-2**(height-level-2)))
                    new_level_nodes.append((node.right, pos+2**(height-level-2)))
            print("".join(line).rstrip())

            if level < height-1:
                slash_line = [" "] * max_width
                for node, pos in level_nodes:
                    if node and node.left:
                        slash_line[pos-1] = "/"
                    if node and node.right:
                        slash_line[pos+1] = "\\"
                print("".join(slash_line).rstrip())
            
            level_nodes = new_level_nodes

    # Helper function to calculate height of binary tree
    def __getHeight(self, node) -> int:
        if not node:
            return 0
        return 1 + max(self.__getHeight(node.left), self.__getHeight(node.right))

    def __isEmpty(self):
        return not self.root


class BST:
    def __init__(self):
        self.root = None

class Vector:
    pass


