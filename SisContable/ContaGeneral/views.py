from django.shortcuts import render, render_to_response


def principal(request):
    return render_to_response ("html5up-hyperspace/index.html",locals())

def catalogo(request):
   return render ("html5up-hyperspace/catalogo.html",locals())


# Create your views here.
