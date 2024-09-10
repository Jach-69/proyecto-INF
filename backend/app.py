
from flask import Flask, request, jsonify
import psycopg2
import urllib.parse
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# Escapar caracteres especiales en la contraseña
password = urllib.parse.quote_plus("admin")

# Configurar la conexión a la base de datos
conn = psycopg2.connect(
    f"postgresql://postgres:{password}@localhost/prueba2"
)

cursor = conn.cursor()


@app.route('/logedbd', methods=['POST'])
def logedbd():
    data = request.json
    nombre_usuario = data.get('nombre_usuario')
    password = data.get('password')

    print(f"Datos recibidos: nombre_usuario={nombre_usuario}, password={password}")

    if not nombre_usuario or not password:
        return jsonify({"status": "fail", "message": "Nombre de usuario y contraseña son requeridos"}), 400

    cursor.execute(
        "SELECT * FROM usuarios WHERE nombre_usuario = %s AND password = %s",
        (nombre_usuario, password)
    )
    result = cursor.fetchone()

    print(f"Resultado de la consulta: {result}")

    if result:
        return jsonify({"status": "success", "message": "Login exitoso"}), 200
    else:
        return jsonify({"status": "fail", "message": "Nombre de usuario o contraseña incorrectos"}), 401



@app.route('/accesos/<int:id>', methods=['GET'])
def get_acceso(id):
    cursor.execute("SELECT * FROM accesos WHERE id = %s", (id,))
    result = cursor.fetchone()
    
    if result:
        access = {
            'id': result[0],
            'clave': result[1],
            'tarjeta_rfid': result[2],
            'nombre_usuario': result[3],
            'fecha_hora': result[4]
        }
        return jsonify(access)
    else:
        return jsonify({"status": "fail", "message": "Acceso no encontrado"}), 404


@app.route('/accesos', methods=['GET'])
def get_accesses():
    cursor.execute("SELECT * FROM accesos")
    result = cursor.fetchall()
    
    accesses = []
    for row in result:
        access = {
            'id': row[0],
            'clave': row[1],
            'tarjeta_rfid': row[2],
            'nombre_usuario': row[3],
            'fecha_hora': row[4]
        }
        accesses.append(access)
    
    return jsonify(accesses)

@app.route('/accesos', methods=['POST'])
def create_access():
    data = request.json
    clave = data.get('clave')
    tarjeta_rfid = data.get('tarjeta_rfid')
    nombre_usuario = data.get('nombre_usuario')

    cursor.execute(
        "INSERT INTO accesos (clave, tarjeta_rfid, nombre_usuario) VALUES (%s, %s, %s) RETURNING id, fecha_hora",
        (clave, tarjeta_rfid, nombre_usuario)
    )
    conn.commit()
    access_id, fecha_hora = cursor.fetchone()
    
    return jsonify({'id': access_id, 'clave': clave, 'tarjeta_rfid': tarjeta_rfid, 'nombre_usuario': nombre_usuario, 'fecha_hora': fecha_hora}), 201


@app.route('/accesos/<int:id>', methods=['PUT'])
def update_acceso(id):
    data = request.json
    clave = data.get('clave')
    tarjeta_rfid = data.get('tarjeta_rfid')
    nombre_usuario = data.get('nombre_usuario')

    update_fields = []
    params = []

    if clave is not None:
        update_fields.append("clave = %s")
        params.append(clave)

    if tarjeta_rfid is not None:
        update_fields.append("tarjeta_rfid = %s")
        params.append(tarjeta_rfid)

    if nombre_usuario is not None:
        update_fields.append("nombre_usuario = %s")
        params.append(nombre_usuario)

    if not update_fields:
        return jsonify({"status": "fail", "message": "Debe proporcionar al menos un campo para actualizar"}), 400

    params.append(id)
    update_query = "UPDATE accesos SET " + ", ".join(update_fields) + " WHERE id = %s"

    try:
        cursor.execute(update_query, tuple(params))
        conn.commit()

        if cursor.rowcount > 0:
            return jsonify({"status": "success", "message": "Access updated"}), 200
        else:
            return jsonify({"status": "fail", "message": "No record found with the given ID"}), 404
    except Exception as e:
        conn.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/accesos/<int:id>', methods=['DELETE'])
def delete_access(id):
    cursor.execute("DELETE FROM accesos WHERE id = %s", (id,))
    conn.commit()
    
    return jsonify({'message': 'Acceso eliminado correctamente'}), 200

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    password = data.get('password')
    rfid = data.get('rfid')

    if not password and not rfid:
        return jsonify({"status": "fail", "message": "Debe proporcionar al menos una contraseña o un RFID"}), 400

    query = "SELECT * FROM accesos WHERE"
    params = []

    if password is not None:
        query += " clave = %s"
        params.append(password)

    if rfid is not None:
        if password is not None:
            query += " OR"
        query += " tarjeta_rfid = %s"
        params.append(rfid)

    cursor.execute(query, tuple(params))
    result = cursor.fetchone()

    if result:
        return jsonify({"status": "success", "message": "Access granted"}), 200
    else:
        return jsonify({"status": "fail", "message": "Access denied"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)