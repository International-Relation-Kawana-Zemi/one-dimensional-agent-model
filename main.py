import numpy as np

def update(array: np.ndarray) -> np.ndarray:
    pass

def main():
    _mu, _sigma = np.float128(0), np.float128(10)
    opinion_vector = np.random.normal(_mu, _sigma, size=100)
    _size: int = len(opinion_vector)
    print(_size)


if __name__ == "__main__":
    main()
