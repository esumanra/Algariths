inp = 5988


def no_of_coins(value):
    coins = []
    denos = [1, 2, 5, 10, 20, 50, 100, 500, 1000, 2000]

    for d in denos[::-1]:
        while value >= d:
            value -= d
            coins.append(d)
    return coins


print(no_of_coins(inp))
