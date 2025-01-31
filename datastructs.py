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


# linked list - 
class SignlyLL:
    pass

class DoublyLL:
    pass

class Queue:
    pass