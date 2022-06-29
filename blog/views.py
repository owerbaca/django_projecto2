from django.shortcuts import render

def site(request):
    return render (request , 'blog/index.html')