
# iterates through the array from the start of it. worst case is searching the last number of the array or a number that is not contained within the array.
def LinearSearch(arr, value):

    for i in range(len(arr)):
        if(arr[i] == value):
            return i

    return -1


# we use a similar approach to quick sort, but instead of generating new lists/arrays we get the indexes for right, left and middle
def BinarySearch(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:

        middle = (left + right) // 2

        if(value == array[middle]): # we check if the middle value is what we are searching for. if so, return the index
            return middle

        if(value > array[middle]): # if the value is greater than middle, left is middle +1, as we discard the previous left half we had
            left = middle + 1

        elif(value < array[middle]): # if the value is lesser than the middle half, we discard the right half by updating the right value
            right = middle - 1

    # in case nothing was found, return -1
    return -1

# in the hash search we search for a value in a given table. 
def HashSearch(hash_table, hash):

    if(hash in hash_table):
        return hash_table[hash]

    # in any other case we return -1
    return -1

# for binary search it assumes the array is already ordered. 
array = [2, 3, 5, 6, 7, 46, 60, 79, 85, 467, 897]

# hash table for the hashsearch

hash_table = {
    "Mnbv&%677Hg": "javier",
    "KL{O7u9D": "alex",
    "GHDVNm$Fd/": "hola",
    "GdfgR3$%7JK": "futbol por la banda"
}

print(LinearSearch(array, 60))
print(BinarySearch(array, 897))
print(HashSearch(hash_table, "GdfgR3$%7JK"))

