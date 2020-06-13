from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'secondapp/index.html')

def static_exmaple(request):
    return render(request,'secondapp/static_exmaple.html')