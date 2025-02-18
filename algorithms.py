# Common algorithm implementations (C) KFW 2025
from typing import Iterable 

# Linear search - An algorithm that checks each element in an iterable
def linearSearch(iterable: Iterable, target: any) -> bool:
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


