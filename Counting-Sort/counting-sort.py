
def countingSort(arr):
    arr_size = 100 
    new_arr = []
    for index in range(arr_size):
        new_arr.append(0)
    for num in arr:
        new_arr[num] += 1
    return new_arr
        
         
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
