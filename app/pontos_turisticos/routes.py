from flask import render_template, request
from app.pontos_turisticos import bp
from app.models.ponto_turistico import PontoTuristico
from app.extensions import db

@bp.route("/pontos_turisticos/cadastrar")
def tela_cadastrar_pontos_turisticos():
    return render_template('telaCadastroPontos.html')

@bp.route("/pontos_turisticos/listar")
def tela_listar_pontos_turisticos():

    lista_pontos_turisticos = get_pontos_turisticos()
    print(lista_pontos_turisticos)

    headers = ['id', 'nome', 'descricao', 'longitude', 'latitude']

    return render_template(
        'telaListaPontos.html',
        headers=headers,
        lista_pontos_turisticos=lista_pontos_turisticos
    )


@bp.route("/pontos_turisticos", methods=['POST'])
def add_pontos_turisticos():
    data = request.json
    print("Data received from the request:", data)

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

    print(novo_ponto_turistico.id)

    return {'id': novo_ponto_turistico.id}

@bp.route("/pontos_turisticos", methods=['GET'])
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