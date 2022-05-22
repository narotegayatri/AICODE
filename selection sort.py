# Selection sort in Python


def selectionSort(array, s):
    
    
   
    for j in range(s):
        min_idx = j

        for i in range(j + 1, s):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[j], array[min_idx]) = (array[min_idx], array[j])

n = int(input("Enter number of elements : "))
data = []
for i in range(0, n):
    ele = int(input( "number:"))
    data.append(ele)
s = len(data)
selectionSort(data, s)
print('Sorted Array in Ascending Order:')
print(data)