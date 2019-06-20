def insertion_sort(arr):
    """ Реализация алгоритма сортировки вставками """

    """ Прохождение по массиву от второго (индекс = 1) до крайнего элемента.
        Нулевой элемент пропускается, т.к. подразумевается, что это множество уже отсортировано.
    """
    for top in range(1, len(arr)):
        k = top

        #print("Отсортированная часть: " + str(arr[0:top]) + " Текущий элемент: " + str(top))

        while k > 0 and arr[k - 1] > arr[k]:
            ''' В данном цикле текущая вершина спускается в отсортированную часть цикла на своё место
            '''

            tmp = arr[k - 1]
            arr[k - 1] = arr[k]
            arr[k] = tmp
            k -= 1

    return arr


if __name__ == "__main__":
    print("Test 0: Массив уже отсортирован")
    array = [0, 1, 2, 3]
    print(array)
    insertion_sort(array)
    print(array)

    print("Test 1: Массив отсортирован в обратном порядке")
    array = [12, 11, 13, 5, 6]
    print(array)
    insertion_sort(array)
    print(array)
    print()

    print("Test 2: Массив не отсортирован")
    array = [7, 2, -4, 0, 3]
    print(array)
    insertion_sort(array)
    print(array)
    print()

    print("Test 3: Массив нулевой длины")
    array = []
    print(array)
    insertion_sort(array)
    print(array)
    print()
