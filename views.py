from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def store(request):
    return render(request,'core/store.html')

def contact(request):
    return render(request,'core/contact.html')



    