from django.shortcuts import render
from .models import RegistroCovid, InfoAutores
from django.db.models import Avg
from django.db.models.aggregates import StdDev
from collections import Counter

# Create your views here.


def home(request):
    return render(request, 'index.html')


def acerca(request):
    info = InfoAutores.objects.get(id=1)
    info_autor = {'infomacion': info}
    print(info)
    return render(request, 'acerca.html', info_autor)


def subida(request):
    return render(request, 'subida.html')


def mortalidad(request):
    mujeres_f = RegistroCovid.objects.filter(Sexo='F').filter(Estado='Fallecido').count()
    hombres_f = RegistroCovid.objects.filter(Sexo='M').filter(Estado='Fallecido').count()
    total_gente = RegistroCovid.objects.all().count()
    total_muertos = mujeres_f + hombres_f

    mortalidad_feme = round(((mujeres_f / total_muertos) * 100), 2)
    mortalidad_mascu = round(((hombres_f / total_muertos) * 100), 2)
    mor_gente = {'mortal_femenina': mortalidad_feme, 'mortal_masculina': mortalidad_mascu, 'tot_muer':total_muertos}

    return render(request, 'mortalidad.html', mor_gente)


def diagramapastel(request):
    ############## Porcentaje para el grafico de pie leve, moderado, grave, fallecido ####################
    total_gente = RegistroCovid.objects.all().count()

    #  Se genera búsqueda de Leves para minúscula y mayúscula, ya que existen entro de la db
    Leves = RegistroCovid.objects.filter(Estado='Leve').count()
    leves = RegistroCovid.objects.filter(Estado='leve').count()
    leves_total = Leves + leves

    moderados = RegistroCovid.objects.filter(Estado='Moderados').count()
    graves = RegistroCovid.objects.filter(Estado='Grave').count()
    fallecidos = RegistroCovid.objects.filter(Estado='Fallecido').count()
    NA = RegistroCovid.objects.filter(Estado='N/A').count()

    leves_porc = round(((leves_total / total_gente) * 100), 2)
    moderados_porc = round(((moderados / total_gente) * 100), 2)
    graves_porc = round(((graves / total_gente) * 100), 2)
    fallecidos_porc = round(((fallecidos / total_gente) * 100), 2)
    NA_porc = round(((NA / total_gente) * 100), 2)

    porcentajes = {'leves': leves_porc, 'moderados': moderados_porc, 'graves': graves_porc, 'fallecidos': fallecidos_porc, 'NA': NA_porc}

    return render(request, 'diagramapastel.html', porcentajes)


def media_desvistd(request):
    ############### media ##########################

    # Se categorizará con la edad, ya que en los datos no hay fallecidos con edad en meses o dias
    # Si existiera el caso se genera el filtro primero en promedio de fallecidos con años
    # Luego el promedio de fallecidos con edad en meses
    # Por ultimo fallecidos con edad en dias

    #  años unidad_de_edad == "1"
    dic_promedio_anos = RegistroCovid.objects.filter(Unidad_de_edad='1').filter(Estado='Fallecido').aggregate(Avg('Edad'))
    Edad_promedio_anos = (dic_promedio_anos['Edad__avg'])

    #  meses unidad_de_edad == "2"
    dic_promedio_meses = RegistroCovid.objects.filter(Unidad_de_edad='2').filter(Estado='Fallecido').aggregate(Avg('Edad'))
    Edad_promedio_meses = (dic_promedio_meses['Edad__avg'])
    if Edad_promedio_meses is None:
        Edad_promedio_meses = 0

    #  dias unidad_de_edad == "3"
    dic_promedio_dias = RegistroCovid.objects.filter(Unidad_de_edad='3').filter(Estado='Fallecido').aggregate(Avg('Edad'))
    Edad_promedio_dias = (dic_promedio_dias['Edad__avg'])
    if Edad_promedio_dias is None:
        Edad_promedio_dias = 0

    media_edad_fallecidos = round((Edad_promedio_anos + Edad_promedio_meses / 12 + Edad_promedio_dias / 365))

    ################ desviacion estandar ###############
    dic_desv_anos = RegistroCovid.objects.filter(Unidad_de_edad='1').filter(Estado='Fallecido').aggregate(StdDev('Edad'))
    desv_anos = (dic_desv_anos['Edad__stddev'])

    dic_desv_meses = RegistroCovid.objects.filter(Unidad_de_edad='2').filter(Estado='Fallecido').aggregate(StdDev('Edad'))
    desv_meses = (dic_desv_meses['Edad__stddev'])
    if desv_meses is None:
        desv_meses = 0

    dic_desv_dias = RegistroCovid.objects.filter(Unidad_de_edad='3').filter(Estado='Fallecido').aggregate(StdDev('Edad'))
    desv_dias = (dic_desv_dias['Edad__stddev'])
    if desv_dias is None:
        desv_dias = 0

    desv_edad_fallecidos = round((desv_anos + desv_meses / 12 + desv_dias / 365), 2)

    total_gente = RegistroCovid.objects.all().count()

    media_desvi = {'media': media_edad_fallecidos, 'desviacion': desv_edad_fallecidos, 'gente':total_gente}

    return render(request, 'media_desvistd.html', media_desvi)

def mayorescasos(request):
    municipios = []
    mun = 0
    contaditos = 0
    contaditos3_mayores = 0

    Registro_aux = RegistroCovid.objects.all()
    for elemento in Registro_aux:
        if elemento.Nombre_Municipio is not None:
            mun = elemento.Nombre_Municipio
            municipios.append(mun)

    contaditos = Counter(municipios)  # Organizo mediante el conteo
    contaditos3_mayores = contaditos.most_common(3)  # Se utiliza most_common de la libreria counter con arg 3
    # Sale 3 tuplas el resultado
    ciudad1 = contaditos3_mayores[0][0]
    casos1 = contaditos3_mayores[0][1]

    ciudad2 = contaditos3_mayores[1][0]
    casos2 = contaditos3_mayores[1][1]

    ciudad3 = contaditos3_mayores[2][0]
    casos3 = contaditos3_mayores[2][1]

    mayores = {'ciudad1': ciudad1, 'casos1': casos1, 'ciudad2': ciudad2, 'casos2': casos2, 'ciudad3': ciudad3, 'casos3':casos3}

    return render(request, 'mayorescasos.html', mayores)

def menorescasos(request):
    municipios = []
    mun = 0
    contaditos = 0

    Registro_aux = RegistroCovid.objects.all()
    for elemento in Registro_aux:
        if elemento.Nombre_Municipio is not None:
            mun = elemento.Nombre_Municipio
            municipios.append(mun)

    contaditos = Counter(municipios)  # Organizo mediante el conteo

    contaditos3_menores_ultimo = contaditos.most_common()[-1]
    contaditos3_menores_penultimo = contaditos.most_common()[-2]
    contaditos3_menores_antepenultimo = contaditos.most_common()[-3]
    contaditos3_menores = contaditos3_menores_ultimo + contaditos3_menores_penultimo + contaditos3_menores_antepenultimo

    ciudad1 = contaditos3_menores_ultimo[0]
    casos1 = contaditos3_menores_ultimo[1]

    ciudad2 = contaditos3_menores_penultimo[0]
    casos2 = contaditos3_menores_penultimo[1]

    ciudad3 = contaditos3_menores_antepenultimo[0]
    casos3 = contaditos3_menores_antepenultimo[1]

    menores = {'ciudad1': ciudad1, 'casos1': casos1, 'ciudad2': ciudad2, 'casos2': casos2, 'ciudad3': ciudad3, 'casos3':casos3}

    return render(request, 'menorescasos.html', menores)

def promrecuperacion(request):
    ################## Tiempo medio de recuperación #########################
    deltas = []
    contador = 0
    Registro_aux = RegistroCovid.objects.all()
    # Saco las fechas a una lista
    for elemento in Registro_aux:
        if elemento.Fecha_recuperacion is not None and elemento.Fecha_sintomas is not None and elemento.Recuperado != 'Fallecido' and elemento.Recuperado != 'N/A':
            delta = elemento.Fecha_recuperacion - elemento.Fecha_sintomas
            deltas.append(delta)

    media_recuperacion_aux = deltas[0]
    contador1 = len(deltas)

    while contador1 > 0:
        media_recuperacion_aux = media_recuperacion_aux + deltas[contador]
        contador1 -= 1
        contador += 1

    media_recuperacion_final = media_recuperacion_aux - deltas[0]
    media_recuperacion_final = media_recuperacion_final / len(deltas)

    horas = round((media_recuperacion_final.seconds/3600),)

    recuper = {'recuperacion': media_recuperacion_final, 'horas': horas, 'tot_recupe': len(deltas)}

    return render(request, 'promrecuperacion.html', recuper)


def prommuerte(request):
    ################## Tiempo medio de muerte #########################
    deltas_muerte = []
    contador = 0
    Registro_aux = RegistroCovid.objects.all()
    # Saco las fechas a una lista

    for regis in Registro_aux:
        if regis.Fecha_muerte is not None and regis.Fecha_sintomas is not None and regis.Recuperado != 'N/A' and regis.Recuperado != 'Recuperado':
            delta = regis.Fecha_muerte - regis.Fecha_sintomas
            deltas_muerte.append(delta)

    media_muerte_aux = deltas_muerte[0]
    contador1 = len(deltas_muerte)

    while contador1 > 0:
        media_muerte_aux = media_muerte_aux + deltas_muerte[contador]
        contador1 -= 1
        contador += 1

    media_muerte_final = media_muerte_aux - deltas_muerte[0]
    media_muerte_final = media_muerte_final / len(deltas_muerte)
    horas = round((media_muerte_final.seconds / 3600), )

    muer = {'muerte': media_muerte_final, 'horas': horas, 'tot_muertos': len(deltas_muerte)}

    return render(request, 'prommuerte.html', muer)