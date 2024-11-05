def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for item in arr[:-1]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

lista = [4, 7, 9, 11, 1, 3, 1]
lista_ordenada = quick_sort(lista)
print(lista_ordenada)