#!/usr/bin/env python3
import cv2
from project_file.utils.network import yolo
from project_file.utils.detector import detect
from project_file.utils.drawer import draw_boxes
import os
import time
import shutil


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

dir_path = os.path.dirname(os.path.realpath(__file__))
process_path = '/uploads/'

model_file = 'temp/checkpoints/latest.h5'


min_threshold = 0.5
model = yolo()

model.load_weights(model_file)


def predict(file):
    has_face = 'has_face/'
    no_face = 'no_face/'
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
    # print(result)
    if result:
        shutil.move(actual_file, has_face)
    else:
        shutil.move(actual_file, no_face)


def run():
    for file in os.listdir(dir_path + process_path):
        predict(file)

if __name__ == '__main__':

    start_time = time.time()
    run()
    end_time = time.time() - start_time
    print(round(end_time, 2))

