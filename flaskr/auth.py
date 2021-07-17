from flask import Blueprint,render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('home.html')

@auth.route('/sign-up',  methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password1') 
        confirm_password = request.form.get('password2')

        if len(email) < 4:
            flash('email must be greater than 4 characters.',category='error')
        elif len(firstName) <2:
            flash('First Name must be greater than 2 characters.', category='error')
        elif password != confirm_password:
            flash('Passwords dont\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        
        return render_template('signup.html', badPassword=False)
    else:
        return render_template('signup.html', badPassword=False)