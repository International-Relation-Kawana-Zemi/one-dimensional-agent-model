from typing import Callable

import matplotlib.pyplot as plt
import numpy as np

from utils.function import Z, update_function


def update(
    array: np.ndarray,
    omega: np.float128 = np.float128(0.5),
    epsilon: np.float128 = np.float128(0.50),
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
            epsilon=epsilon,
            Z=Z,
        )
    return res_array


def graph_plot(opniion_vector: np.ndarray, _t: int, omega: np.float128, epsilon: np.float128):

    plt.figure(figsize=(10, 10))
    plt.xlim(-1, 1)
    plt.ylim(0, 100)

    plt.title("t: {}".format(_t))
    plt.xlabel("opnion-vector")
    plt.ylabel("frequency")

    plt.hist(opniion_vector, bins=100, range=(-1, 1), alpha=0.7)

    plt.savefig("output/epsilon={}/omega={},t={}.png".format(omega, epsilon, _t))
