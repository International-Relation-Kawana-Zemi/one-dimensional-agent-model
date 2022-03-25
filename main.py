import numpy as np
import seaborn as sns
from scipy.stats import truncnorm

from utils.OpinionVector import graph_plot, update


def main():

    sns.set()
    np.random.seed(0)

    max_range_number = 1.0
    min_range_number = -1.0

    mean, std = 0.0, 0.34

    max_range_number, min_range_number = (max_range_number - mean) / std, (min_range_number - mean) / std

    omega: np.float128 = np.float128(0.5)
    # epsilon: np.float128 = np.float128(0.50)

    for epsilon in np.arange(0.1, 1.0, 0.1):
        # opinion_vector = np.random.uniform(-1, 1, 100)  # [-1, 1]の一様分布
        opinion_vector = truncnorm.rvs(min_range_number, max_range_number, loc=mean, scale=std, size=1000)

        _trail_max: int = 1000
        output_t_array: list[int] = [0, 1, 2, 3, 5, 10, 30, 60, 90, 100, 300, 600, 900, 1000]

        for _t in range(0, _trail_max + 1):
            if _t in output_t_array:
                print("t: {}".format(_t))
                print("opinion_vector: {}".format(opinion_vector))
                print("")
                graph_plot(opinion_vector, _t, omega, epsilon)

            opinion_vector = update(opinion_vector, omega=omega, epsilon=epsilon)


if __name__ == "__main__":
    main()
