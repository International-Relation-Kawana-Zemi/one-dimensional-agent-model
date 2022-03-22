from typing import Callable

import matplotlib.pyplot as plt
import numpy as np

from utils.function import Z, update_function


def update(
    array: np.ndarray,
    omega: np.float128 = np.float128(0.5),
    sigma: np.float128 = np.float128(0.50),
    Z: Callable[[np.float128], np.float128] = Z,
) -> np.ndarray:

    _size: int = len(array)
    random_sample_id_list = np.random.choice(_size, _size, replace=False)  # equal to permutation

    res_array = np.zeros(shape=_size, dtype=np.float128)

    for i in range(0, _size):
        res_array[i] = update_function(
            array[random_sample_id_list[i]],
            array[random_sample_id_list[(i + 1) % _size]],
            omega=omega,
            sigma=sigma,
            Z=Z,
        )
    return res_array


def graph_show(opniion_vector: np.ndarray, _t: int, omega: np.float128, sigma: np.float128):

    plt.figure(figsize=(10, 10))
    plt.xlim(-1, 1)
    plt.ylim(0, 100)

    plt.title("t: {}".format(_t))
    plt.xlabel("opnion-vector")
    plt.ylabel("frequency")

    plt.hist(opniion_vector, bins=100, range=(-1, 1), alpha=0.7)

    plt.savefig("output/omega={}, sigma={}, t={}.png".format(omega, sigma, _t))


def main():

    omega: np.float128 = np.float128(0.5)
    sigma: np.float128 = np.float128(0.50)

    _mu, _sigma = np.float128(0), np.float128(10)
    # opinion_vector = np.random.normal(_mu, _sigma, size=100) # 正規分布では範囲指定ができない？
    opinion_vector = np.random.uniform(-1, 1, 100)  # [-1, 1]の一様分布

    _trail_max: int = 1000
    output_t_array: list[int] = [0, 1, 2, 3, 5, 10, 30, 60, 90, 100, 300, 600, 900, 1000]

    for _t in range(0, _trail_max + 1):
        if _t in output_t_array:
            print("t: {}".format(_t))
            print("opinion_vector: {}".format(opinion_vector))
            print("")
            graph_show(opinion_vector, _t, omega, sigma)

        opinion_vector = update(opinion_vector, omega=omega, sigma=sigma)


if __name__ == "__main__":
    main()
