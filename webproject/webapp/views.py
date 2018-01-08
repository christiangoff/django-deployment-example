from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def mediaView(request):
    return render(request,'media.html')
