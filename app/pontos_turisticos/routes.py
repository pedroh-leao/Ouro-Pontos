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


def listar_pontos_adm(headers, lista_pontos_turisticos):
    headers = headers + ['Latitude', 'Longitude', 'Editar', 'Remover']

    return render_template(
        'telaListaPontosADM.html',
        headers=headers,
        lista_pontos_turisticos=lista_pontos_turisticos
    )


def listar_pontos_usuario(headers, lista_pontos_turisticos):
    return render_template(
        'telaListaPontos.html',
        headers=headers,
        lista_pontos_turisticos=lista_pontos_turisticos
    )


@bp.route("/pontos_turisticos/listar")
def tela_listar_pontos_turisticos():
    lista_pontos_turisticos = get_pontos_turisticos()
    headers = ['ID', 'Nome', 'Descrição']

    print(session['type_user'])
    if session['type_user'] == 'admin':
        return listar_pontos_adm(headers, lista_pontos_turisticos)
    else:
        return listar_pontos_usuario(headers, lista_pontos_turisticos)

@bp.route("/pontos_turisticos/deletar", methods=["DELETE"])
def deletar_ponto_turistico():
    id = request.json["id"]
    target_ponto_turistico = PontoTuristico(id=id)
    return dao_pontos_turisticos.delete_ponto_turistico(target_ponto_turistico)


@bp.route("/pontos_turisticos", methods=['GET'])
def get_pontos_turisticos():    
    return dao_pontos_turisticos.get_pontos_turisticos()


@bp.route("/pontos_turisticos/listar_por_ids", methods=['POST'])
def listar_pontos_turisticos_por_ids():
    ids = request.json["ids"]
    return dao_pontos_turisticos.get_many_pontos_turisticos_by_ids(ids)

@bp.route("/pontos_turisticos/editar", methods=["POST"])
def update_ponto_turistico():
    data = request.json
    print("Data received from the request:", data)

    nome = request.json["nome"]
    descricao = request.json["descricao"]
    longitude = request.json["longitude"]
    latitude = request.json["latitude"]
    id = request.json["id"]

    target_ponto_turistico = PontoTuristico(
        nome=nome, 
        descricao=descricao, 
        longitude=float(longitude), 
        latitude=float(latitude),
        id = int(id)
    )
    return dao_pontos_turisticos.update_ponto_turistico(target_ponto_turistico)

@bp.route("/pontos_turisticos/pontos_turisticos/tela_editar", methods=["GET"])
def tela_editar_ponto_turistico():
    id = request.args.get("id")
    ponto_turistico = dao_pontos_turisticos.get_ponto_turistico_by_id(id)
    print(ponto_turistico)
    return render_template(
        'telaEditarPonto.html',
        ponto_turistico=ponto_turistico
    )

@bp.route("/pontos_turisticos/listarMenorCaminho")
def tela_lista_menor_caminho():
    return render_template('telaListaMenorCaminho.html')