from app.main import bp
from flask import render_template, request
from app.pontos_turisticos.routes import tela_listar_pontos_turisticos

@bp.route('/', methods=["GET"])
def index():

    arguments = request.args.get("adm")
    if arguments is not None and arguments == "123456":
        return render_template('index.html')
    
    return tela_listar_pontos_turisticos()
