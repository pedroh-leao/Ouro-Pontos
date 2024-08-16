from flask import Blueprint

bp = Blueprint('pontos_turisticos', __name__)

from app.pontos_turisticos import routes