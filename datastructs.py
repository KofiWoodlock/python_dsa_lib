# Common & custom data structures interface & implementation (C) KFW 2025 

class Array:
    """
    Static array - A structure consisting of elements of the same type, identifiable by an index, 
                stored contiguosly in memory. It's size is not changeable
    ... 

    Attributes:
    -----------
    arr: list
        The actual array that stores the elements 
    type:
        The specified data type of the elements that the array will store 
    size: int
        The maximum capacity of the array
    length: int
        The number of elements the array currently contains
    
    Methods:
    --------
    append(val)
        Adds an element to the end of the array
    delete(val)
        Removes first occurence of specified value
    insertAt(index, val) 
        Inserts and overwrites an element at a given index within the array 
    removeAt(index)
        Removes an element at a given index from the array 
    pop()
        Removes and returns the last element in the array 
    reverse()
        Reverses the contents of the array 
    sort(desc)
        Sorts the contents of the array defaults to ascending order
    get(index)
        Returns the element at a given index
    find(val)
        Finds an element in the array and returns its inded
    print()
        Prints contents of the array
    """

    def __init__(self, size: int, type: any) -> None:
        self.arr: list = [None] * size
        self.type = type
        self.size: int = size
        self.length: int = 0

    def append(self, val: any) -> None:
        """
        Appends an element to the end of the array

        :param val: Value that will be appended to the array

        :raises TypeError: If type of value does not match specified type of array
        :raises OverflowError: If the max capacity of the array has been reached
        """

        self.__checkType(val)
        if self.__isFull():
            raise OverflowError("Cannot append to full array.")
        
        self.arr[self.length] = val
        self.length += 1

    def delete(self, val: any) -> None:
        """
        Deletes the first occurence of a specified value in the array

        :param val: Value that will be deleted from the array

        :raises Exception: If array is empty
        :raises TypeError: If type of value does not match specified type of array
        """

        if self.__isEmpty():
            raise Exception("Cannot delete from an empty array")
        self.__checkType(val)

        found: bool = False
        target_index: int = 0
        for i in range(self.length):
            if self.arr[i] == val:
                found = True
                target_index = i
        
        if found:
            self.arr[target_index] = None
            self.__shiftLeft(target_index)
            self.length -= 1
        
    def insertAt(self, index: int, val) -> None:
        """
        Inserts and overwrites an elements at a given index within the array 

        :param int index: Index that element will be inserted at
        :param val: Value wthat will be inserted

        :raises IndexError: If specified index is out of the array bounds
        :raises TypeError: If type of value does not match specified type of array
        """

        self.__checkType(val)
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")

        self.arr[index] = val
 
    def removeAt(self, index: int) -> None:
        """
        Removes an element at a given index from the array 

        :param int index: Index that element will be removed from

        :raises IndexError: If specified index is out of the array bounds
        :raises Exception: If array is empty
        """

        if self.__isEmpty():
            raise Exception("Cannot remove from empty array.")
        
        if index < 0 or index > self.length:
            raise IndexError("Index out of range.")
    
        self.arr[index] = None
        self.__shiftLeft(index)
        self.length -=1
                
    def pop(self) -> any:
        """
        Removes and returns the last element in the array 

        :return val: Last value in the array
        :raises Exception: If array is empty
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

        :raises Exception: If array is empty
        """

        if self.__isEmpty():
            raise Exception("Cannot reverse empty array.")
        self.arr[:self.length] = self.arr[self.length-1::-1]

    def sort(self, desc: bool=False) -> None:
        """
        Sorts the contents of the array defaults to ascending order

        :param bool desc: Sorts array in descending order
        """
        self.arr = self.__sort(self.arr, desc) 

    def __sort(self, arr: list, desc: bool) -> list:
       if len(arr) <= 1:
           return arr
       
       mid: int = len(arr) // 2
       left_half: list = arr[:mid] 
       right_half: list = arr[mid:self.length]

       left_half = self.__sort(left_half, desc)
       right_half = self.__sort(right_half, desc)
       return self.__merge(left_half, right_half, desc)
    
    def get(self, index: int):
        """
        Returns the element at a given index

        :param int index: Index of the element being accessed

        :raises IndexError: If specified index is out of the array bounds
        """

        if index < 0 or index > self.length:
            raise IndexError("Index out of range.")

        return self.arr[index]

    def find(self, val: any) -> int:
        """
        Finds an element in the array and returns its index

        :param val: Value to be searched for
        """

        for i in range(self.arr):
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

    def __shiftLeft(self, index: int):
        for i in range(index, self.size):
            self.arr[i-1] = self.arr[i]
            self.arr[i] = None
    
    def __checkType(self, val: any) -> None:
        if type(val) == self.type:
            raise TypeError("Value must be of same type declared when initialising array")
    
    def __merge(self, left: list, right: list, desc: bool) -> list:
        res: list = []
        i: int = 0
        j: int = 0

        while i < len(left) and j < len(right):
            if desc:
                if left[i] > right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            else:
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else: 
                    res.append(right[j])
                    j += 1  

        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        
        return res


class DynamicArray:
    """
    Dynamic array - A structure consisting of elements of the same type, 
                    identifiable by an index, stored contiguosly in memory. 
                    It's size is changeable during runtime
    ...

    Attributes:
    -----------
    arr: list
        The actual array that stores the elements  
    type:
        The specified data type of the elements that the array will store
    size: int
        The capacity of the array (dynamic)
    length: int
        The number of elements currently in the array

    Methods:
    --------

    append(val)
        Appends an element to the end of the array
    pop()
        Removes & returns the last element in the array
    insertAt(val, index)
        Inserts & overwrites an element at a given index within the array
    removeAt(index)
        Removes an element at a given index from the array
    reverse()
        Reverses the array
    sort(desc)
        Sorts the array in ascending order by default  
    get(index)
        Returns an element at a given index 
    print()
        Prints contents of the array
    """

    def __init__(self, type) -> None:
        self.type = type
        self.size: int = 2
        self.length: int = 0
        self.arr: list = [None] * self.size

    def append(self, val: any) -> None:
        """
        Appends an element to the end of the array

        :param val: Value appended to the end of the array

        :raises TypeError: If type of value does not match specified type of array
        """

        self.__checkType(val)
        if self.length == self.size:
            self.__resize()
        
        self.arr[self.length] = val
        self.length += 1

    
    def pop(self) -> any:
        """
        Removes & returns the last element in the array

        :raises Exception: If the array is empty 
        """

        if self.__isEmpty():
            raise Exception("Cannot pop from empty array.")
        
        value: any = self.arr[self.length-1]
        self.arr[self.length-1] = None
        self.length -= 1
        return value 
    
    def insertAt(self, val: any, index: int) -> None:
        """
        Inserts & overwrites an element at a given index within the array

        :param int index: Index that element will be inserted at
        :param val: Value wthat will be inserted

        :raises IndexError: If specified index is out of the array bounds
        :raises TypeError: If type of value does not match specified type of array
        """

        self.__checkType(val) 
        if self.__isEmpty() and index > 0:
            raise Exception("Index specified does not exist as array is empty.")
        
        if index < 0 or index > self.length-1:
            raise IndexError("Index out of bounds.")

        self.arr[index] = val

    
    def removeAt(self, index: int) -> None:
        """
        Removes an element at a given index from the array

        :param int index: Index that element will be inserted at

        :raises IndexError: If specified index is out of the array bounds
        :raises Exception: If the array is empty
        """

        if self.__isEmpty():
            raise Exception("Cannot remove from empty array.")

        if index < 0 or index > self.length-1:
            raise IndexError("Index out of bounds.")

        self.arr[index] = None
        self.__shiftLeft(index+1)
        self.length -= 1

    
    def reverse(self) -> None:
        """
        Reverses the array

        :raises Exception: If the array is empty 
        """

        if self.__isEmpty():
            raise Exception("Cannot reverse empty array.")
        self.arr[:self.length] = self.arr[self.length-1::-1]

    def sort(self, desc: bool=False) -> None:
        """
        Sorts the array in ascending order by default  
        """

        self.arr = self.__sort(self.arr, desc)
    
    def __sort(self, arr: list, desc: bool) -> list:
       if len(arr) <= 1:
           return arr
       
       mid: int = len(arr) // 2
       left_half: list = arr[:mid] 
       right_half: list = arr[mid:self.length]

       left_half = self.__sort(left_half, desc)
       right_half = self.__sort(right_half, desc)
       return self.__merge(left_half, right_half, desc)

    def get(self, index: int) -> any:
        """
        Returns an element at a given index 

        :raises IndexError: If specified index is out of the array bounds
        :raises Exception: If the array is empty
        """

        if self.__isEmpty():
            raise Exception("Cannot use get on empty array.")
        if index < 0 or index > self.length-1:
            raise IndexError("Index out of bounds.")
        
        return self.arr[index]
    
    def print(self) -> None:
        """ 
        Prints contents of the array 
        """

        print(self.arr[:self.length])

    def __isEmpty(self) -> bool:
        return self.length == 0

    def __resize(self) -> None:
        self.size *= 2
        new_arr: list = [None] * self.size

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def __shiftLeft(self, index: int):
        for i in range(index, self.size):
            self.arr[i-1] = self.arr[i]
            self.arr[i] = None
    
    def __checkType(self, val: any) -> None:
        if type(val) != self.type:
            raise TypeError("Value must be of same type declared when initialising array.")

    def __merge(self, left: list, right: list, desc: bool) -> list:
        res: list = []
        i: int = 0
        j: int = 0

        while i < len(left) and j < len(right):
            if desc:
                if left[i] > right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            else:
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else: 
                    res.append(right[j])
                    j += 1  

        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        
        return res

           
class Stack:
    """
    Stack - A structure consiting of elements that can be of different types. 
            Operates in the last-in-first-out (LIFO) principle. 

    Attributes:
    ----------- 
    stack: list
        The underlying array which stores elemetns on the stack

    Methods:
    --------
    push(val)
        Adds a value to the top of the stack 
    pop()
        Removes and returns the top value of the stack 
    peek()
        Prints the top value of the stack 
    clear()
        Clears contents of stack
    print()
        Prints contents of stack
    """

    def __init__(self):
        self.stack: list = [] 

    def push(self, val: any) -> None:
        """
        Adds a value to the top of the stack 
        """

        self.stack.append(val)

    def pop(self) -> any:
        """
        Removes and returns the top value of the stack 
        """

        return self.stack.pop()

    def peek(self) -> None:
        """
        Prints the top value of the stack 
        """

        print(self.stack[-1])
    
    def clear(self) -> None:
        """
        Clears contents of stack 
        """

        while self.stack:
            self.stack.pop()

    def print(self) -> None:
        """
        Prints contents of stack
        """

        print(self.stack)


class ListNode:
    def __init__(self, val: any) -> None:
            self.val: any = val
            self.next: ListNode | None = None
            self.prev: ListNode | None = None

  
class SinglyLL:
    """
    Singly Linked list - a structure similar to an array 
                but the elements are not stored contiguosly in memory, 
                they are linked together via pointers to ones memory address 

    Attributes:
    -----------
    head: ListNode
        The first element in the linked list 
    tail: ListNode
        The last element in the linked list
    length: int
        The current length of the linked list
    
    Methods:
    --------
    insertHead(val)
        Inserts an element at the front (head) of the linked list 
    insertTail(val)
        Inserts an element at the end (tail) of the linked list 
    removeHead()
        Removes first (head) element from the linked list
    removeTail()
        Removes the last (tail) element from the linked list
    removeAt(index)
        Removes element at a specified index 
    reverse()
        Reverses contents linked list 
    find(target)
        Checks to see if some element is in the linked list & returns position
    print()
        Prints contents of the linked list 
    """

    def __init__(self) -> None:
        self.head: ListNode = None
        self.tail: ListNode = None
        self.length: int = 0

    def insertHead(self, val: any) -> None:
        """
        Inserts an element at the front (head) of the linked list 
        """

        new_node: ListNode = ListNode(val)

        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insertTail(self, val: any) -> None:
        """
        Inserts an element at the end (tail) of the linked list 
        """

        new_node: ListNode = ListNode(val)

        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
    
    def removeHead(self) -> None:
        """
        Removes first (head) element from the linked list

        :raises Exception: If the linked list is empty 
        """

        if self.__isEmpty():
            raise Exception("Cannot remove from empty linked list")
        
        self.head = self.head.next
        self.length -= 1
    
    def removeTail(self) -> None: 
        """ 
        Removes the last (tail) element from the linked list 

        :raises Exception: If the linked list is empty 
        """

        if self.__isEmpty():
            raise Exception("Cannot remove from empty linked list")
        
        curr = self.head
        while curr:
            if curr.next is self.tail:
                curr.next = None
                self.tail = curr
                self.length -= 1
            elif curr.next and curr.next is not self.tail:
                curr = curr.next
            else:
                break

 
    def removeAt(self, index: int) -> None:
        """
        Removes element at a specified index 

        :raises IndexError: If specified index is out of the linked list bounds
        """

        if index < 0 or index > self.length -1:
            raise IndexError("Index is out of bounds")

        i: int = 0 
        curr: ListNode = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        self.length -= 1

    def reverse(self) -> None:
        """
        Reverses contents linked list 

        :raises Exception: If the linked list is empty
        """

        if self.__isEmpty():
            raise Exception("Cannot reverse empty linked list.")
        
        curr: ListNode = self.head
        prev = None
        while curr:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


    def find(self, target: any) -> int:
        """
        Checks to see if some element is in the linked list & returns position
        """

        position: int = 0
        curr: ListNode = self.head
        while curr:
            if curr.val == target:
                return position
            else:
                curr = curr.next
                position += 1
        return -1

    def print(self) -> None:
        """
        Prints contents of the linked list 
        """

        curr: ListNode = self.head
        while curr != None:
            print(f"{curr.val}->",end="")
            curr = curr.next
        print()

    def __isEmpty(self) -> bool:
        return not self.head


class DoublyLL:
    """
    Doubly linked list - A structure similar to a singly linked list 
                        but each element within the list is connected to the 
                        previous and next node via pointers 
    
    Attributes:
    -----------
    head: ListNode
        The first element in the linked list 
    tail: ListNode
        The last element in the linked list
    length: int
        The current length of the linked list
    
    Methods:
    --------
    """

    def __init__(self) -> None:
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self.length: int = 0
    

    def insertHead(self, val: any) -> None:
        """
        Inserts an element at the head (front) of the linked list 
        """

        new_node: ListNode = ListNode(val)
        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
        else:            
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1 


    def insertTail(self, val: any) -> None:
        """
        Inserts an element at the tail (end) of the linked list
        """

        new_node: ListNode = ListNode(val)
        if self.__isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1


    def insertAt(self, val: any, index: int) -> None:
        """
        Inserts an element at a given index 

        :raises IndexError: If the specified index is outside the bounds of the linked list 
        """

        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.insertHead(val)
            return
        elif index == self.length:
            self.insertTail(val)
            return

        new_node: ListNode = ListNode(val)
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
        

    def removeHead(self) -> None:
        """
        Removes the element at the head (front) of the linked list
        """

        if self.__isEmpty():
            raise Exception("Cannot remove from empty list")
        
        self.head.next.prev.val = None
        self.head = self.head.next


    def removeTail(self) -> None:
        """
        Removes the element at the tail (end) of the linked list
        """
        
        if self.__isEmpty():
            raise Exception("Cannot remove from empty list")
        
        self.tail.prev.next = None
        self.tail = self.tail.prev


    def removeAt(self) -> None:
        """
        Removes the element at a given index 
        """
        pass


    def clear(self) -> None:
        """
        Removes all elements from the linked list
        """

        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = None
            curr.prev = None
            curr = next_node
        
        self.head = None
        self.tail = None
        self.length = 0
    
     
    def find(self, target) -> int:
        """
        Checks to see if some element is in the linked list & returns position
        """

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
        """ Prints contents of linked list """

        curr = self.head
        while curr != None:
            print(f"{curr.val}<->",end="")
            curr = curr.next
        print()

    def __isEmpty(self) -> bool:
        return not self.head


class Queue:
    """
    Queue - A structure consiting of elements that can be of different types. 
            Operates in the first-in-first-out (FIFO) principle 
            meaning the first element added will be the first element removed
    """
    def __init__(self) -> None:
        self.first: ListNode = None 
        self.last: ListNode = None
        self.length: int = 0

    def enqueue(self, val: any) -> None:
        """
         Adds an item to the front of the queue 
        """
        new_node: ListNode = ListNode(val)
        
        if self.__isEmpty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next
        self.length += 1

    def dequeue(self) -> any:
        """
        Removes the first item from the queue 
        """
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
    
    def getfront(self) -> any:
        """
        Returns the first item in the queue
        """
        return self.first.val

    def getRear(self) -> any:
        """
        Returns the last item in the queue  
        """
        return self.last.val

    def print(self) -> None:
        """
        Prints the entire queue 
        """
        curr = self.first
        while curr != None:
            print(f"{curr.val}->",end="")
            curr = curr.next
        print()

    def __isEmpty(self) -> int:
        return self.length == 0


class Deque:
    """
    Deque - Short for double ended queue it is a structure consiting of elements that cane be of different types.
         It is similar to a queue in the fact it operates in the first-in-first-out (FIFO) principle but differs to a queue
         as both ends can act as the first element in the queue i.e elements can be added and removed from the front and back    
    """
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
    """
    Circular queue - similar to a regular queue except the last element in the queue is connected to
                  the first element, forming a circle. A circualr queue still operates in the first-in-first-out (FIFO)
                  principle
    """
    def __init__(self, size: int, type: any):
        self.size: int = size
        self.type: any = type
        self.queue: list = [None] * self.size
        
    def enqueue(self, val: any) -> None:
        """
        Adds an item to the front of the queue 
        """
        pass

    def dequeue(self) -> any:
        """
        Removes the first item from the queue        
        """
        pass
    
    def getfront(self) -> any:
        """
        Returns the first item in the queue       
        """
        pass

    def getRear(self) -> any:
        """
        Returns the last item in the queue        
        """
        pass


class PriorityQueue:
    """
    Priority queue - A subset of the queue data structure that arranges elements based on their priority value.
                  Elements with a higher priority are retrieved and removed first                   
    """
    pass


class CircularBuffer:
    """
    Circular buffer - A structure consisting of elements of the same type, identifiable by an index,
                   stored contigously in memory. It's size is not changeable & once the buffer is full
                   the oldest data is overwrited starting from the beginning.
    """
    def __init__(self, size: int, type: any) -> None:
        self.buffer = Array(size, type)
        self.type = type
        self.size = size
        self.first = 0

    def insert(self, val) -> None:
        if type(val) != self.type:
            raise TypeError("Value data type does not match specified data type.")

        if self.__isFull():
            raise MemoryError("Buffer is full.")

        last = (self.first + self.buffer.length) % self.buffer.size
        self.buffer.insertAt(last, val)
        self.buffer.length += 1

    def remove(self):
        if self.__isEmpty():
            return None
        
        val = self.buffer.get(self.first)
        self.first = (self.first + 1) % self.buffer.size
        self.buffer.length -= 1
        return val

    def getFirst(self) -> any:
        if self.__isEmpty():
            return None
        return self.buffer.get(self.first)

    def getLast(self) -> any:
        if self.__isEmpty():
            return None
        last = (self.first + self.buffer.length-1) % self.buffer.size
        return self.buffer.get(last)

    def print(self):
        print(self.buffer.print())

    def __isFull(self) -> bool:
        return self.buffer.length == self.buffer.size

    def __isEmpty(self) -> bool:
        return self.buffer.length == 0


class TreeNode:
    """
    Helper class for BinaryTree & Binary Search Tree classes  
    """
    def __init__(self, val: any) -> None:
        self.val: any = val
        self.left: TreeNode = None
        self.right: TreeNode = None


class PointerBinaryTree:
    """
    Binary tree (pointer) - A structure in which data is arranged in a tree-like structure
               consiting of a root node, branch nodes and leaf nodes. Each node can have
               a maximum of two child nodes. Nodes are implemented using pointers.  
    """

    def __init__(self) -> None:
        self.root: TreeNode = None

    def insert(self, val: any) -> None:
        """
        Adds a new node to the tree in the next non-complete layer from left to right     
        """
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

    def remove(self, val: any) -> None:
        """
        Removes a specified element from the tree and replaces it with bottom right-most node   
        """

        self.root = self.__remove(self.root, val)
    
    def __remove(self, root: TreeNode, val: any) -> TreeNode:
        if self.__isEmpty():
            raise Exception("Cannot remove from empty tree")

        if not root.left and not root.right:
            if root.val == val:
                return None
            else:
                return root

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
    
    def pop(self) -> any:
        """
        Removes and returns the deepest node in binary tree 
        """ 

        q: Queue = Queue()
        out: list = []

        if self.root:
            q.enqueue(self.root)

        while q.length > 0:
            for i in range(q.length):
                curr = q.dequeue()
                out.append(curr)
                if curr.left:
                    q.enqueue(curr.left)
                if curr.right:
                    q.enqueue(curr.right)
        
        val: any = out[-1].val
        self.remove(out[-1].val)
        return val
        
    def preOrder(self) -> None:
        """
        Prints nodes in pre-order (root, left, right)  
        """

        self._preOrder(self.root) 
        
    def _preOrder(self, root) -> None:
        if not root:
            return

        print(root.val, end="")
        self._preOrder(root.left)
        self._preOrder(root.right)


    def inOrder(self) -> None:
        """
        Prints nodes in-order (left, root, right) 
        """

        self._inOrder(self.root)
    
    def _inOrder(self, root) -> None:
        if not root:
            return

        self._inOrder(root.left)
        print(root.val, end="")
        self._inOrder(root.right)


    def postOrder(self) -> list:
        """
        Prints nodes in post-order (left, right, root) 
        """

        self._postOrder(self.root)
    
    def _postOrder(self, root) -> None:
        if not root:
            return 

        self._postOrder(root.left)
        self._postOrder(root.right)
        print(root.val, end="")
    
    def levelOrder(self) -> list:
        """ 
        Returns a list of nodes in a level order fashion computing left to right 
        """

        return self.__levelOrder(self.root)
    
    def __levelOrder(self, root) -> list:        
        q = Queue()
        out = []

        if root:
            q.enqueue(root)

        while q.length > 0:
            for i in range(q.length):
                curr = q.dequeue()
                out.append(curr.val)
                if curr.left:
                    q.enqueue(curr.left)
                if curr.right:
                    q.enqueue(curr.right)
        
        return out

    def maxHeight(self) -> int:
        return self.__getHeight(self.root)

    def maxDepth(self) -> int:
        pass

    def enumerate(self) -> None:
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

    def __getHeight(self, node) -> int:
        """
        Helper function to calculate height of binary tree
        """
        if not node:
            return 0
        return 1 + max(self.__getHeight(node.left), self.__getHeight(node.right))
    
    def __remDeepest(self, root, target) -> None:
        """
        Helper function to delete deepest node in binary tree 
        """

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


class ArrayBinaryTree:
    """
     Binary tree (array) - A structure in which data is arranged in a tree-like structure
               consiting of a root node, branch nodes and leaf nodes. Each node can have
               a maximum of two child nodes. Nodes are implemented using array indexes.  
    
    """
    def __init__(self) -> None:
        self.tree = [0]
        self.size = 0
    
    def insert(self, val: any) -> None: 
        self.tree.append(val)
        self.size += 1
    
    def remove(self) -> any:
        val = self.tree.pop()
        self.size -= 1
        return val

    def find(self, val: any) -> bool:
        if self.__isEmpty():
            return False
        
        curr = 1
        while curr < self.size:
            if self.tree[curr] == val:
                return True
            curr += 1

    def getNode(self, index: int) -> any:
        if self.__isEmpty():
            return None        
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
 
        return self.tree[index]

    def getParent(self, index: int) -> any:
        if self.__isEmpty():
            return None        
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
 
        return self.tree[index // 2]

    def getLeft(self, index: int) -> any:
        if self.__isEmpty():
            return None        
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        
        if (2 * index) < self.size:
            return self.tree[2 * index] 
        else:
            return None
    
    def getRight(self, index: int) -> any:
        if self.__isEmpty():
            return None
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if (2 * index) < self.size:
            return self.tree[2 * index + 1] 
        else:
            return None
 
    def print(self) -> None:
        print(self.tree[1:])

    def __isEmpty(self) -> bool:
        return self.size == 0


class BST:
    """
    Binary search tree - A structure similar to a binary tree however the tree has an ordered property.
                      Meaning nodes smaller than the root will be inserted into the left subtree 
                      whereas nodes larger than the root will be inserted into the right subtree.
    """

    def __init__(self):
        self.root = None

    def insert(self, val: any) -> None:
        """ Inserts a value into the binary search tree """

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
        """ Removes a value from the binary search tree """
        
        if self.__isEmpty():
            return

        curr = self.root
        while curr: 
            if curr.val > val:
                curr = curr.left
            elif curr.val < val:
                curr = curr.right
            else:
                if not curr.left:
                    pass 
        return False

    def search(self, val: any) -> bool:
        """ Searches for a specified value in the binary search tree, returns true if found else false """
        
        curr = self.root
        while curr:
            if curr.val == val:
                return True
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return False
    
    def preOrder(self) -> None:
        """
        Prints nodes in pre-order (root, left, right)  
        """

        self._preOrder(self.root) 
        
    def _preOrder(self, root) -> None:
        if not root:
            return

        print(root.val, end="")
        self._preOrder(root.left)
        self._preOrder(root.right)


    def inOrder(self) -> None:
        """
        Prints nodes in-order (left, root, right) 
        """

        self._inOrder(self.root)
    
    def _inOrder(self, root) -> None:
        if not root:
            return

        self._inOrder(root.left)
        print(root.val, end="")
        self._inOrder(root.right)


    def postOrder(self) -> list:
        """
        Prints nodes in post-order (left, right, root) 
        """

        self._postOrder(self.root)
    
    def _postOrder(self, root) -> None:
        if not root:
            return 

        self._postOrder(root.left)
        self._postOrder(root.right)
        print(root.val, end="")
    

    def floor(self, k: int) -> int:
        """ Returns the largest element that is less than or equal to k """
        
        return self.__floor(k, self.root)

    def __floor(self, k: int, root: TreeNode) -> int:
        if not root:
            return -1

        if root.val == k:
            return root.val        
        if root.val > k:
            return self.__floor(k, root.left)
        
        floor: TreeNode | int = self.__floor(k, root.right)
        return floor if floor <= k and floor != -1 else root.val


    def ceil(self, k: int) -> int:
        """ Returns the smallest values that is greater than or equal to k """
        
        return self.__ceil(k, self.root)
    
    def __ceil(self, k: int, root: TreeNode) -> int:
        if not root:
            return -1
        
        if root.val == k:
            return root.val
        if root.val < k:
           return self.__ceil(k, root.right) 
        
        ceil: TreeNode | int = self.__ceil(k, root.left)
        return ceil if ceil >= k else root.val

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

    def __minVal(self, root: TreeNode) -> any:
        """ Returns the minimum node of a subtree specified by an input root """

        curr = root
        while curr and curr.left:
            curr = curr.left 
        return curr 

    def __getHeight(self, node) -> int:
        """ Helper function to calculate height of binary search tree """

        if not node:
            return 0
        return 1 + max(self.__getHeight(node.left), self.__getHeight(node.right)) 

    def __isEmpty(self):
        return not self.root


class MinHeap:
    """
    MinHeap - A structure in which the root node is the smallest value among its descendant nodes 
           And the same property must follow for it's left and right subtrees also.
    """
    def __init__(self):
        self.heap = []

    def insert(self, val: any) -> None:
        """ Inserts a value to the heap and orders depending on its value. Lowest becoming the root. """
        self.heap.append(val)
        index = len(self.heap) -1 
        while index > 0 and self.heap[index-1 // 2] > self.heap[index]:
            self.heap[index], self.heap[index-1 // 2] = self.heap[index-1 // 2], self.heap[index] 
            index = (index - 1) // 2

    def delete(self) -> None:
        """ Removes the node with the smallest value from the heap """

        # Stores value with minimum value i.e the 1st index in umderlying array 
        res = self.heap[1]
        # Update first element with last element 
        self.heap[1] = self.heap.pop()
        
        # Ensure min property of heap 
        # if root node is now larger than any of its descendatns move that node to the correct position 

        # helper function to percolate nodes to correct position
        self.__percolateDown()
    
    def __percolateDowm(self) -> None:
        index = 1
        # While current node is not a leaf node 
        while 2*index < len(self.heap):
            if (2*index + 1 < len(self.heap)) and self.heap[index] > self.heap[2*index+1]:
                self.heap[index], self.heap[2*index+1] =  self.heap[2*index+1], self.heap[index]
                index = 2*index+1
            elif self.heap[index] > self.heap[2*index]:
                self.heap[index], self.heap[2*index] =  self.heap[2*index], self.heap[index]
                index = 2*index+1
            else:
                break
        


    def heapify(self, Iterable: list ) -> None:
        pass


class MaxHeap:
    pass


class Vector:
    """ 
    """


class Matrix:
    """
    Matrix - A two-dimnensional structure arranged in rows and columns   

    Attributes:
    -----------
    matrix: list
        The underlying array that stores the elements in the matrix 
    rows: int
        The number of rows in the matrix     
    cols: int
        The number of columns in the matrix 
    
    Methods:
    --------
    insert(val, row, column)
        Inserts and overwrites a value into the matrix at a given position 
    """

    def __init__(self, rows: int, cols: int) -> None:
        self.rows: int = rows
        self.columns: int = cols
        self.matrix: list[list] = [[None for col in range(cols)] for _ in range(rows)]

    def insert(self, val: any, row: int, column: int) -> None:
        """ 
        Inserts and overwrites a value into the matrix at a given position 

        :raises IndexError: If the row or column is out of matrix bounds
        """

        if row < 0 or row > self.rows:
            raise IndexError("Index out of bounds")
        if column < 0 or column > self.columns:
            raise IndexError("Index out of bounds")
        
        self.matrix[row][column] = val
    
    def remove(self, row: int, column: int) -> None:
        """
        Removes an element from the matrix at a specified index

        :raises: Exception: If the index specified is empty
        """

        if self.matrix[row][column] == None:
            raise Exception("Cannot remove empty element")
        
        self.matrix[row][column] = None
    
    def search(self, target: any) -> bool:
        """
        Searches for an element within the matrix, return True if found else False
        """

        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] == target:
                    return True
        return False
    
    def add(self, m: 'Matrix') -> None:
        """
        Performs matrix addition with another N x M matrix

        :raises Exception: If the matricies are not equal in size
        """

        if (m.rows != self.rows) or (m.columns != self.columns):
            raise Exception("Matricies my be the same size")

        for i in range(m.rows):
            for j in range(m.columns):
                self.matrix[i][j] += m.matrix[i][j]

    def subtract(self, m: 'Matrix') -> None:
        """
        Performs matrix subtraction with another N x M matrix

        :raises Exception: If the matricies are not equal in size
        """

        if (m.rows != self.rows) or (m.columns != self.columns):
            raise Exception("Matricies my be the same size")

        for i in range(m.rows):
            for j in range(m.columns):
                self.matrix[i][j] -= m.matrix[i][j]
    
    def scalarMultiply(self, k: int) -> None:
        """
        Multiplies matrix by given scalar k
        """
        
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] is not None:
                    self.matrix[i][j] *= k
         
    def print(self) -> None:
        """
        Prints contents of the matrix
        """

        for i in range(self.rows):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=" ")
            print()


class HashTable:
    """
    Hash Table - A structure that creates a mapping between keys and values using hashing  
                 this implementation uses chaining to deal with collisions

    Attributes:
    -----------
    capacity: int
        The maximum size of the hash table
    table: list
        The actual hash table data structure

    Methods:
    --------
    __hash(key)
        Takes a key argument of either type string or int and performs hash function to produce some index 
    insert(item)
        Inserts an item into the hash table 
    remove(item)
        Removes an item from the hash table 
    print()
        Prints the contents of the hash table  
    __getCapacity()
        Getter method for capacity
    """

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.table: list[list] = [[] for _ in range(capacity)]

    def __hash(self, key: any) -> int:
        """ 
        Takes a key argument of either type string or int and performs hash function to produce some index 

        :param key: The key that will be mapped to a value
        """
        
        if type(key) == int:
            # Use division hash algorithm h(key) = key % capacity
            return key % self.capacity
        if type(key) == str:
            # Use ASCII characters: h(key) = sum(a for c in s) % capacity
            # where a is ascii value, c is the character, s is the string input
            return (sum(ord(c) for c in key) % self.capacity)

    def insert(self, item: any) -> None:
        """ 
        Inserts an item into the hash table 

        :param item: Item that will be inserted into the hash table
        """
        
        index: int = self.__hash(item)
        self.table[index].append(item)

    def remove(self, item: any) -> None:
        """ 
        Removes an item from the hash table 

        :param item: Item that will be removed from the hash table
        """

        index: int = self.__hash(item)
        if item not in self.table[index]:
            return
        self.table[index].remove(item)
    
    def print(self) -> None:
        """ 
        Prints the contents of the hash table  
        """
        
        for i in range(self.capacity):
            print(f"{i}", end="")
            for j in self.table[i]:
                print(f" --> {j}", end="")
            print()
    
    def __getCapacity(self) -> int: return self.capacity 
