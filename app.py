"""
Examen Unidad III 
Autor: Emmanuel Alvarez Giles
Fecha: 29 de Octubre de 2025

Descripción:
Objetivo del examen
Desarrollar una API básica con Flask que permita:

Crear un diccionario de dispositivos de red.
Agregar nuevos dispositivos.
Modificar dispositivos existentes.
Mostrar un listado de todos los dispositivos en formato HTML, 
donde cada dispositivo se muestre en un <div> con nombre, 
descripción y características

Requisitos técnicos

Usar Flask.
Usar un diccionario como estructura principal de almacenamiento.
Implementar al menos tres rutas:

GET /dispositivos_html: muestra todos los dispositivos en HTML.
POST /dispositivos: agrega un nuevo dispositivo.
PUT /dispositivos/<id>: modifica un dispositivo existente.

Ejemplo del Diccionario de dispositivos: 
{
  "id": "router01",
  "nombre": "Router Principal",
  "descripcion": "Router de borde para salida a Internet",
  "ip": "192.168.1.1",
  "mac": "00:1A:2B:3C:4D:5E",
  "ubicacion": "Sala de servidores",
  "tipo": "Router",
  "otros": ""
}

Recuerda tener al menos 3 commits en tu repositorio. 

Para puntos extra
Puedes ocupar css para añadir puntos a tu examen, perzonalizalo con estilos como el siguiente:
<style>
    .dispositivo {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px;
    }
</style>

Puntos extra para añador formula en el cmapo de otros
la formula es la siguente: 

último octeto de la IP * 3 + longitud del nombre del dispositivo + ":" + nombre (Cambiando los espacios por _)

"""
from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)


@app.route('/dispositivos_html', methods=['GET'])
def dispositivos_html():
    template = '''
    <!doctype html>
    <html lang="es">
    <head>
      <meta charset="utf-8">
      <title>Dispositivos</title>
    </head>
    <body>
      <h1>Listado de dispositivos</h1>
      {% for d in dispositivos %}
        <div class="dispositivo">
          <h2>{{ d.nombre }} ({{ d.id }})</h2>
          <p><strong>Descripción:</strong> {{ d.descripcion }}</p>
          <p><strong>IP:</strong> {{ d.ip }} &nbsp; <strong>MAC:</strong> {{ d.mac }}</p>
          <p><strong>Ubicación:</strong> {{ d.ubicacion }} &nbsp; <strong>Tipo:</strong> {{ d.tipo }}</p>
          <p><strong>Otros:</strong> {{ d.otros }}</p>
        </div>
      {% else %}
        <p>No hay dispositivos registrados.</p>
      {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(template, dispositivos=list(devices.values()))


@app.route('/dispositivos', methods=['POST'])
def add_dispositivo():
    if not request.is_json:
        return jsonify({"error": "Se requiere JSON"}), 400
    data = request.get_json()
    if 'id' not in data:
        return jsonify({"error": "Falta campo 'id'"}), 400
    device_id = data['id']
    if device_id in devices:
        return jsonify({"error": "Dispositivo con ese id ya existe"}), 400
    device = {
        'id': device_id,
        'nombre': data.get('nombre', ''),
        'descripcion': data.get('descripcion', ''),
        'ip': data.get('ip', ''),
        'mac': data.get('mac', ''),
        'ubicacion': data.get('ubicacion', ''),
        'tipo': data.get('tipo', ''),
        'otros': data.get('otros', '')
    }
    devices[device_id] = device
    return jsonify(device), 201


if __name__ == '__main__':
    app.run(debug=True)