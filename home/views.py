from django.shortcuts import render

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


    return render(request, 'home.html', context)