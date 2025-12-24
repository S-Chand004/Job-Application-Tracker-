from flask import Blueprint, session, render_template, redirect, url_for
from app.models.db import mysql

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics')
def analytics():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']

    cur = mysql.connection.cursor()

    cur.execute("SELECT status, COUNT(*) FROM applications WHERE user_id = %s GROUP BY status", (user_id,))
    status_count = cur.fetchall()

    cur.execute("SELECT applied_date, COUNT(*) FROM applications WHERE user_id = %s GROUP BY applied_date", (user_id,))
    month_count = cur.fetchall()

    cur.close()

    return render_template('analytics.html', status_counts = status_count, month_counts = month_count)
