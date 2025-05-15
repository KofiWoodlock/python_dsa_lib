# Common algorithm implementations (C) KFW 2025
from datastructs import *
from typing import Iterable 

# ------------- Searching algorithms -------------

def linearSearch(iterable: Iterable, target: any) -> bool:
    """
    Checks each element in iterable returns True if value is found else False
    """

    for i in range(len(iterable)):
        if iterable[i] == target:
            return True
    return False

def binarySearch(iterable: Iterable, target: any) -> bool:
    l = 0
    r = len(iterable)-1

    while l<= r:
        m = l+(r-l) // 2
        if iterable[m] == target:
            return True
        elif iterable[m] < target:
            l = m+1
        else:
            r = m-1
    return False


def binaryTreeSearch(root: TreeNode, val: any) -> bool: 
    curr = root
    while curr:
        if curr.val == val:
            return True
        elif curr.val > val:
            curr = curr.left
        else:
            curr = curr.right
    return False

# ------------- Sorting algorithms -------------

def bubbleSort(array: list) -> list:
    for i in range(len(array)-1):
        for j in range(i, len(array)-1):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    
    return array

def mergeSort(iterable: Iterable) -> Iterable:
    pass

def quickSort(iterable: Iterable) -> Iterable:
    pass

def insertionSort(iterable: Iterable) -> Iterable:
    pass
