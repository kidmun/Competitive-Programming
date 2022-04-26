
class Solution: 

    def select(self, arr, i):

        for index in range(len(arr)):
           return arr[index]
                
                      
    def selectionSort(self, arr,n):

        for index in range(len(arr)):
            min_index = index

            for j in range(index+1,len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[index], arr[min_index] = arr[min_index], arr[index]
        return arr