def factorial_recursion(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


def factorial_top_down(n, fact_list):
    if n == 0 or n == 1:
        fact_list[n] = 1

    if fact_list[n] is None:
        fact_list[n] = n * factorial_top_down(n - 1, fact_list)

    return fact_list[n]


def factorial_bottom_up(n):
    fact_list = [None] * (n + 1)
    fact_list[0] = fact_list[1] = 1

    for f in range(1, n + 1):
        fact_list[f] = fact_list[f - 1] * f

    return fact_list[n]


print("recursion: {}".format(factorial_recursion(10)))
lis = [None] * (10 + 1)
print(" top_down: {}".format(factorial_top_down(10, lis)))
print("bottom_up: {}".format(factorial_bottom_up(10)))

print("mani".swapcase())
