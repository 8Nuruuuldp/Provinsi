import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import flash, request

from werkzeug.security import generate_password_hash, check_password_hash

def my_function(connect):
    cursor = connect.cursor()
    # execute SQL query using cursor object

@app.route('/api/provinsi', methods=['POST'])
def add_provinsi():
    if request.method == 'POST':
        nama = request.json['nama']
        cursor = mysql.connect.cursor()
        cursor.execute("INSERT INTO t_provinsi (nama) VALUES (%s)", [nama])
        mysql.connect.commit()
        cursor.close()
        return jsonify({'message': 'Data provinsi berhasil ditambahkan'})

# Read
@app.route('/api/provinsi', methods=['GET'])
def get_provinsi():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM t_provinsi")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

# Update
@app.route('/api/provinsi/<int:id>', methods=['PUT'])
def update_provinsi(id):
    if request.method == 'PUT':
        nama = request.json['nama']
        cursor = mysql.connect.cursor()
        cursor.execute("UPDATE t_provinsi SET nama=%s WHERE id=%s", (nama, id))
        mysql.connect.commit()
        cursor.close()
        return jsonify({'message': 'Data provinsi berhasil diupdate'})

# Delete
@app.route('/api/provinsi/<int:id>', methods=['DELETE'])
def delete_provinsi(id):
    if request.method == 'DELETE':
        cursor = mysql.connect.cursor()
        cursor.execute("DELETE FROM t_provinsi WHERE id=%s", [id])
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Data provinsi berhasil dihapus'})

if __name__ == '__main__':
    app.run(debug=True)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
if __name__ == "__main__":
    app.run()
