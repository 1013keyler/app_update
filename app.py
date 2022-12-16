from flask import Flask, render_template, request, redirect
import sqlite3 as sql
from funciones import get_db, consultar
from datetime import datetime, timedelta
import json

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/parque_tayrona')
def parque():
    return render_template('parque_tayrona.html')

@app.route('/santa_marta')
def san():
    return render_template('santa_marta.html')

@app.route('/minca')
def minca():
    return render_template('minca.html')

@app.route('/ciudad_perdida')
def ciu():
    return render_template('ciudad_perdida.html')

@app.route('/palomino')
def palo():
    return render_template('palomino.html')

@app.route('/tours')
def tour():
    return render_template('tours.html')

@app.route('/playa_blanca')
def playa():
    return render_template('Playa_Blanca.html')

@app.route('/cabo_sanjuan')
def cabo():
    return render_template('cabo_sanjuan.html')

@app.route('/pozo_azul')
def pozo():
    return render_template('pozo_azul.html')

@app.route('/untitled')
def resultado():
    return render_template('untitled.html')

@app.route('/categoria')
def busqueda():
    return render_template('categorias.html')

@app.route('/compra', methods=['POST', 'GET'])
def compra():
    if request.method == 'POST':
        valor = request.form['valor']
        destino = request.form['destino']
        today = datetime.now()+timedelta(days=+15)
        day= datetime.now()+timedelta(days=+90)
        diam = day.day
        mesm = day.month
        añom = day.year
        año = today.year
        mes = today.month
        dia = today.day
        print(f"mes {mes}")
        numeros = [1,2,3,4,5,6,7,8,9]
        if dia in numeros:
            dia = f"0{dia}"
        if mes in numeros:
            mes = f"0{mes}"
        if diam in numeros:
            diam = f"0{diam}"
        if mesm in numeros:
            mesm = f"0{mesm}"
        fecha_max = f"{day.year}-{mesm}-{diam}"
        fecha_min = f"{año}-{mes}-{dia}"
        print(fecha_max)
        print(fecha_min)
        return render_template('pagos.html', costo = valor, lugar = destino, min = fecha_min, max = fecha_max)

@app.route('/buscar', methods=['POST'])
def buscar():
    sitioprevio = request.form['caja_buscar']
    sitio = sitioprevio.upper()
    if sitio == 'SANTA MARTA':
        direccion = '/santa_marta'
    elif sitio == 'MINCA':
        direccion = '/minca'
    elif sitio == 'PLAYA BLANCA':
        direccion = '/playa_blanca'
    elif sitio == 'CABO SAN JUAN':
        direccion = '/cabo_sanjuan'
    elif sitio == 'POZO AZUL':
        direccion = '/pozo_azul'
    elif sitio == 'CIUDAD PERDIDA':
        direccion = '/ciudad_perdida'
    elif sitio == 'PALOMINO':
        direccion = '/palomino'
    elif sitio == 'PARQUE TAYRONA':
        direccion = '/parque_tayrona'
    return redirect(direccion)

@app.route('/recomendacion', methods=['POST'])
def recomendar():

    naturaleza = 'no'
    caminata = 'no'
    montaña =  'no'
    cultura = 'no'
    playa = 'no'


    if 'naturaleza' in request.form:
        naturaleza = request.form['naturaleza']
    if 'caminata' in request.form:
        caminata = request.form['caminata']
    if 'montaña' in request.form:
        montaña = request.form['montaña']
    if 'cultura' in request.form:
        cultura = request.form['cultura']
    if 'playa' in request.form:
        playa = request.form['playa']

    categorias = [naturaleza, caminata, montaña, cultura, playa]
    lista = consultar("select lugar, naturaleza, caminata, montaña, cultura, playa from destinos")
    print(lista)
    sitios = []
    if categorias != ['no','no','no','no','no']:
        aciertomayor = 0
        for i in lista:
            aciertos = 0
            for a in range(len(categorias)):
                if 'si' == i[a+1]:
                    aciertos += 1
            if aciertos >= aciertomayor:
                aciertomayor = aciertos
                sitios.append(i[0])
                print(i[0], aciertos)
    if len(sitios) > 2:
        print(sitios[:3])
        sitios = sitios[:3]
    return render_template('recomendacion.html', destinos = sitios, cantidad = len(sitios))


@app.route('/tours')
def tours():
    return render_template('tours.html')

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    return output

@app.route('/pagar', methods=['POST'])
def pagar():
    cupos = request.form['cupos']
    comprador = request.form['comprador']
    fecha = request.form['fecha']
    costo = request.form['costo']
    destino = request.form['destino']
    cupos = int(cupos)
    costo = int(costo)
    pago = costo*cupos
    print(type(cupos))
    print(type(costo))
    return render_template('pagar.html', date = fecha, personas = cupos, cliente = comprador, pagar = pago, lugar = destino)

if __name__ == "__main__":
    app.run(debug=True)