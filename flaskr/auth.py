from flask import Blueprint,render_template, request

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
            pass
        elif len(firstName) <2:
            pass
        elif password != confirm_password:
            pass
        else:
            pass
        
        return render_template('signup.html', badPassword=False)
    else:
        return render_template('signup.html', badPassword=False)