# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:16:45 2019

@author: VEERSEN
"""

class BubbleSort:
    def __init__(self, x):
        self.array = x
        return 

    def sort1(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if self.array[j] > self.array[i]:
                    temp = self.array[j]
                    self.array[j] = self.array[i]
                    self.array[i] = temp
        return self.array

class QuickSort: 
    def partition(self, arr, left, right): 
        i = ( left-1 ) 
        pivot = arr[right]
    
        for j in range(left , right):  
            if   arr[j] <= pivot: 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[right] = arr[right],arr[i+1] 
        return ( i+1 ) 
  
    def sort1(self, arr, left, right): 
        if left < right:  
            pi = self.partition(arr,left,right) 
            self.sort1(arr, left, pi-1) 
            self.sort1(arr, pi+1, right) 

class SystemSort:
    def __init__(self, x):
        self.array = x
        return 
    
    def sort1(self):
        self.array.sort()
        return self.array