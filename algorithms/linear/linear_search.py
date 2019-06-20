def linear_search(arr, x):
    """ Алгоритм линейного поиска элемента x в массиве arr.
        Возвращает индекс первого вхождения элемента, либо -1 в случае, если элемент не найден.
    """
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


if __name__ == "__main__":
    A = [5, 3, -6, 11, 0]
    print(linear_search(A, 11))
