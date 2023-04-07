import numpy as np
from scipy.interpolate import lagrange


def lagrandge(x, y):
    # Интерполяционный многочлен Лагранжа
    poly = lagrange(x, y)
    print(poly)
    for co in reversed(range(len(poly) + 1)):
        print(poly[co], end=' ')


if __name__ == "__main__":
    x = np.array([0, 1, 2, 3])
    y = np.array([-2, -5, 0, -4])
    lagrandge(x, y)
