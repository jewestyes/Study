import numpy as np
import os
import pathlib
import pylab
import cv2

from tkinter import *
from tkinter.filedialog import askopenfilename
from scipy.interpolate import lagrange
from PIL import Image
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from interface import Ui_MainWindow

def show_luminance_in_section(path=None, name=None):
    y1, y2, x1, x2 = 0, 10, 0, 10
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
    for i in range(len(values)):
        print(f"{i} {values[i]}")
        x.append(i)
    
    poly = lagrandge(x, values)

    pylab.figure(name)
    pylab.ylabel('Interpolating polynomial')
    pylab.xlabel('X axis')
    pylab.plot(x, poly[0], color=name)

    pylab.ylabel('Average Luminance')
    pylab.xlabel('X axis')
    pylab.plot(values, color="Blue")

    pylab.show()


def lagrandge(x, y):
    # Интерполяционный многочлен Лагранжа
    poly = lagrange(x, y)
    poly_reversed = []
    for co in reversed(range(len(poly) + 1)):
        poly_reversed.append(poly[co])
    return poly, poly_reversed


if __name__ == "__main__":
    show_luminance_in_section(rf"C:\Users\ggezj\PycharmProjects\Study\images\4.jpg", "Red")
