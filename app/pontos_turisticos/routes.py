from flask import render_template, request, jsonify
from app.pontos_turisticos import bp
from app.extensions import MySQLDatabase
import mysql.connector

@bp.route("/pontos_turisticos/cadastrar")
def tela_cadastrar_pontos_turisticos():
    return render_template('telaCadastroPontos.html')

@bp.route("/pontos_turisticos", methods=['POST'])
def add_pontos_turisticos():
    data = request.json
    print("Data received from the request:", data)

    nome = request.json["nome"]
    descricao = request.json["descricao"]
    longitude = request.json["longitude"]
    latitude = request.json["latitude"]

    try:
        conn = MySQLDatabase.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO pontos_turisticos (nome, descricao, latitude, longitude) VALUES (%s, %s, %s, %s)', 
            (nome, descricao, latitude, longitude)
        )
        conn.commit()

        cursor.execute('SELECT LAST_INSERT_ID()')
        last_id = cursor.fetchone()[0]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            MySQLDatabase.close_connection(conn)

    return {'id': last_id}

@bp.route("/pontos_turisticos/listar")
def tela_listar_pontos_turisticos():

    lista_pontos_turisticos = get_pontos_turisticos()
    headers = ['ID', 'Nome', 'Descrição', 'Longitude', 'Latitude']

    return render_template(
        'telaListaPontos.html',
        headers=headers,
        lista_pontos_turisticos=lista_pontos_turisticos
    )

@bp.route("/pontos_turisticos", methods=['GET'])
def get_pontos_turisticos():    
    conn = MySQLDatabase.get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM pontos_turisticos')
    results = cursor.fetchall()
    cursor.close()
    MySQLDatabase.close_connection(conn)

    return results