from django.http import HttpResponse
import datetime
from django.template import Template, Context


#USO DE PLANTILLAS
class persona(object):#declaracion de objetos
        def __init__(self,nombre, apellido):
            self.nombre=nombre
            self.apellido=apellido

def saludo(request):#vista se declara como una funcion
    #saludo="""<html><body><h1>Hola mundito</h1></body></html>"""
    
    persona1=persona("Juanelo","Alimaña") #instanciacion de clase "persona"

    nombre='Sergio' #variables
    apellido="Palapa"
    present=datetime.datetime.now() 
    
    


    #con la nomenclatura . podemos acceder a las propiedades de los objetos



    doc_saludo=open("/home/eum/Documentos/Cursos/python/django/proyectos/django-learning/plantillas/templates/templates/plantillas_doc/plantilla1.html")
    

    plt=Template(doc_saludo.read())#objeto de tipo template
    doc_saludo.close() #cierre del documento
    #contexto (al momento vacio ya que no hay contenido dinamico)
    #ctx=Context({"nombrep":nombre,"apellidop":apellido,"actual":present})
    ctx=Context({"nombrep":persona1.nombre,"apellidop":persona1.apellido,"actual":present})
    documento=plt.render(ctx)
    return HttpResponse(documento)


#Uso de variables, objetos y propiedades en plantillas
