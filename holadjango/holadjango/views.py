from django.http import HttpResponse
import datetime

def saludo(request):#vista se declara como una funcion
    return HttpResponse("Hello MF, this is your first django project.")

def despedida(request):
    return HttpResponse("Goodbye MF.")

def index(request):
    pagina='''<html>
        <body>
            <h1>Django</h1>
            <h2>Parametros html</h2>
            <p>Las vistas/funciones pueden devolver codigo html como parametros en Httpreponse<p/>
        </body>
    </html>'''
    return HttpResponse(pagina) #recibe la variable con codigo html


def date(request):
    fecha=datetime.datetime.now()
    pagina='''<html>
        <body>
            <h1>Django</h1>
            <h2>Contenido dinamico</h2>
            <h3>Fecha y hora: %s </h3>  
            <p><p/>
        </body>
    </html>'''%fecha
    #%s marcadores de posición
    return HttpResponse(pagina) #recibe la variable con codigo html

def calcula_edad(request, edad, anio): #la vista recibe un parametro, que viaja por la URL
    #edad_actual=30
    periodo=anio-2022
    edaf=edad+periodo
    pagina='''<html>
        <body>
            <h1>Django</h1>
            <h2>Calculadora de edad</h2>
            <h3>En el año %s tendras %s años</h3>  
            <p><p/>
        </body>
    </html>'''%(anio, edaf)
    return HttpResponse(pagina)



    
#nota: Se enlaza una URL con esta vista(funcion) para poderla llamar. Archivo urls.py
#En el parametro htmlresponse es posible pasar etiquetas html



