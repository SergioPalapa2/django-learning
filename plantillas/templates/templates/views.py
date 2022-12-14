from django.http import HttpResponse
#import datetime
from django.template import Template, Context


#USO DE PLANTILLAS

def saludo(request):#vista se declara como una funcion
    #saludo="""<html><body><h1>Hola mundito</h1></body></html>"""

    nombre='Sergio2' #variables

    doc_saludo=open("/home/eum/Documentos/Cursos/python/django/proyectos/django-learning/plantillas/templates/templates/plantillas_doc/plantilla1.html")
    

    plt=Template(doc_saludo.read())#objeto de tipo template
    doc_saludo.close() #cierre del documento
    #contexto (al momento vacio ya que no hay contenido dinamico)
    ctx=Context({"nombrep":nombre})
    documento=plt.render(ctx)
    return HttpResponse(documento)


#Uso de variables, objetos y propiedades en plantillas
