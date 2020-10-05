def mergeSort(array):

    if len(array) > 1:
        mid = len(array)
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k=k+1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1

array = []

flag = True
while flag == True:
    try:
        value = int(input("Insira um valor: "))
        array.append(value)
    except ValueError:
        flag = False

mergeSort(array)
print(array)