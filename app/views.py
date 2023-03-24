from django.shortcuts import render

# Create your views here.
def bgimage(request):
    return render(request,'bgimage.html')