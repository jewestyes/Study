import numpy as np
import os
import pathlib
import pylab
import cv2
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from tkinter import *
from tkinter.filedialog import askopenfilename
from numpy.polynomial.polynomial import Polynomial
from PIL import Image
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from interface import Ui_MainWindow

def show_luminance_in_section(path=None, name=None):
    y1, y2, x1, x2 = 0, 5, 0, 5
    img = cv2.imread(path, 1)
    # y2 = img.shape[0]
    # x2 = img.shape[1]

    cropped = img[int(y1):int(y2), int(x1):int(x2)]

    lab = cv2.cvtColor(cropped, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    values = []
    for c in range(l.shape[1]):
        count = 0
        for r in range(l.shape[0]):
            count += l[r][c]
        values.append(1.0 * count / l.shape[0])
    

    x = []
    for i in range(len(values)): x.append(i)
    poly = lagrange(x, values)

    x_new = np.arange(0, len(x), 0.1)
    res = []
    reversed_poly = poly.coef[::-1]

    for i in range(len(reversed_poly) - 1):
        res += i*reversed_poly[i]
    

    plt.scatter(x, values, label='data')
    plt.plot(x_new, Polynomial(res, label='Polynomial'))
    plt.plot(x, values,
         label=r"$func$", linestyle='-.')
    plt.legend()
    plt.show()
    


if __name__ == "__main__":
    show_luminance_in_section(rf"D:\Github\Study\1_compressed.jpg", "Red")
