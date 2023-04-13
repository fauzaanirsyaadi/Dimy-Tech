from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

metadata = MetaData()

engine = create_engine("sqlite:///orders.db")
metadata.create_all(engine)

customer = Table(
    "customer",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_name", String(255), nullable=False),
)

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("price", Integer, nullable=False),
)

customer_address = Table(
    "customer_address",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customer.id")),
    Column("address", String(255), nullable=False),
)

payment_method = Table(
    "payment_method",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("is_active", Integer, nullable=False),
)

orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customer.id")),
    Column("customer_address_id", Integer, ForeignKey("customer_address.id")),
)

order_product = Table(
    "order_product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("product_id", Integer, ForeignKey("product.id")),
    Column("quantity", Integer, nullable=False),
)

order_payment = Table(
    "order_payment",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id")),
    Column("payment_method_id", Integer, ForeignKey("payment_method.id")),
)


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# define connection to database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# define transaction model
class Transaction(BaseModel):
    customer_id: int
    customer_address_id: int
    products: List[int]
    quantities: List[int]
    payment_methods: List[int]

# define route for creating new transaction
@app.post("/transactions/")
async def create_transaction(transaction: Transaction):
    # insert new customer address
    cursor.execute(f"INSERT INTO customer_address (customer_id, address) VALUES (?, ?)", 
        (transaction.customer_id, transaction.customer_address_id))
    customer_address_id = cursor.lastrowid

    # insert new order
    cursor.execute(f"INSERT INTO orders (customer_id, customer_address_id) VALUES (?, ?)", 
        (transaction.customer_id, customer_address_id))
    order_id = cursor.lastrowid

    # insert order products
    for i in range(len(transaction.products)):
        cursor.execute(f"INSERT INTO order_product (order_id, product_id, quantity) VALUES (?, ?, ?)", 
            (order_id, transaction.products[i], transaction.quantities[i]))

    # insert order payment methods
    for payment_method in transaction.payment_methods:
        cursor.execute(f"INSERT INTO order_payment (order_id, payment_method_id) VALUES (?, ?)", 
            (order_id, payment_method))

    # commit changes to database
    conn.commit()

    # return new transaction ID
    return {"transaction_id": order_id}

# keterangan :  api ini berfungsi untuk membuat data transaksi dengan mengimplementasikan desain database. 
# catatan : dengan asumsi sudah ada customer,product, dan payment methods
# POST http://localhost:8000/orders

# Request body:
# {
#   "customer_id": 1,
#   "customer_address_id": 1,
#   "products": [
#     {"product_id": 1, "quantity": 2},
#     {"product_id": 2, "quantity": 1}
#   ],
#   "payment_methods": [
#     {"payment_method_id": 1},
#     {"payment_method_id": 2}
#   ]
# }


# detail transaction :

# GET http://localhost:8000/orders/1
