def test(n, *args, txt='Сумма'):
    s = 0
    for i in range(len(args)):
        s += args[i] // n
    print(txt + ':', s)


test(2, 1, 2, 3, txt='квадратный корень суммы')


def test2(n):
    if n == 0:
        return 1

    else:
        return n * test2(n - 1)

print(test2(6))
