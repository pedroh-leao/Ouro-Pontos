from app.main import bp
from flask import render_template, request, session
from app.pontos_turisticos.routes import tela_listar_pontos_turisticos

@bp.route('/menu', methods=["GET"])
def index_adm():  
    session['type_user'] = 'admin'
    return render_template("index.html")


@bp.route('/', methods=["GET"])
def index():    
    session['type_user'] = 'simple_user'
    return tela_listar_pontos_turisticos()
