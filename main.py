#!/usr/bin/env python3
import cv2
from project_file.utils.network import yolo
from project_file.utils.detector import detect
from project_file.utils.drawer import draw_boxes
import os, zipfile, time
import shutil


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

dir_path = os.path.dirname(os.path.realpath(__file__))

process_path = '/media/'

model_file = 'project_file/temp/checkpoints/latest.h5'


min_threshold = 0.5
model = yolo()

model.load_weights(model_file)


def predict(file):
    has_face = '/static/has_face/'
    no_face = '/static/no_face/'
    actual_file = dir_path + process_path + file
    image = cv2.imread(actual_file)
    image = cv2.resize(image, (416, 416))
    boxes, labels = detect(image, model)
    image = draw_boxes(image, boxes, labels)
    image = cv2.resize(image, (800, 600))


    result = False
    if len(boxes) > 0:
        for box in boxes:
            if box.label == 0:
                if box.score > 0.50:
                    result = True
    if result:
        shutil.move(actual_file, dir_path + has_face)
    else:
        shutil.move(actual_file, dir_path + no_face)


def run():
    extension = ".zip"

    os.chdir(dir_path + process_path)  # change directory from working dir to dir with files

    for item in os.listdir(dir_path + process_path):  # loop through items in dir
        if item.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(item)  # get full path of files
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(dir_path + process_path)  # extract file to dir
            zip_ref.close()  # close file
            os.remove(file_name)

    for file in os.listdir(dir_path + process_path):
        predict(file)

    if os.listdir(dir_path + '/static/no_face'):
        shutil.make_archive('noface', 'zip', dir_path + '/static/no_face/')

    if os.listdir(dir_path + '/static/has_face'):
        shutil.make_archive('hasface', 'zip', dir_path + '/static/has_face/')

def delete():
    print('çalıştım bebeğim')