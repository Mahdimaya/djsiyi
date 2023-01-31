from flask import Blueprint ,render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/Login', methods=['GET', 'POST'])
def login():
    data= request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/Logout')
def logout():
    return "<p>Logout</p>"  

@auth.route('/sign-up')
def sign_up():
    if request.method == 'POST'
    email= request.form.get('email')
    firstname= request.form.get('firstname')
    lastname= request.form.get('lastname')
    password= request.form.get('password')
    username= request.form.get('username')

    if len (email) < 4:
        flash('email must be greater than 4 characters', category='error')
       pass
    elif len (firstname) < 2:
        flash('firstname must be greater than 2 characters', category='error')
       pass
    elif len (lastname) < 4:
        flash('lastname must be greater than 2 characters', category='error')
       pass
    elif len (password) <7:
        flash('password must be greater than 7 characters', category='error')
        pass
    else:
        flash('account created!', category='success')
        pass
        

    
    return render_template("signup.html")