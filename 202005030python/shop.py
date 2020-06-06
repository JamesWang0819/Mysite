from flask import Flask, session, render_template, request, redirect, g

app = Flask(__name__)

app.secret_key = b'should be a secret'

users_db = {
    'Darius':{
        'nid':'Darius',
        'password':'Myaxisready',
        'name':'Darius',
        'email':'darius@email.com'
    }
}

def get_user():
  user_id = session.get('user_id')
  if user_id:
    g.user = users_db.get(user_id)
  else:
    g.user = { 'nid': None, 'name': 'Guest' }

@app.route('/')
def index():
    get_user()
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    counter = session['counter']
        
    msg = 'Counter is %d' % counter
    return render_template('home.html', counter_msg = msg, user=g.user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nid = request.form.get('nid')
        password = request.form.get('password')
        print(nid, password)

        if not nid or not password:
            return 'invaild input'

        user = users_db.get(nid)
        if not user:
            return 'user not exist'
        if user.get('password') != password:
            return 'password error'
        session['user_id'] = nid
        return redirect ('/')

        return render_template('login.html')

    return render_template("login.html")

@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nid = request.form.get('nid')
        password = request.form.get('password')
        uname = request.form.get('uname')
        email = request.form.get('email')
        print(nid, password)

        if not nid or not password or not uname or not email:
            return 'invaild input'

        user = users_db.get(nid)
        if user:
            return 'user exist'

        users_db[nid] = {
        'nid':nid,
        'password':password,
        'name':uname,
        'email':email
        }

        session['user_id'] = nid
        return redirect ('/')

    return render_template("signup.html")

@app.route('/profile')
def profile():
    get_user()
    return render_template('profile.html', user=g.user)

@app.route('/uploadfile', methods = ('GET', 'POST'))
def uploadfile():
    
    return render_template('uploadfile.html')
