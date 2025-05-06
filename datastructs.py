# Common & custom data structures, interface & implementation (C) KFW 2025 

# Static array - A structure consisting of elements of the same type, identifiable by an index, 
#              stored contiguosly in memory. It's size is not changeable 
class Array:
    """
    A structure to store a fixed number of homogenous types contiguosly in memory 
    
    ... 

    Attributes:
    ----------
    arr: list
        The actual array that stores the values 
    type:
        The specified data type that the array will store 
    size: 
        The maximum capacity of the array
    length:
        The number of elements the array currently contains
    
    Methods:
    -------
    append(val)
        Adds an element to the end of the array
    delete(val)
        Removes first occurence of specified value
    insertAt(index, val)
    """
    def __init__(self, size: int, type: type) -> None:
        self.arr: list = [None] * size
        self.type = type
        self.size: int = size
        self.length: int = 0

    def append(self, val) -> None:
        """ 
        Appends an element to the end of the array
        """

        self.__checkType(val)
        if self.__isFull():
            raise Exception("Cannot append to full array.")
        
        self.arr[self.length] = val
        self.length += 1

    def delete(self, val) -> None:
        """
        Deletes the first occurence of a specified value in the array
        """

        found = False
        for i in range(self.length):
            if found:
                self.arr[i-1] = self.arr[i]
            elif self.arr[i] == val:
                found = True
        
        if found:
            self.length -= 1
        
    def insertAt(self, index: int, val) -> None:
        """
        Inserts and overwrites an elements at a given index within the array 
        """

        self.__checkType(val)
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")

        self.arr[index] = val

    def removeAt(self, index: int) -> None:
        """
        Removes an element at a given index from the array 
        """

        if self.__isEmpty():
            raise Exception("Cannot remove from empty array.")
        if index < 0 or index > self.length:
            raise IndexError("Index out of range.")
    
        self.__shiftLeft(index)
        self.length -=1
                
    def pop(self):
        """
        Removes and returns the last element in the array 
        """

        if self.__isEmpty():
            raise Exception("Cannot pop from empty array.")
        
        val = self.arr[self.length-1]
        self.arr[self.length-1] = None
        self.length -= 1
        return val
    
    def reverse(self) -> None:
        """ 
        Reverses the contents of the array 
        """

        if self.__isEmpty():
            raise Exception("Cannot reverse empty array.")
        self.arr[:self.length] = self.arr[:self.length][::-1]

    def sort(self, desc: bool = False):
        """
        Sorts the contents of the array defaults to ascending order
        """
        pass

    def get(self, index: int):
        """
        Returns the element at a given index
        """

        return self.arr[index]

    def find(self, val) -> int:
        """
        Returns the index of a given value otherwise returns -1
        """

        for i in range(self.length):
            if self.arr[i] == val:
                return i
        return -1 

    def print(self) -> None:
        """
        Prints contents of the array
        """

        print(self.arr[:self.length])

    def __isEmpty(self) -> bool:
        return self.length == 0

    def __isFull(self) -> bool:
        return self.length == self.size

    def __shiftLeft(self, i: int):
        for index in range(i+1, self.size):
            self.arr[index-1] = self.arr[index]
        
    def __checkType(self, val) -> None:
        if type(val) != self.type:
            raise TypeError(f"Values must be of type {self.type}")

# Dynamic array - A structure consisting of elements of the same type, identifiable by an index, 
#              stored contiguosly in memory. It's size is changeable during runtime
class DynamicArray:
    def __init__(self, type: type) -> None:
        self.type = type
        self.size = 2
        self.length = 0
        self.arr = [None] * self.size

    # Appends an element to the end of the array
    def append(self, val) -> None:
        if type(val) != self.type:
            raise TypeError("Value must be of same type declared when initialising array.")
        
        if self.length == self.size:
            self.__resize()
        
        self.arr[self.length] = val
        self.length += 1

    # Removes & returns the last element in the array
    def pop(self) -> any:
        if self.__isEmpty():
            raise Exception("Cannot pop from empty array.")
        
        value = self.arr[self.length-1]
        self.arr[self.length-1] = None
        self.length -= 1
        return value 
    
    # Inserts & overwrites an element at a given index within the array
    def insertAt(self, val: type, index: int) -> None:
        self.__checkType(val)
        if self.__isEmpty() and index > 0:
            raise Exception("Index specified does not exist as array is empty.")
        if index < 0 or index > self.length-1:
            raise IndexError("Index out of bounds.")

        self.arr[index] = val

    # Removes an element at a given index from the array
    def removeAt(self, val: type, index: int) -> None:
        self.__checkType(val)
        if self.__isEmpty():
            raise Exception("Cannot remove from empty array.")
        if index < 0 or index > self.length-1:
            raise IndexError("Index out of bounds.")

        self.arr[index] = None
        self.length -= 1

    # Reverses the list
    def reverse(self) -> None:
        if self.__isEmpty():
            raise Exception("Cannot reverse empty array.")
        self.arr[:self.length] = self.arr[self.length-1::-1]
    
    # Sorts the list in ascending order by default if descending parameter not supplied 
    def sort(self, descending: bool=False) -> None:     
        self.__sort(self.arr, 0, self.length)
        
        if descending:
            self.arr.reverse()

    def __sort(self, arr, l, r) -> list:
        if l < r:
            m = (l+r) // 2
            self.__sort(arr, l, m)
            self.__sort(arr, m+1, r)
            self.__merge(arr, l, m, r)
    
    def __merge(self, arr, left, mid, right) -> list:
        lsubarr = arr[left: mid+1]
        rsubarr = arr[mid+1: right+1]

        i = 0
        j = 0
        k = left
        while i<len(lsubarr) and j < len(rsubarr):
            if lsubarr[i] <= rsubarr[j]:
                arr[k] = lsubarr[i]
                i += 1
            else:
                arr[k] = rsubarr[j]
                j += 1
            k += 1
        
        while i < len(lsubarr):
            arr[k] = lsubarr[i]
            i += 1
            k += 1
        while j < len(rsubarr):
            arr[k]= rsubarr[j]
            j += 1
            k += 1

    # Returns an element at a given index 
    def get(self, index: int) -> any:
        if self.__isEmpty():
            raise IndexError("Cannot use get on empty array.")
        
        return self.arr[index]
    
    # reutrns index of first occurence of an element 
    def index(self, val: any) -> int:
        for i in range(self.length):
            if self.arr[i] == val:
                return i
        raise ValueError(f"{val} does not exist in the array.")

    # Clears contents of array
    def clear(self) -> None:
        if self.__isEmpty():
            raise Exception("Cannot clear empty array.")
        
        for i in range(self.length):
            self.arr[i] = None
        self.length = 0

    # Returns the number of occurences of a value
    def count(self, val: any) -> int:
        occurences = 0
        for i in range(self.length):
            if self.arr[i] == val:
                occurences += 1
        return occurences
    
    def concatenate(self, array: list) -> None:
        for e in array:
            self.append(e)
    
    def print(self) -> None:
        print(self.arr[:self.length])

    def __isEmpty(self) -> bool:
        return self.length == 0

    def __resize(self) -> None:
        self.size *= 2
        new_arr = [None] * self.size

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def __checkType(self, val) -> None:
        if type(val) != self.type:
            raise TypeError(f"Values must be of type {self.type}")

# Stack - A structure consiting of elements that can be of different types. 
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

# Linked list - A structure similar to an array but the elements are not stored contiguosly in memory, in fact 
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

    # Inserts an element at the front (head) of the linked list 
    def insertHead(self, val: any) -> None:
        new_node = ListNode(val)

        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    # Inserts an element at the end (tail) of the linked list 
    def insertTail(self, val: any) -> None:
        new_node = ListNode(val)

        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = self.tail.next

    # Removes first (head) element from the linked list
    def removeHead(self) -> None:
        if self.__isEmpty():
            raise Exception("Cannot remove from empty linked list")
        
        self.head = self.head.next

    # Removes element at a specified index 
    def removeAt(self, index: int) -> None:
        i = 0 
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

    # Reverses contents linked list 
    def reverse(self) -> None:
        if self.__isEmpty():
            raise Exception("Cannot reverse empty linked list.")
        
        curr = self.head
        prev = None
        while curr:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


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

# Doubly linked list - A structure similar to a singly linked list but each element within the list is connected to the previous
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
#         Operates in the first-in-first-out (FIFO) principle meaning the first element added will be the first element removed
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
    
    # Returns the first item in the queue
    def getfront(self) -> any:
        return self.first.val

    # Returns the last item in the queue 
    def getRear(self) -> any:
        return self.last.val

    # Prints the entire queue 
    def print(self) -> None:
        curr = self.first
        while curr != None:
            print(f"{curr.val}->",end="")
            curr = curr.next
        print()

    def __isEmpty(self) -> int:
        return self.length == 0

# Deque - Short for double ended queue it is a structure consiting of elements that cane be of different types.
#         It is similar to a queue in the fact it operates in the first-in-first-out (FIFO) principle but differs to a queue
#         as both ends can act as the first element in the queue i.e elements can be added and removed from the front and back    
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
        if self.__isEmpty():
            raise Exception("Cannot pop from empty Deque")

        val = self.back.val
        self.back.prev.next = None
        self.back = self.back.prev
        return val

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

# Circular queue - similar to a regular queue except the last element in the queue is connected to
#                  the first element, forming a circle. A circualr queue still operates in the first-in-first-out (FIFO)
#                  principle. The queue is of fixed size
class CircularQueue:
    def __init__(self, size: int, type: any ):
        self.size = size
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1

    # Adds an item to the front of the queue 
    def enqueue(self, val: any) -> None:
        if self.__isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear+1) % self.size
        
        self.queue[self.rear] = val

    # Removes the first item from the queue 
    def dequeue(self) -> any:
        if self.__isEmpty():
            raise Exception("Cannot dequeue from empty queue.")
        
        val = self.queue[self.front]
        self.queue[self.front] = None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1) % self.size
        
        return val
    
    # Returns the first item in the queue
    def getfront(self) -> any:
        if self.__isEmpty():
            raise Exception("Queue is empty")
        return self.queue[self.front]

    # Returns the last item in the queue 
    def getRear(self) -> any:
        if self.__isEmpty():
            raise Exception("Queue is empty")
        return self.queue[self.rear]

    def print(self):
        if self.__isEmpty():
            print("Queue is empty")
            return 

        res = []
        i = self.front
        while True:
            res.append(self.queue[i])
            if i == self.rear:
                break
            i = (i+1) % self.size
        print(res)

    def __isEmpty(self) -> bool:
        return self.front == -1
    
    def __isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front

# Circular buffer - A structure consisting of elements of the same type, identifiable by an index,
#                   stored contigously in memory. It's size is not changeable & once the buffer is full
#                   the oldest data is overwrited starting from the beginning.
class CircularBuffer:
    def __init__(self, size: int, type: any) -> None:
        self.type = type
        self.size = size
        self.first = -1
        self.last = -1
        self.buffer = [None] * self.size

    # Inserts an element into the buffer 
    def insert(self, val) -> None:
        if not isinstance(val, self.type):
            raise TypeError("Value data type does not match specified data type.")

        if self.__isFull():
            self.first = (self.first + 1) % self.size

        if self.__isEmpty():
            self.first = 0

        self.last = (self.last + 1) % self.size
        self.buffer[self.last] = val     

    # Removes the first element added to the buffer
    def remove(self) -> any:
        if self.__isEmpty():
            raise Exception("Buffer is empty.")
        
        val = self.buffer[self.first]
        self.buffer[self.first] = None

        if self.first == self.last:
            self.first = -1
            self.last = -1
        else:
            self.first = (self.first + 1) % self.size
        
        return val

    # Returns the first element in the buffer
    def getFirst(self) -> any:
        if self.__isEmpty():
            return None
        return self.buffer[self.first]

    # Returns the last element in the buffer
    def getLast(self) -> any:
        if self.__isEmpty():
            return None
        return self.buffer[self.last]

    def print(self):
        if self.__isEmpty():
            print("Buffer is empty")
            return 
        
        result = []
        i = self.first
        while True:
            result.append(self.buffer[i])
            if i == self.last:
                break
            i = (i + 1) % self.size
        
        print(result)

    def __isFull(self) -> bool:
        return (self.last+1) % self.size == self.first

    def __isEmpty(self) -> bool:
        return self.first == -1


# Helper class for BinaryTree & Binary Search Tree classes 
class TreeNode:
    def __init__(self, val: any) -> None:
        self.val = val
        self.left = None
        self.right = None

# Binary tree - A structure in which data is arranged in a tree-like structure
#               consiting of a root node, branch nodes and leaf nodes. Each node can have
#               a maximum of two child nodes. 
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.height = self.__getHeight(self.root)
        self.__preOutput = []
        self.__inOutput = []
        self.__postOutput = []
        self.__levelOutput = []

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

    # Removes a specified element from the tree and replaces it with bottom right-most node  
    def remove(self, val: any) -> None:
        if self.__isEmpty():
            raise Exception("Cannot remove from empty tree")
        
        self.root = self.__remove(self.root, val)
    
    def __remove(self, root: TreeNode, val: any) -> TreeNode:
        if not root.left and not root.right:
            return None if root.val == val else root

        q = [root]
        curr = None
        targetNode = None
        # BFS to find deepest node & target node
        while q:
            curr = q.pop(0)
            if curr.val == val:
                targetNode = curr
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        if targetNode:
            temp = curr.val
            targetNode.val = temp
            self.__remDeepest(root, curr)

        return root 
    
    # Returns & Removes the deepest rightmost node in the binary tree 
    def pop(self) -> any:
        if self.__isEmpty():
            raise Exception("Cannot pop from empty tree")
        
        if not self.root.left and not self.root.right:
            val = self.root.val
            self.root = None
            return val
        
        q = [self.root]
        parent = None
        curr = None
        while q:
            curr = q.pop(0)
            if curr.left:
                parent = curr
                q.append(curr.left)
            if curr.right:
                parent = curr
                q.append(curr.right)
        val = curr.val
        if parent:
            if parent.right == curr:
                parent.right = None
            else:
                parent.left = None
                
        return val


    # Returns a list of nodes in pre-order (root, left, right)
    def preOrder(self) -> list:
        return self.__preOrder(self.root)

    def __preOrder(self, root: TreeNode) -> list:
        if not root:
            return

        self.__preOutput.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
        return self.__preOutput
        

    # Returns a list of nodes in-order (left, root, right)
    def inOrder(self) -> list:
        return self.__inOrder(self.root)

    def __inOrder(self, root: TreeNode) -> list:
        if not root:
            return

        self.inOrder(root.left)
        self.__inOutput.append(root.val)
        self.inOrder(root.right)
        return self.__inOutput

    # Returns a list of nodes in post-order (left, right, root)
    def postOrder(self) -> list:
        return self.__postOrder(self.root)

    def __postOrder(self, root: TreeNode) -> list:
        if not root:
            return 

        self.postOrder(root.left)
        self.postOrder(root.right)
        self.__postOutput.append(root.val)
        return self.__postOutput
    
    def levelOrder(self, root) -> list:
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
    
    # Helper function to delete deepest node in binary tree
    def __remDeepest(self, root, target) -> None:
        q = [root]
        while q:
            curr = q.pop(0)
            if curr == target:
                curr = None
                del target
                return 
            
            if curr.right:
                if curr.right == target:
                    curr.right = None
                    del target
                    return
                q.append(curr.right)
            
            if curr.left:
                if curr.left == target:
                    curr.left = None
                    del target
                    return
                q.append(curr.left)


    def __isEmpty(self) -> bool:
        return not self.root

# Binary search tree - A structure similar to a binary tree however the tree has an ordered property.
#                      Meaning nodes smaller than the root will be inserted into the left subtree 
#                      whereas nodes larger than the root will be inserted into the right subtree.
class BST:
    def __init__(self):
        self.root = None

    def insert(self, val: any) -> None:
        newNode = TreeNode(val)

        if self.__isEmpty(): 
            self.root = newNode
        
        parent = None
        curr = self.root
        while curr:
            parent = curr
            if curr.val > val:
                curr = curr.left
            elif curr.val < val:
                curr = curr.right
            else:
                return
        if parent.val > val:
            parent.left = newNode
        else:
            parent.right = newNode
        return
    
    def remove(self, val: any) -> None:
        if self.__isEmpty():
            raise Exception("Cannot remove from empty tree")
        self.root = self.__remove(self.root, val)
    
    def __remove(self, root: TreeNode, val: any) -> TreeNode:
        if not root:
            raise Exception("Element not found in tree")

        if val < root.val:
            root.left = self.__remove(root.left, val)
            return root
        elif val > root.val:
            root.right = self.__remove(root.right, val)
            return root
        
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        parent = root
        successor = root.right
        while successor.left:
            parent = successor
            successor = successor.left

        root.val = successor.val
        if parent.left == successor:
            parent.left = successor.right
        else:
            parent.right = successor.right
        
        return root

    def search(self, val: any) -> bool:
        if self.__isEmpty():
            raise Exception("Cannot search empty tree")
        return self.__search(self.root, val)

    def __search(self, root: TreeNode, val: any) -> bool:
        if not root:
            return False

        if val < root.val:
            return self.__search(root.left, val)
        elif val > root.val:
            return self.__search(root.right, val)
        else:
            return True 
        
    def minVal(self) -> any:
        if self.__isEmpty():
            raise Exception("Tree is empty")  
        return self.__getMinVal(self.root)
        
    def __getMinVal(self, root: TreeNode) -> any:
        if not root:
            return None

        curr = root
        while curr.left:
            curr = curr.left
        return curr.val

    def maxVal(self) -> any:
        if self.__isEmpty():
            raise Exception("Tree is empty")
        return self.__getMaxVal(self.root)
    
    def __getMaxVal(self, root: TreeNode) -> any:
        if not root:
            return None
        
        curr = root
        while curr.right:
            curr = curr.right
        return curr.val

    def floor(self, val: int) -> int:
        if self.__isEmpty():
            raise Exception("Tree is empty")
        return self.__floor(self.root, val)
    
    def __floor(self, root: TreeNode, val: int) -> int:
        if not root:
            return -1
        
        if root.val == val:
            return root.val
        if root.val > val:
            return self.__floor(root.left, val)

        floor = self.__floor(root.right, val)
        
        return floor if floor <= val and floor != -1 else root.val

    def ceil(self, val: int) -> int:
        if self.__isEmpty():
            raise Exception("Tree is empty")
        return self.__ceil(self.root, val)
    
    def __ceil(self, root: TreeNode, val: int) -> int:
        if not root:
            return -1
        
        if root.val == val:
            return root.val
        if root.val < val:
            return self.__ceil(root.right, val)
        ceil = self.__floor(root.left, val)
        return ceil if ceil >= val else root.val
        

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

    # Helper function to calculate height of binary search tree
    def __getHeight(self, node) -> int:
        if not node:
            return 0
        return 1 + max(self.__getHeight(node.left), self.__getHeight(node.right))        

    def __isEmpty(self) -> bool:
        return not self.root

# MinHeap - A structure in which the root node is the smallest value among its descendant nodes 
#           And the same property must follow for it's left and right subtrees also.
class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val: any) -> None:
        self.heap.append(val)
        index = len(self.heap) - 1 
        while index > 1 and self.heap[index // 2] > self.heap[index]:
            self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index] 
            index = index // 2

    def pop(self) -> any:
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        val = self.heap[1]
        self.heap[1] = self.heap.pop()
        index = 1

        while index * 2 < len(self.heap):
            if 2 * index + 1 < len(self.heap) and \
            self.heap[2*index+1] < self.heap[2*index] and \
            self.heap[index] > self.heap[2*index+1]:
                self.heap[index], self.heap[2*index+1] = self.heap[2*index+1], self.heap[index]
                index = 2 * index + 1
            elif self.heap[index] > self.heap[2*index]:
                self.heap[index], self.heap[2*index] = self.heap[2*index], self.heap[index]
                index = 2 * index
            else:
                break
        return val 

    def heapify(self, arr: list) -> None:
        arr.append(arr[0])

        self.heap = arr
        curr = (len(self.heap)-1) // 2
        while curr > 0:
            index = curr
            while 2*index < len(self.heap):
                if (2*index+1 < len(self.heap)) and \
                self.heap[2*index+1] < self.heap[2*index] and \
                self.heap[index] > self.heap[2*index+1]:
                    self.heap[index], self.heap[2*index+1] = self.heap[2*index+1], self.heap[index]
                    index = 2*index+1
                elif self.heap[index] > self.heap[2*index]:
                    self.heap[index], self.heap[2*index] = self.heap[2*index], self.heap[index]
                    index = 2*index
                else:
                    break
            curr -= 1

    def getMin(self) -> any:
        if len(self.heap) >= 1:
            return self.heap[1]
        else:
            raise Exception("Heap is empty")

    def print(self) -> None:
        print(self.heap[1:])

# MaxHeap - A structure in which the root node is the largest value among its descendant nodes
#           And the same property must follow for it's left and right subtrees also.
class MaxHeap:
    def __init__(self) -> None:
        self.heap = [0]

    def push(self, val: any) -> None:
        self.heap.append(val)
        index = len(self.heap) - 1
        while index > 1 and self.heap[index // 2] < self.heap[index]:
            self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index = index // 2

    def pop(self) -> any:
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        val = self.heap[1]
        self.heap[1] = self.heap.pop()
        index = 1

        while 2*index < len(self.heap):
            if 2*index + 1 < len(self.heap) and \
            self.heap[2*index+1] > self.heap[2*index] and \
            self.heap[index] < self.heap[2*index+1]:
                self.heap[index], self.heap[2*index+1] = self.heap[2*index+1], self.heap[index]
                index = 2*index+1
            elif self.heap[index] < self.heap[2*index]:
                self.heap[index], self.heap[2*index] = self.heap[2*index], self.heap[index]
                index = 2*index
            else:
                break
        return val

    def heapify(self, arr: list) -> None:
        arr.append(arr[0])
        
        self.heap = arr
        curr = (len(self.heap)-1) // 2
        while curr > 0:
            index = curr
            while 2*index < len(self.heap):
                if 2*index+1 < len(self.heap) and \
                self.heap[2*index+1] > self.heap[2*index] and \
                self.heap[index] < self.heap[2*index+1]:
                    self.heap[index], self.heap[2*index+1] = self.heap[2*index+1], self.heap[index]
                    index = 2*index+1
                elif self.heap[index] < self.heap[2*index]:
                    self.heap[index], self.heap[2*index] = self.heap[2*index], self.heap[index]
                    index = 2*index
                else:
                    break
            curr -=1 

    def getMax(self) -> any:
        if len(self.heap) >= 1:
            return self.heap[1]
        else:
            raise Exception("Heap is empty")

    def print(self) -> None:
        print(self.heap[1:])

# Helper class for Adjacency List class
class GraphNode:
    def __init__(self, val: any):
        self.val = val
        self.neighbours = []

# Adjacency list - A strucutre that represents graphs 
#                  using a lists that store a nodes neighbours
class AdjacencyList:
    pass

# Matrix - A structure in which elements are arranged in rows and columns
class Matrix:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for c in range(self.columns)] for r in range(self.rows)]

    # Inserts a specified value into a given row and column of the matrix
    def insert(self, val: any, row: int, column: int) -> None:
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            raise IndexError("row or column is out of bounds")
        self.matrix[row][column] = val
    
    # Removes the first occurence of a specified value 
    def remove(self, val: any) -> None:
        if len(self.matrix) == 0:
            raise Exception("Cannot remove from empty matrix")

        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                if cell == val:
                    self.matrix[i][j] = 0
                    return 
        raise Exception(f"{val} does not exist in matrix")

    def print(self) -> None:
        for row in self.matrix:
            print(" | ".join(map(str, row)))

# Vector - A one dimensional array typically storing numbers that represent direction and magnitude
class Vector:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.vector = [x, y, z]

    def add(self, v: 'Vector') -> None:
        for i in range(len(self.vector)):
            self.vector[i] += v.vector[i]

    def subtract(self, v: 'Vector') -> None:
        for i in range(len(self.vector)):
            self.vector[i] -= v.vector[i]
    
    def multiply(self, v: 'Vector') -> None:
        pass

    def print(self) -> None:
        print(self.vector)

# Hashmap - A structure that maps key : value pairs by computing an index using a hash function
#           The key is unique and immutable and duplicates are not supported 
class HashMap:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.hashmap = [None] * capacity

    def __hash(self, val: any) -> int:
        pass

    def insert(self, val: any, key: any) -> None:
        pass
