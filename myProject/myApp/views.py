from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'myApp/main.html')

def contacto(request):
     return render(request, 'myApp/contacto.html')

def productos(request):
    return render(request, 'myApp/productos.html')