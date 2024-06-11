import os
import pathlib
import cv2
import pylab

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from interface import Ui_MainWindow

def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def initialize_rgb_buttons():
    ui.red_luminosity_button.setStyleSheet("background-color: red")
    ui.green_luminosity_button.setStyleSheet("background-color: green")
    ui.blue_luminosity_button.setStyleSheet("background-color: blue")
    ui.red_luminosity_button.setEnabled(True)
    ui.green_luminosity_button.setEnabled(True)
    ui.blue_luminosity_button.setEnabled(True)


def compress_img():
    new_size_ratio = float(ui.resize_slider.value() / 100)
    quality = ui.quality_slider_2.value()
    width = int(ui.width_edit_line.text()) if ui.width_edit_line.text() else None
    height = int(ui.height_edit_line.text()) if ui.height_edit_line.text() else None
    to_jpg = ui.jpg_checkBox_2.isChecked()

    img = Image.open(image_path)

    original_text_log = [f"Image shape: {img.size}"]
    compressed_text_log = []

    image_size = os.path.getsize(image_path)
    original_text_log.append(f"Size before compression: {get_size_format(image_size)}")
    if new_size_ratio < 1.0:
        # if resizing ratio is below 1.0, then multiply width & height with this ratio to reduce image size
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.LANCZOS)
        compressed_text_log.append(f"New Image shape: {img.size}")
    elif width and height:
        img = img.resize((width, height), Image.ANTIALIAS)
        compressed_text_log.append(f"New Image shape: {img.size}")

    global new_filename
    filename, ext = os.path.splitext(image_path)
    if to_jpg:
        new_filename = f"{filename}_compressed.jpg"
    else:
        new_filename = f"{filename}_compressed{ext}"
    try:
        img.save(new_filename, quality=quality, optimize=True)
    except OSError:
        img = img.convert("RGB")
        img.save(new_filename, quality=quality, optimize=True)
    new_image_size = os.path.getsize(new_filename)
    compressed_text_log.append(f"Size after compression: {get_size_format(new_image_size)}")
    saving_diff = new_image_size - image_size
    compressed_text_log.append(f"Image size change: {saving_diff / image_size * 100:.2f}% of the original image size.")

    orig_text = ""
    for i in range(len(original_text_log)):
        orig_text += str(original_text_log[i]) + "\n"
    ui.original_photo_info_2.setText(orig_text)

    compressed_text = ""
    for i in range(len(compressed_text_log)):
        compressed_text += str(compressed_text_log[i]) + "\n"
    ui.compressed_photo_info_2.setText(compressed_text)

    ui.compressed_photo.setPixmap(QtGui.QPixmap(new_filename))
    extract_rgb_channels()
    initialize_rgb_buttons()
    ui.photo_red_2.setPixmap(QtGui.QPixmap(red_img_path))
    ui.photo_green_2.setPixmap(QtGui.QPixmap(green_img_path))
    ui.photo_blue_2.setPixmap(QtGui.QPixmap(blue_img_path))


def show_red_luminance():
    show_luminance_in_section(red_img_path, "Red")


def show_green_luminance():
    show_luminance_in_section(green_img_path, "Green")


def show_blue_luminance():
    show_luminance_in_section(blue_img_path, "Blue")


def show_luminance_in_section(path=None, name=None):
    y1, y2, x1, x2 = 0, 0, 0, 0
    img = cv2.imread(path, 1)
    try:
        match name:
            case "Red":
                y1, y2 = ui.red_height_lineEdit_2.text().split(',')
                x1, x2 = ui.red_height_lineEdit_2.text().split(',')
            case "Green":
                y1, y2 = ui.green_height_lineEdit.text().split(',')
                x1, x2 = ui.green_width_lineEdit.text().split(',')
            case "Blue":
                y1, y2 = ui.blue_height_lineEdit.text().split(',')
                x1, x2 = ui.blue_height_lineEdit.text().split(',')
    except Exception:
        y2 = img.shape[0]
        x2 = img.shape[1]

    cropped = img[int(y1):int(y2), int(x1):int(x2)]
    is_success, im_buf_arr = cv2.imencode(".jpg", cropped)
    byte_im = im_buf_arr.tobytes()

    dir_path = pathlib.PurePath(path)

    try:
        with open(rf"{dir_path.parents[0]}/{name}.txt", 'wb') as binary_file:
            binary_file.write(byte_im)
    except FileNotFoundError:
        print("The directory does not exist")
    lab = cv2.cvtColor(cropped, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

    values = []
    for c in range(l.shape[1]):
        values.append(1.0 * l.shape[0])

    pylab.figure(name)
    pylab.ylabel('Average Luminance')
    pylab.xlabel('X axis')
    pylab.plot(values, 'k-', color=name)
    cv2.imshow(f"{name} cropped image", cropped)
    pylab.show()


def extract_rgb_channels():
    newfile = os.path.splitext(new_filename)
    src = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    global red_img_path, green_img_path, blue_img_path

    red_img_path = f"{newfile[0]}red-channel.jpg"
    green_img_path = f"{newfile[0]}green-channel.jpg"
    blue_img_path = f"{newfile[0]}blue-channel.jpg"

    red_channel = src[:, :, 2]
    green_channel = src[:, :, 1]
    blue_channel = src[:, :, 0]

    cv2.imwrite(red_img_path, red_channel)
    cv2.imwrite(green_img_path, green_channel)
    cv2.imwrite(blue_img_path, blue_channel)


def enable_widgets():
    ui.compressButton.setEnabled(True)
    ui.resize_slider.setEnabled(True)
    ui.quality_slider_2.setEnabled(True)
    ui.jpg_checkBox_2.setEnabled(True)
    ui.height_edit_line.setEnabled(True)
    ui.width_edit_line.setEnabled(True)


def open_file():
    global image_path
    Tk().withdraw()
    ui.actionOpen_File.setEnabled(False)
    image_path = askopenfilename(initialdir="/images",
                                 title="Select A File",
                                 filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("All files", "*.*")))
    ui.actionOpen_File.setEnabled(True)
    if image_path:
        ui.original_photo.setPixmap(QtGui.QPixmap(image_path))
        enable_widgets()
        ui.original_photo_info_2.setText('')
        ui.compressed_photo_info_2.setText('')
        ui.compressed_photo.setPixmap(QtGui.QPixmap(''))
        only_int = QIntValidator()
        ui.height_edit_line.setValidator(only_int)
        ui.width_edit_line.setValidator(only_int)


def actions():
    ui.actionOpen_File.triggered.connect(open_file)
    ui.compressButton.clicked.connect(compress_img)
    ui.quality_slider_2.valueChanged[int].connect(quality_change_value)
    ui.resize_slider.valueChanged[int].connect(resizing_change_value)

    ui.red_luminosity_button.clicked.connect(show_red_luminance)
    ui.green_luminosity_button.clicked.connect(show_green_luminance)
    ui.blue_luminosity_button.clicked.connect(show_blue_luminance)


def quality_change_value(value):
    ui.quality_label_2.setText(f"Quality: {value}")


def resizing_change_value(value):
    ui.resize_label.setText(f"Resizing ratio: {value}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    actions()

    MainWindow.show()
    sys.exit(app.exec_())
