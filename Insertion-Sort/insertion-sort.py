def insertionSort1(n, arr):
    last_index = len(arr)-1
    value = arr[last_index]
    while value < arr[last_index-1] and last_index > 0:
        arr[last_index] = arr[last_index-1]
        last_index -= 1
        print(*arr)
        
    arr[last_index] = value
    print(*arr)
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
