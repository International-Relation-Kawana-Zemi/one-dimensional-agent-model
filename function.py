from typing import Callable

import numpy as np


def step_function(number: np.float128) -> int:
    """
    args: number(float128)

    returns: int

    note: number == 0のときについても再検討の余地あり
    """
    if number > 0:
        return 1
    else:
        return 0


def F(o_i_t: np.float128, o_j_t: np.float128, sigma: np.float128 = np.float128(0.50)) -> int:
    """
    args:
        o_i_t: state of i at time t
        o_j_t: state of j at time t

    returns: int
    """
    return step_function(2 * sigma - np.abs(o_j_t - o_i_t))


def G(o_i_t: np.float128, o_j_t: np.float128, omega: np.float128 = np.float128(0.5)) -> np.float128:
    """
    args:
        o_i_t: state of i at time t
        o_j_t: state of j at time t

    returns: np.float128
    """
    return o_i_t + omega * (o_j_t - o_i_t)


def Z(o_i_t: np.float128) -> np.float128:
    """
    args:
        o_i_t: state of i at time t

    returns: np.float128
    """
    return np.float128(0)


def update_function(o_i_t: np.float128, o_j_t: np.float128, Z: Callable[[np.float128], np.float128]) -> np.float128:
    """
    args:
        o_i_t: state of i at time t
        o_j_t: state of j at time t
        Z: function

    returns: np.float128
    """
    return F(o_i_t, o_j_t) * G(o_i_t, o_j_t) + Z(o_i_t)
