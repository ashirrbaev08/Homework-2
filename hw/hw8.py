import sqlite3

connect = sqlite3.connect('customer.db')
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50)
    
    )    
''')

cursor.execute('''
     CREATE TABLE IF NOT EXISTS purchases(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        goods TEXT,
        total INTEGER,
        customer_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customer(id)
        )
''')

connect.commit()

def create_customer(name):
    cursor.execute('INSERT INTO customers(name) VALUES (?)', (name,))
    connect.commit()
    print(f"Клиент создан! {name}")

def create_purchase(customer_id,purchase_name,total):
    cursor.execute('INSERT INTO purchases(customer_id,goods,total) VALUES (?,?,?)',
                   (customer_id,purchase_name,total))
    connect.commit()
    print(f"Покупка была создана! {purchase_name}")

# create_customer("Bektur")
# create_customer("Eldar")
# create_customer("Sara")
# create_customer("Bili")
# create_purchase(1,"ice-cream",200)
# create_purchase(2,"Shoro",300)
# create_purchase(3,"samsy",400)

def get_customer_purchase():

    cursor.execute('''
            SELECT customers.name,purchases.goods,purchases.total
            FROM customers INNER JOIN purchases ON customers.id = purchases.customer_id
    ''')
    customers = cursor.fetchall()

    for i in customers:
        print(f"NAME:{i[0]} PURCHASE:{i[1]} TOTAL:{i[2]}")

# get_customer_purchase()

def max_total():
    cursor.execute('SELECT MAX(total) FROM purchases')
    purchases = cursor.fetchone()
    print(purchases)

# max_total()

def min_total():
    cursor.execute('SELECT MIN(total) FROM purchases')
    purchases = cursor.fetchone()
    print(purchases)

# min_total()

def avg_total():
    cursor.execute('SELECT AVG(total) FROM purchases')
    purchases = cursor.fetchone()
    print(purchases)

# avg_total()

def sum_total():
    cursor.execute('SELECT SUM(total) FROM purchases')
    purchases = cursor.fetchone()
    print(purchases)

# sum_total()

def get_custmer_orders():
    cursor.execute('''
        SELECT customer_id, COUNT(*)
        FROM purchases
        GROUP BY customer_id    
    ''')
    customers = cursor.fetchall()
    print(customers)

# get_custmer_orders()


def samsy_customer():
    cursor.execute('''
        SELECT name
        FROM customers
        WHERE id IN (
            SELECT customer_id FROM purchases
            WHERE goods = 'samsy'           
        )
    ''')
    customer = cursor.fetchall()
    print(customer)

# samsy_customer()

def create_my_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT 
            customers.name,
            purchases.goods,
            purchases.total
        FROM customers
        LEFT JOIN purchases ON customers.id = purchases.customer_id
    ''')
    connect.commit()


# create_my_view()

def get_customer_purchases_join():
    cursor.execute('SELECT * FROM my_view')
    results = cursor.fetchall()
    print(results)

get_customer_purchases_join()


