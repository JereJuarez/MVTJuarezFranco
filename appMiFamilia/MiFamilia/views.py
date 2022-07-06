from django.shortcuts import render
from django.http import HttpResponse
from MiFamilia.models import familiares
from django.template import Context, Template 
from django.template import loader


# Create your views here.


def familiar1(self):

    familiar= familiares(nombre="Gustavo" ,edad="50" ,profesion="Comerciante" ,cuadro="Godoy Cruz" ,fecha_nacimiento="1972-03-27")
    familiar.save()
    documentoDeTexto = f"Nombre: {familiar.nombre}, Edad: {familiar.edad}, Profesión: {familiar.profesion}, Cuadro: {familiar.cuadro}, fecha de nacimiento: {familiar.fecha_nacimiento} "


    return HttpResponse(documentoDeTexto)

def familiar2(self):

    familiar= familiares(nombre="Ana" ,edad="48" ,profesion="Secretaria" ,cuadro="Boca" ,fecha_nacimiento="1973-12-12")
    familiar.save()
    documentoDeTexto = f"Nombre: {familiar.nombre}, Edad: {familiar.edad}, Profesión: {familiar.profesion}, Cuadro: {familiar.cuadro}, fecha de nacimiento: {familiar.fecha_nacimiento} "

    return HttpResponse(documentoDeTexto)

def familiar3(self):

    familiar= familiares(nombre="Maximiliano" ,edad="30" ,profesion="Misionero" ,cuadro="Boca" ,fecha_nacimiento="1991-08-29")
    familiar.save()
    documentoDeTexto = f"Nombre: {familiar.nombre}, Edad: {familiar.edad}, Profesión: {familiar.profesion}, Cuadro: {familiar.cuadro}, fecha de nacimiento: {familiar.fecha_nacimiento} "

    return HttpResponse(documentoDeTexto)

def familiar4(self):

    familiar= familiares(nombre="Jennifer" ,edad="29" ,profesion="Escribana" ,cuadro="River" ,fecha_nacimiento="1992-07-20")
    familiar.save()
    documentoDeTexto = f"Nombre: {familiar.nombre}, Edad: {familiar.edad}, Profesión: {familiar.profesion}, Cuadro: {familiar.cuadro}, fecha de nacimiento: {familiar.fecha_nacimiento} "

    return HttpResponse(documentoDeTexto)


def Templateinicio(request):

    miHtml=open("C:/Users/jere_/Desktop/MVT/appMiFamilia/tem/template1.html")

    plantilla=Template(miHtml.read())

    miHtml.close()

    miContexto= Context()

    documento= plantilla.render(miContexto)

    return HttpResponse(documento)

    



