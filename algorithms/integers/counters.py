def count_digits(n):
    if n < 0:
        n = -n

    cnt = 0
    while n > 0:
        n = n // 10
        cnt += 1
    return cnt


if __name__ == "__main__":
    print(count_digits(324345))
    print(count_digits(123))
    print(count_digits(0))
    print(count_digits(-77))
