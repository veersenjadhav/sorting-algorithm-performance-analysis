"""
Created on Sat Jan 5 2019

@author: VEERSEN
"""
from SortingAlgorithms import *
import random

class Array:
    def __init__(self):
        self.small_array = []
        self.medium_array = []
        self.large_array = []

        for i in range(10):
            self.small_array.append(random.randint(0, 1000))

        for i in range(100):
            self.medium_array.append(random.randint(0, 1000))

        for i in range(1000):
            self.large_array.append(random.randint(0, 1000))
        return


# Initialize Arrays
arr1 = Array()
arr2 = Array()
arr3 = Array()

# For Bubble Sort
bs = BubbleSort(arr1.small_array)
%timeit bs.sort1()

bs = BubbleSort(arr1.medium_array)
%timeit bs.sort1()

bs = BubbleSort(arr1.large_array)
%timeit bs.sort1()

# For Quick Sort
qs = QuickSort()
%timeit qs.sort1(arr2.small_array, 0, len(arr2.small_array)-1)

qs = QuickSort()
%timeit qs.sort1(arr2.medium_array, 0, len(arr2.medium_array)-1)

qs = QuickSort()
%timeit qs.sort1(arr2.large_array, 0, len(arr2.large_array)-1)

# For System Sort
ss = SystemSort(arr3.small_array)
%timeit ss.sort1()

ss = SystemSort(arr3.medium_array)
%timeit ss.sort1()

ss = SystemSort(arr3.large_array)
%timeit ss.sort1()