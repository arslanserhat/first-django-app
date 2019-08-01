import urllib
import string
import random
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def get_remote_image():
    filename_charset = string.ascii_letters + string.digits
    filename_length = 10
    file_save_dir = dir_path + '/media/'

    filename = ''.join(random.choice(filename_charset) for s in range(filename_length))

    urllib.urlretrieve("http://www.example.com/image.png",os.path.join(file_save_dir, filename + '.png'))