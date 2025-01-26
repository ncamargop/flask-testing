from flask import Blueprint

# check this
ofertas_bp = Blueprint('ofertas', __name__)
from ofertas import routes, models
