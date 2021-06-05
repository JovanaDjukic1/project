
from django.shortcuts import render
from .models import Video

# Create your views here.



# Create your views here.
def index(request):
    video=Video.objects.all()
    return render(request, "index.html", {"video":video})

#def index(request):
#    return render(request,"index.css")

def download(request):
    return render(request, 'download.html')

def history(request):
    return render(request, 'history.html')

def mvcarhitecture(request):
    return render(request, 'mvcarhitecture.html')

def functions(request):
    return render(request, 'functions.html')

def laravel8(request):
    return render(request, 'laravel8.html')

def composer(request):
    return render(request, 'composer.html')

def artisan(request):
    return render(request, 'artisan.html')

def other(request):
    return render(request, 'other.html')

def framework(request):
    return render(request, 'framework.html')

def php(request):
    return render(request, 'php.html')

def why(request):
    return render(request, 'why.html')

def support(request):
    return render(request, 'support.html')