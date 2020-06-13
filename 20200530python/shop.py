import os
from flask import Flask, session, render_template, request, redirect, g
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, 'static', 'upload')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.secret_key = b'should be a secret'

users_db = {
    'Darius':{
        'nid':'Darius',
        'password':'Myaxisready',
        'name':'Darius',
        'email':'darius@gmail.com'
    },
    'Quinn':{
        'nid':'Quinn',
        'password':'Demaciawing',
        'name':'Quinn',
        'email':'quinn@gmail.com'  
    }
}

items_db = [{
    'item_id': 0,
    'nid':'Quinn',
    'name': 'Valor',
    'price': 6000,
    'desc': 'Blue Bird',
    'filename': 'bird.jpg'
}]

def get_user():
  user_id = session.get('user_id')
  if user_id:
    g.user = users_db.get(user_id)
  else:
    g.user = { 'nid': None, 'name': 'Guest' }

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    get_user()
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    counter = session['counter']
        
    msg = 'Counter is %d' % counter
    return render_template('home.html', counter_msg = msg, user=g.user, items = items_db, user_map = users_db)

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
    get_user()
    if not g or not g.user['nid']:
        return redirect('/')

    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        desc = request.form.get('desc')
        if not name or not price or not desc:
            return "Invalid Inputs"

        filename = None
        if 'picture' in request.files:
            pic = request.files['picture']
            if pic and allowed_file(pic.filename):
                filename = secure_filename(pic.filename)
                pic.save(os.path.join(UPLOAD_FOLDER, filename))

        item_id = len(items_db)
        items_db.append({
            'item_id': item_id,
            'nid': g.user['nid'],
            'name': name,
            'price': float(price),
            'desc': desc,
            'filename': filename
        })
        return redirect('/')
    return render_template('uploadfile.html', user=g.user)

@app.route('/item/<item_id>')
def itemView(item_id):
    item = None
    for it in items_db:
        if str(it ['item_id']) == item_id:
            item = it
            break

    return render_template('item.html', item = item)

@app.route('/myitems')
def myitems():
    get_user()
    items = [it for it in items_db if it['nid'] == g.user['nid']]
    return render_template('my-items.html', user = g.user, items = items)


