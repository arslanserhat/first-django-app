import os, time


dir_path = os.path.dirname(os.path.realpath(__file__))

has_face = dir_path + '/static/has_face'
no_face = dir_path + '/static/no_face'
media = dir_path + '/media/result'

while True:
    print('File searching...')
    if os.listdir(has_face) or os.listdir(no_face) or os.listdir(media):
        print('File Founded ', 'Has Face: ' + str(os.listdir(has_face)), 'No Face: ' + str(os.listdir(no_face)))
        for the_file in os.listdir(has_face):
            file_path = os.path.join(has_face, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

        for the_file in os.listdir(no_face):
            file_path = os.path.join(no_face, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

        for the_file in os.listdir(media):
            file_path = os.path.join(media, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

    time.sleep(20)