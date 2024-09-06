from app.extensions import MySQLDatabase
from app.models.ponto_turistico import PontoTuristico
from flask import jsonify
import mysql.connector


class DAO_Pontos_Turisticos:
    def create_connection(self) -> mysql.connector.connection_cext.CMySQLConnection:
        return MySQLDatabase.get_db_connection()
    
    def close_connection(self, conn) -> None:
        MySQLDatabase.close_connection(conn)

    def get_pontos_turisticos(self) -> list:
        conn = self.create_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM pontos_turisticos')
        results = cursor.fetchall()
        cursor.close()
        self.close_connection(conn)

        return results
    
    def get_pontos_turisticos_by_id(self, ids) -> list:
        conn = self.create_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM pontos_turisticos WHERE id IN ("
        for id in ids:
            query += f"{id},"
        query = query[:-1] + ");"

        print(query)

        cursor.execute(query)
        results = cursor.fetchall()
        
        cursor.close()
        self.close_connection(conn)
        
        return_value = {
            row['id']: {
                "latitude": row['latitude'], 
                "longitude": row['longitude']
            } 
            for row in results
        }
        return jsonify(return_value)
    
    def delete_ponto_turistico(self, target_ponto_turistico: PontoTuristico):
        return_value = None
        query = 'DELETE FROM pontos_turisticos WHERE id=%s'

        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(query, (target_ponto_turistico.id, ))
            conn.commit()
        except mysql.connector.Error as err:
            return_value = jsonify({'message': err}), 400
        else:
            return_value = jsonify({'message': f'ID {target_ponto_turistico.id} deletado'}), 200
        
        if cursor: 
            cursor.close()
        if conn:
            self.close_connection(conn)

        return return_value

    def insert_ponto_turistico(self, target_ponto_turistico: PontoTuristico):
        return_value = None
        query = 'INSERT INTO pontos_turisticos (nome, descricao, latitude, longitude) VALUES (%s, %s, %s, %s)'

        try:
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(query, (
                target_ponto_turistico.nome,
                target_ponto_turistico.descricao,
                target_ponto_turistico.latitude,
                target_ponto_turistico.longitude,
            ))
            conn.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")
            last_id = cursor.fetchone()[0]
        except mysql.connector.Error as err:
            return_value = jsonify({'message': err}), 400
        else:
            return_value = jsonify({'message': f'{target_ponto_turistico.nome} cadastrado com id: {last_id}'}), 200
        
        if cursor:
            cursor.close()
        if conn:
            self.close_connection(conn)

        return return_value
        