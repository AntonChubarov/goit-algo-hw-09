from coins import *

import timeit
import matplotlib.pyplot as plt


def benchmark():
    greedy_times = []
    dynamic_times = []

    amounts = list(range(1, 1000, 11))

    for amount in amounts:
        greedy_times.append(timeit.timeit(lambda: find_coins_greedy(amount), number=1000))
        dynamic_times.append(timeit.timeit(lambda: find_min_coins(amount), number=1000))

    plt.scatter(amounts, greedy_times, color='blue', label='Greedy Times')
    plt.scatter(amounts, dynamic_times, color='red', label='Dynamic Times')

    plt.title('Greedy vs Dynamic Programming Benchmark')
    plt.xlabel('Amounts')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    benchmark()
