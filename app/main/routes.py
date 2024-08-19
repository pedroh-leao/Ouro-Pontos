from app.main import bp
from flask import render_template, request, session
from app.pontos_turisticos.routes import tela_listar_pontos_turisticos

@bp.route('/', methods=["GET"])
def index():

    arguments = request.args.get("adm")
    if arguments is not None and arguments == "123456":
        session['type_user'] = 'admin'
        return render_template('index.html')
    
    session['type_user'] = 'simple_user'
    return tela_listar_pontos_turisticos()
