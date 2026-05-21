# Question:-  Implement Merge Sort in Python to sort an array of integers using the Divide and Conquer approach.



def merge(arr, left, mid, right):
    
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0  # Pointer for L
    j = 0  # Pointer for R
    k = left  # Pointer for main array

    # Compare and merge
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # remaining elements of L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # remaining elements of R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Recursive Merge Sort 
def merge_sort(arr, left, right):
    # Divide array until single element
    if left < right:
        mid = (left + right) // 2 

        merge_sort(arr, left, mid)      
        merge_sort(arr, mid + 1, right) 

        merge(arr, left, mid, right)   




if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements separated by space: ").split()))

    print("Original Array:", arr)

    merge_sort(arr, 0, n - 1)

    print("Sorted Array:", arr)