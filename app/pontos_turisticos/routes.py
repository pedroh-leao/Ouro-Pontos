from flask import render_template, request
from app.pontos_turisticos import bp
from app.models.ponto_turistico import PontoTuristico
from app.extensions import db

@bp.route("/ponto_turistico", methods=['POST'])
def add_ponto_turistico():
    nome = request.json["nome"]
    descricao = request.json["descricao"]
    longitude = request.json["longitude"]
    latitude = request.json["latitude"]

    novo_ponto_turistico = PontoTuristico(
        nome=nome,
        descricao=descricao,
        longitude=longitude,
        latitude=latitude
    )

    db.session.add(novo_ponto_turistico)
    db.session.commit()

    return {'id': novo_ponto_turistico.id}

@bp.route("/ponto_turistico", methods=['GET'])
def get_pontos_turisticos():
    pontos_turisticos = PontoTuristico.query.all()
    output = [{
        'id': pt.id,
        'nome': pt.nome,
        'descricao': pt.descricao,
        'longitude': pt.longitude,
        'latitude': pt.latitude,
    } for pt in pontos_turisticos]

    return output