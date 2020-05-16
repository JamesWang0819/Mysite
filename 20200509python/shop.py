from flask import Flask, render_template
from flask import request, redirect
app = Flask(__name__)

products = {
  "sku01": { 
      "id": "sku01", 
      "name": "Spandex", 
      "price": 60000, 
      "desc": "I'm thin.",
      "src": "https://media1.tenor.com/images/e3b2141c9028da0b7090a7995c381392/tenor.gif?itemid=5103926" },
  "sku02": { 
      "id": "sku02", 
      "name": "Guns", 
      "price": 10, 
      "desc": "Guns, lots of guns.",
      "src": "https://vignette.wikia.nocookie.net/fallout/images/3/3c/Fallout4_laser_pistol.png/revision/latest/scale-to-width-down/340?cb=20190808164830" },
  "sku03": { 
      "id": "sku03", 
      "name": "Justin Bieber", 
      "price": "265000000", 
      "desc": "Baby, baby, baby no.",
      "src": "https://www.famousbirthdays.com/group_images/medium/baby-justin-bieber-song.jpg" },
  "sku04": { 
      "id": "sku04", 
      "name": "Weed", 
      "price": 110, 
      "desc": "Smoke weed everyday!!!",
      "src": "https://cms.qz.com/wp-content/uploads/2019/10/Recreational-Weed-e1570153378769.jpg?quality=75&strip=all&w=1600&h=900&crop=1" }
}

mycart = {
    'sku01': 3
}

@app.route('/')
def shop():
    return render_template('shop.html', products = products)

@app.route('/product/<sid>')
def productView(sid):
    pd = products[sid]
    return render_template('product.html', product = pd)

@app.route('/cart')
def cartView():
    return render_template('cart.html', mycart = mycart,
        products= products)

@app.route('/add-cart/<sid>')
def addcart(sid):
    mycart[sid] = mycart.get (sid, 0) + 1
    return redirect('/cart')