from django.shortcuts import render

def home(request):
    a = {}

    a["greeting"] = "hello world"

    return render(request, 'home.html', a)
