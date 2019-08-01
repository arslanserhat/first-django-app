from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import time, os

def home_view(request):

    if request.user.is_authenticated:
        context = {
            'isim': 'Serhat',
            'soyisim': 'Arslan'
        }
    else:
        context = {
            'isim': 'Misafir',
            'soyisim': 'Kullanıcı'
        }

    if request.method == 'POST':
        import main

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        start_time = time.time()
        main.run()
        end_time = time.time() - start_time
        print(round(end_time, 2))

        dir_path = os.path.abspath('../..')

        no_face = dir_path + '/static/no_face'
        has_face = dir_path + '/static/has_face'

        content = {
            'noface': os.listdir(no_face),
            'hasface': os.listdir(has_face),
            'noface_zip': '/media/result/noface.zip',
            'hasface_zip': '/media/result/hasface.zip',
        }

        return render(request, 'result.html', content)

    return render(request, 'home.html', context)


def index(request):

    if request.POST:
        print('çalış bebeğim')
        import delete

        delete.delete_items()

    return render(request,'result.html')

def api(request):
    import main

    myfile = request.GET.get('url', 'Not Found')


    result = main.api_url(myfile)

    print(result)


    return render(request, 'home.html')

