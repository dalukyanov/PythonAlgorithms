def sum_of_digits(n):
    """
    Функция вычисляет сумму всех разрядов в числе
    """
    sm = 0
    while n > 0:
        d = n % 10
        n = n // 10
        sm += d
    return sm


def recursive_sum_of_digits(n):
    """
    Алгоритм вычисляет рекурсивно сумму всех цифр, входящих в число "n" до тех пор пока не останется один разряд
    Пример:

    digital_root(132189)
    => 1 + 3 + 2 + 1 + 8 + 9
    => 24 ...
    => 2 + 4
    => 6

    """
    while n > 9:
        n = sum_of_digits(n)
    return n


if __name__ == "__main__":
    print(recursive_sum_of_digits(16))         # 7
    print(recursive_sum_of_digits(942))        # 6
    print(recursive_sum_of_digits(132189))     # 6
    print(recursive_sum_of_digits(493193))     # 2
    print(recursive_sum_of_digits(0))          # 0
