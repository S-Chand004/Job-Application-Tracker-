Job Application Tracker

A Flask + MySQL based application to manage and analyze job applications.

Features:

1. User registration & login (secure password hashing)
2. Add job applications (company, role, status, notes, date)
3. Edit/update applications anytime
4. View applications in clean dashboard

Analytics:

1. Applications by status
2. Applications per month
3. Clean, modular backend structure with Blueprints

Tech Stack:

1. Python, Flask
2. MySQL (Flask-MySQLdb)
3. HTML/CSS templates
4. SQL Joins & aggregations

Project Structure:

1. auth/ → login & register
2. applications/ → add, edit, view applications
3. analytics/ → insights dashboard
4. models/ → database connection
5. templates/ → UI pages

Database Schema:

1. users
2. applications

MySQL Queries:

CREATE DATABASE job_tracker_db;
USE job_tracker_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    company VARCHAR(150),
    role VARCHAR(150),
    status ENUM('applied', 'interview', 'offer', 'rejected') DEFAULT 'applied',
    applied_date DATE,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
