from . import db
from flaskr.model import Note
from flask import Blueprint, render_template, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask import request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():

    if request.method == 'POST':
        data = request.form.get('note')
        note = Note(data=data, user_id=current_user.id)

        if len(data) < 1:
            flash('Note must be at least more than 1 character.', category='error')

        else:
            try:
                db.session.add(note)
                db.sesion.commit()
            except:  
                flash('Error trying to save the note, please try again.', category='error')

            flash('Note Added!', category='success')
    return render_template('home.html', user=current_user)