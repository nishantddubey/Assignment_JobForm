from django.shortcuts import render

# Create your views here.

def jobform(request):
    return render(request,'jobform.html')