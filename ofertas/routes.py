from flask import jsonify, request
from ofertas import ofertas_bp
from ofertas.models import OfferModel
from app import db


# Health check
@ofertas_bp.route('/offers/ping', methods=['GET'])
def ping():
    return jsonify({'msg': 'pong'}), 200


