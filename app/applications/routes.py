from flask import Blueprint, session, redirect, url_for

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        redirect(url_for('auth.login'))
    return 'Job Tracker Dashboard'
