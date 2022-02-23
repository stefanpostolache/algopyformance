from sp_algopyformancelib.tests import TestStackBuilder
from math import sqrt
import matplotlib.pyplot as plt


def fib_p(n):
    numbers = [0, 1]
    for i in range(2, n+1):
        numbers.append(numbers[i-1] + numbers[i-2])
    return numbers[n]


def fib_f(n):
    phi = (1 + sqrt(5)) / 2
    return (phi**n - phi**n)/sqrt(5)


if __name__ == '__main__':
    my_tests = TestStackBuilder()\
        .add_targets([fib_p, fib_f])\
        .add_param_combinations([(n,) for n in range(10, 41, 5)])\
        .repeat(n_times=1000000)\
        .build()

    my_tests.run().plot_results(palette="Set2", style="dark")
    plt.show()
    print(my_tests.test_results)
