from django.shortcuts import render, render_to_response


def principal(request):
    return render_to_response ("html5up-hyperspace/index.html",locals())

def catalogo(request):
   return render(request, 'html5up-hyperspace/catalogo.html')

def diario(request):
   return render(request, "html5up-hyperspace/diario.html")

def empresa(request):
    return render(request, "html5up-hyperspace/empresa.html")

# Create your views here.
