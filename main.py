import numpy as np

from utils.function import update_function


def update(array: np.ndarray) -> np.ndarray:
    _size: int = len(array)
    random_sample_id_list = np.random.choice(_size, _size, replace=False)  # equal to permutation

    res_array = np.zeros(shape=_size, dtype=np.float128)

    for i in range(0, _size):
        res_array[i] = update_function(array[random_sample_id_list[i]], array[random_sample_id_list[(i + 1) % _size]])
    return res_array


def main():
    _mu, _sigma = np.float128(0), np.float128(10)
    opinion_vector = np.random.normal(_mu, _sigma, size=100)
    _size: int = len(opinion_vector)
    print(_size)


if __name__ == "__main__":
    main()
