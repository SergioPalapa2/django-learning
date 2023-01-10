from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader #cargador de plantillas metodo clave: loader.get_template

from django.shortcuts import render



#USO DE PLANTILLAS
class persona(object):#declaracion de objetos
        def __init__(self,nombre, apellido):
            self.nombre=nombre
            self.apellido=apellido

def saludo(request):#vista se declara como una funcion
    #saludo="""<html><body><h1>Hola mundito</h1></body></html>"""
    
    persona1=persona("Juanelo","Alimaña") #instanciacion de clase "persona"
    devMaster=persona("Sergio","Palapa")
    nombre='Sergio'
    apellido="Palapa"
    present=datetime.datetime.now() 
    temasC=["python","javascript","django"]
    #equiposC=[]
    equiposC=["gabinete","monitor","switch","regulador","impresora"]
    #con la nomenclatura . podemos acceder a las propiedades de los objetos


    ####carga de plantilla de forma manual####
    #doc_saludo=open("/home/eum/Documentos/Cursos/python/django/proyectos/django-learning/plantillas/templates/templates/plantillas_doc/plantilla1.html")
    #plt=Template(doc_saludo.read())#objeto de tipo template
    #doc_saludo.close() #cierre del documento

    ####carga de plantillas optimizado####
    doc_saludo=loader.get_template('plantilla1.html')
    #es posible cargar mas plantillas 


    #contexto (al momento vacio ya que no hay contenido dinamico)
    #ctx=Context({"nombrep":nombre,"apellidop":apellido,"actual":present})
    #Es posible pasar al contexto listas

    #ctx=Context({"nombrep":persona1.nombre,"apellidop":persona1.apellido,"actual":present,"temas":temasC,"equipos":equiposC,"nombreDev":devMaster.nombre,"apellidoDev":devMaster.apellido})
    

    ####renderizado de forma manual
    #documento=plt.render(ctx)

    ####renderizado de forma optima
    documento=doc_saludo.render({"nombrep":persona1.nombre,"apellidop":persona1.apellido,"actual":present,"temas":temasC,"equipos":equiposC,"nombreDev":devMaster.nombre,"apellidoDev":devMaster.apellido}) #metodo render es diferente, noa cepta contexto sino un diccionario

    return HttpResponse(documento)


def short(request):
    autor=persona('Sergio','Palapa')
    return render(request,"plantilla2.html") 


#Vistas heredadas
def herencia_ex(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "hija.html",{"dameFecha":fecha_actual})


def herencia_ex2(request):
    return render(request, "hija2.html")


#Uso de variables, objetos y propiedades en plantillas
