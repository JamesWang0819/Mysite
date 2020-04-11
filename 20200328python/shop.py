from flask import Flask, render_template
app = Flask(__name__)

products = {
  "sku01": { "id": "sku01", "name": "Dig it. SUCKA!!!", "price": 666, "src": "https://i.ytimg.com/vi/AL4v0LUXR4k/maxresdefault.jpg" },
  "sku02": { "id": "sku02", "name": "Pina Colada", "price": 300, "src": "https://www.thespruceeats.com/thmb/yGgUHcTYwSPDwvVZwSlPM_4vAl8=/1820x1365/smart/filters:no_upscale()/frozen-pina-colada-recipe-759297-4_preview1-5b02fa8ca18d9e003cddc746.jpeg" },
  "sku03": { "id": "sku03", "name": "Spandex", "price": 60000, "src": "https://media1.tenor.com/images/e3b2141c9028da0b7090a7995c381392/tenor.gif?itemid=5103926" },
  "sku04": { "id": "sku04", "name": "Trout", "price": 25, "src": "https://cdn.pixabay.com/photo/2017/05/28/08/39/isolated-2350400__340.png" },
  "sku05": { "id": "sku05", "name": "Nicolas Cage: Mona Lisa", "price": 9999999, "src": "https://i.pinimg.com/originals/49/5a/81/495a813baa9101a87b7ffc6c7c626e5d.jpg" },
  "sku06": { "id": "sku06", "name": "Weed", "price": 110, "src": "https://cms.qz.com/wp-content/uploads/2019/10/Recreational-Weed-e1570153378769.jpg?quality=75&strip=all&w=1600&h=900&crop=1" }
}

cart = [
    {'id': 'sku01', 'num': 5},
    {'id': 'sku03', 'num': 1},
    {'id': 'sku04', 'num':10},
    {'id': 'sku02', 'num': 2},
    {'id': 'sku05', 'num': 1},
    {'id': 'sku06', 'num': 50}

]

@app.route("/")
def hello():
    heading = 'HIGH NOON STORE'
    title = 'Welcome to HIGH NOON STORE'
    subtitle = 'Can you smell what the Rock is cooking?'
    subtitle1 = 'Pina Colada'
    subtitle2 = 'Spandex'
    total = 0

    for item in cart:
        prod = products.get(item.get('id'))
        total += prod.get('price') * item.get('num')

    return render_template('shop.html', Heading = heading, title = title, 
    subtitle = subtitle, subtitle1 = subtitle1, subtitle2 = subtitle2,
    products = products, cart=cart, total=total)


@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)