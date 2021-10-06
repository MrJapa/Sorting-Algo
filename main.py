def partition(arr, low, high):
    i = (low-1)         # indeks for lavere elementer
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # Hvis gælende element er mindre eller
        # lige med pivot
        if arr[j] <= pivot:
  
            # stigning for mindre elementer
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
    
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi er partitioneringsindeks
        pi = partition(arr, low, high)
  
        # Sorter elementer og før partitionen
        # og efter partitionen
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  

# Driver kode: Koden som definerer array og printer ud 
arr = [12, 4, 18, 23, 1, 5, 6, 9, 20, 10, 31]
n = len(arr)
quickSort(arr, 0, n-1)
text = "sorteret array er: {}".format(arr)
print(text)