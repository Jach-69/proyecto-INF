from flask import Blueprint, request, jsonify
from models import cursor, conn

access_routes = Blueprint('access_routes', __name__)

@access_routes.route('', methods=['GET'])
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

@access_routes.route('', methods=['POST'])
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

@access_routes.route('/<int:id>', methods=['PUT'])
def update_access(id):
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

@access_routes.route('/<int:id>', methods=['DELETE'])
def delete_access(id):
    cursor.execute("DELETE FROM accesos WHERE id = %s", (id,))
    conn.commit()

    return jsonify({'message': 'Acceso eliminado correctamente'}), 200
