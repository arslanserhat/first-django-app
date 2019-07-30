from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import time, os

# Create your views here.
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

        dir_path = os.path.abspath('..')

        no_face = dir_path + '/static/no_face'
        has_face = dir_path + '/static/has_face'

        content = {
            'uploaded_file_url': uploaded_file_url,
            'hasface': os.listdir(has_face),
            'noface': os.listdir(no_face),
            'noface_zip': '/media/noface.zip',
            'hasface_zip': '/media/hasface.zip',
        }

        return render(request, 'result.html', content)

    return render(request, 'home.html', context)

def result_page(request):

    if request.GET.get('result'):
        import  main

        main.delete()

    content = {
        'sa': 'selam bebeğim'
    }

    return render(request, 'result.html', content)