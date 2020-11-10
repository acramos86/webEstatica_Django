from django.http import HttpResponse
from django.template import loader

def inicio(request):
    
    documento = loader.get_template('index.html')
    docRender = documento.render()
    return HttpResponse(docRender)

def talleres(request):
    
    documento = loader.get_template('talleres.html')
    docRender = documento.render()
    return HttpResponse(docRender)

def incubadora(request):

    documento = loader.get_template('incubadora.html')
    docRender = documento.render()
    return HttpResponse(docRender)

def duda(request):

    documento = loader.get_template('duda.html')
    docRender = documento.render()
    return HttpResponse(docRender)

def solDirecto(request):
    documento = loader.get_template('solDirecto.html')
    docRender = documento.render()
    return HttpResponse(docRender)

def humeda(request):
    documento = loader.get_template('humeda.html')
    docRender = documento.render()
    return HttpResponse(docRender)

def guias(request):
    documento = loader.get_template('guias.html')
    docRender = documento.render()
    return HttpResponse(docRender)

def cuidados(request):
    documento = loader.get_template('cuidados.html')
    docRender = documento.render()
    return HttpResponse(docRender)