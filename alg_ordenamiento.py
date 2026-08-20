
def BubbleSort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)):
              if(arr[i] < arr[j]):
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

    return arr

# each iteration we get a key and keep checking each element to the left until j < 0. 
# after elements have been organized, add the key to j + 1, which adjusts the array correctly after all the operations inside the while.
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

    return arr

# quicksort uses the pivot method to get the middle, left and right parts of the array and doing recursiveness.
# in this case this is a compact implementation but there are some problems with the memory 
def QuickSort(arr):

    # base case (len of array is one or less. if it's less it's because some of the arrays like left or right didn't get any elements.)
    if len(arr) <= 1:
        return arr

    # get the pivot
    pivot = arr[len(arr) // 2] # // means floor division. so if we have 5 // 2, the result will be 2, as it divides it and floors the result to the nearest whole integer.

    # we can get the left, middle and right parts of the array through this method, specifying what we want inside an array using a for and a condition.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # lastly we can just return the middle (which is one element) and then the left and right parts.
    return QuickSort(left) + middle + QuickSort(right)
     
array = [3, 66, 2, 1, 8, 100, 7, 89, 0, -3]

print(BubbleSort(array))
print(InsertionSort(array))
print(QuickSort(array))
