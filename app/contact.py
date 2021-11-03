from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db import get_db

bp = Blueprint('contact',__name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def home():
    db, c = get_db()
    c.execute('SELECT * FROM contacts')
    contacts = c.fetchall()
    return render_template('contacts/home.html', contacts = contacts)

@bp.route('/crate', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
            company = request.form.get('company')
            role = request.form.get('role')
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            mail = request.form.get('mail')
            phone = request.form.get('phone')
            errors = []

            if not company:
                errors.append('El campo empresa no puede estar en blanco')
            if not role:
                errors.append('El campo rol no puede estar en blanco')
            if not firstname:
                errors.append('El campo nombre no puede estar en blanco')
            if not lastname:
                errors.append('El campo apellido no puede estar en blanco')
            if not mail:
                errors.append('El campo correo no puede estar en blanco')
            if not phone:
                errors.append('El campo telefono no puede estar en blanco')
            
            if len(errors) == 0:
                db, c = get_db()
                c.execute(
                    'INSERT INTO contacts (company, role, firstname, lastname, mail, phone) VALUES (%s, %s, %s, %s, %s, %s)',
                    (company, role, firstname, lastname, mail, phone)                    
                )
                db.commit()
                return redirect(url_for('contact.home'))
            else:
                for error in errors:
                    flash(error)
    return render_template('contacts/create.html')

@bp.route('<int:id>/update', methods=['GET', 'POST'])
def update(id):
    return 'actualizar'

@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
        db, c = get_db()
        c.execute(
            'DELETE FROM contacts WHERE id = %s', (id,)
        )
        db.commit()
        return redirect(url_for('contact.home'))