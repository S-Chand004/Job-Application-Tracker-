from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def auth():
    return 'This is the authentication page'