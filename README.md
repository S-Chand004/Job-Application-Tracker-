Job Application Tracker

A Flask + MySQL based, backend centric application to manage and analyze job applications with user login and registration (with secure password hashing).

Technology Stack:

1. Python, Flask (Blueprints)
2. MySQL (Flask-MySQLdb)
3. SQL Joins & aggregations
4. Simple HTML Templates

Features:

1. User registration & login (secure password hashing)
2. Add job applications (company, role, status, date, notes)
3. Edit/update applications anytime
4. View applications in a clean dashboard
5. With Analytics:
    - Applications by status
    - Applications per month
    - Clean, modular backend structure with Blueprints

Project Structure:

project/
| -- app/
	| -- analytics/
	| -- applications/
	| -- auth/
	| -- home/
	| -- models/
	| -- statics/
	| -- templates/
	| -- analytics/
| -- __init__.py
| -- config.py
| -- README.md
| -- requirements.txt
| -- run.py

Installation and Setup Instructions:
git clone <repo-url>
cd project

# Create virtual environment
python -m venv venv
source venv/bin/activate  (Linux/Mac)
venv\Scripts\activate     (Windows)

# Install dependencies
pip install -r requirements.txt

Database Schema:

users
applications

Database Setup:
Run the following MySQL queries to create tables:

CREATE DATABASE job_tracker_db;
USE job_tracker_db;

CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100) UNIQUE, password VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

CREATE TABLE applications ( id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, company VARCHAR(150), role VARCHAR(150), status ENUM('applied', 'interview', 'offer', 'rejected') DEFAULT 'applied', applied_date DATE, notes TEXT, FOREIGN KEY (user_id) REFERENCES users(id) );
