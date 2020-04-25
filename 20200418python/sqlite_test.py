import sqlite3  
conn = sqlite3.connect('myshop.db')

def createproducttable(conn):
    c = conn.cursor()
    sql = """
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            qty INTEGER NOT NULL
        )
    """
    c.execute(sql)
    conn.commit

def insertproduct(conn, name, price, qty):
    c = conn.cursor()
    sql = """
        INSERT INTO products (name, price, qty)
        VALUES (?, ?, ?)
    """
    #c.execute(sql, ('Pen', 15, 45))
    #c.execute(sql, ('Cup', 80, 5))
    #c.execute(sql, ('Notebook', 25, 20))
    c.execute(sql, (name, price, qty))
    conn.commit()

def listproduct(conn, where):
    c = conn.cursor() 
    sql = "SELECT id, name, price, qty FROM products where {}".format(where)
    c.execute(sql)
    pds = c.fetchall()
    for pd in pds:
        print(pd)

def getproducts(conn):
    c = conn.cursor() 
    sql = "SELECT id, name, price, qty FROM products"
    c.execute(sql)
    return c.fetchall()

def update_product(conn, id, price, qty):  
    sql = """
        UPDATE products
        SET price = ?,
            qty = ?
        WHERE id = ?
    """
    c = conn.cursor()
    c.execute(sql, (price, qty, id))
    conn.commit()

def delete_by_id(conn, id):
    sql = """
    Delete FROM products WHERE id = ?
    """
    c = conn.cursor()
    c.execute(sql, (id,))
    conn.commit

def test():
    #createproducttable(conn)
    #insertproduct (conn, 'JoJo Memes', 999, 5)
    #insertproduct (conn, 'Coffin Dancer', 2000, 6)

    delete_by_id(conn, 1)
    update_product(conn, 1, 666, 2)
    listproduct(conn, 'qty < 50')
    conn.close()

test()