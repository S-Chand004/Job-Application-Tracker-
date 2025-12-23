from flask import Blueprint, session, redirect, url_for, request, render_template
from app.models.db import mysql

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        redirect(url_for('auth.login'))
    return render_template('dashboard.html')

@applications_bp.route('/add-application', methods = ['GET', 'POST'])
def add_application():
    if 'user_id' not in session:
        redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        company = request.form['company']
        role = request.form['role']
        status = request.form['status']
        applied_date = request.form['applied_date']
        notes = request.form['notes']
        user_id = session['user_id']

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO applications (user_id, company, role, status, applied_date, notes) VALUES (%s, %s, %s, %s, %s, %s)",
                    (user_id, company, role, status, applied_date, notes))
        cur.connection.commit()
        cur.close()
        
        return redirect(url_for('applications.view_applications'))
    
    return render_template('add_application.html')


@applications_bp.route('/applications')
def view_applications():
    if 'user_id' not in session:
        redirect(url_for('auth.login'))

    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT company, role, status, applied_date, notes FROM applications WHERE user_id = (%s) ORDER BY applied_date DESC",
                (user_id,))
    
    apps = cur.fetchall()
    cur.close()

    return render_template('applications.html', apps = apps)
