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
        return redirect(url_for('auth.login'))
    
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
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT company, role, status, applied_date, notes, id FROM applications WHERE user_id = (%s) ORDER BY applied_date DESC",
                (user_id,))
    
    apps = cur.fetchall()
    cur.close()

    return render_template('applications.html', apps = apps)

@applications_bp.route('/edit/<app_id>', methods = ['GET', 'POST'])
def edit_applications(app_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']

    cur = mysql.connection.cursor()
    
    if request.method == 'GET':
        cur.execute("SELECT company, role, status, applied_date, notes FROM applications WHERE id=%s AND user_id = %s", 
                    (app_id, user_id))
        app_data = cur.fetchone()
        cur.close()

        if not app_data:
            return "Application not found."
    
        return render_template('edit_application.html', app = app_data, app_id = app_id)

    if request.method == 'POST':
        company = request.form['company']
        role = request.form['role']
        status = request.form['status']
        applied_date = request.form['applied_date']
        notes = request.form['notes']

        cur.execute("UPDATE applications SET company = %s, role = %s, status = %s, applied_date = %s, notes = %s WHERE id = %s AND user_id = %s", (company, role, status, applied_date, notes, app_id, user_id))

        mysql.connection.commit()
        cur.close()

        return redirect(url_for('applications.view_applications'))
    
