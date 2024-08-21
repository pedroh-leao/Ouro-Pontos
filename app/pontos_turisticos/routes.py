from flask import render_template, request, session
from app.pontos_turisticos import bp

from app.models.ponto_turistico import PontoTuristico
from app.models.dao_pontos_turisticos import DAO_Pontos_Turisticos
dao_pontos_turisticos = DAO_Pontos_Turisticos()


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

    target_ponto_turistico = PontoTuristico(
        nome=nome, 
        descricao=descricao, 
        longitude=float(longitude), 
        latitude=float(latitude)
    )

    return dao_pontos_turisticos.insert_ponto_turistico(target_ponto_turistico)

@bp.route("/pontos_turisticos/listar")
def tela_listar_pontos_turisticos():
    lista_pontos_turisticos = get_pontos_turisticos()
    headers = ['ID', 'Nome', 'Descrição']
    if session['type_user'] == 'admin':
        headers = headers + ['Latitude', 'Longitude', 'Remover']

    return render_template(
        'telaListaPontos.html',
        headers=headers,
        lista_pontos_turisticos=lista_pontos_turisticos
    )

@bp.route("/pontos_turisticos/deletar", methods=["DELETE"])
def deletar_ponto_turistico():
    id = request.json["id"]
    target_ponto_turistico = PontoTuristico(id=id)
    return dao_pontos_turisticos.delete_ponto_turistico(target_ponto_turistico)


@bp.route("/pontos_turisticos", methods=['GET'])
def get_pontos_turisticos():    
    return dao_pontos_turisticos.get_pontos_turisticos()

@bp.route("/pontos_turisticos/listarMenorCaminho")
def tela_lista_menor_caminho():
    return render_template('telaListaMenorCaminho.html')