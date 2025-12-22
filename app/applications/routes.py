from flask import Blueprint

applications_bp = Blueprint('applications_bp', __name__)

@applications_bp.route('/applications')
def applications():
    return 'This is the applications page'