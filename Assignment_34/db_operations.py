from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['testdb']

categories_collection = db['categories']
products_collection = db['products']
orders_collection = db['orders']


def insert_category(category_id, category_name):
    category = {
        "category_id": category_id,
        "category_name": category_name
    }
    categories_collection.insert_one(category)
    return category


def insert_product(product_id, product_name, product_price, stock_quantity, category_id):
    category = categories_collection.find_one({"category_id": category_id})
    if not category:
        raise ValueError("Category not found")

    product = {
        "product_id": product_id,
        "product_name": product_name,
        "product_price": product_price,
        "stock_quantity": stock_quantity,
        "category_id": category_id
    }
    products_collection.insert_one(product)
    return product


def remove_product(product_name):
    result = products_collection.delete_one({"product_name": product_name})
    return result.deleted_count > 0


def update_product(product_name, **kwargs):
    update_fields = {f"$set": kwargs}
    result = products_collection.update_one({"product_name": product_name}, update_fields)
    return result.matched_count > 0


def insert_order(order_id, product_id, quantity, status):
    product = products_collection.find_one({"product_id": product_id})
    if not product:
        raise ValueError("Product not found")
    if product['stock_quantity'] < quantity:
        raise ValueError("Insufficient stock")

    order = {
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "order_date": datetime.utcnow(),
        "status": status
    }
    orders_collection.insert_one(order)

    products_collection.update_one(
        {"product_id": product_id},
        {"$inc": {"stock_quantity": -quantity}}
    )

    return order


def get_pending_orders():
    pending_orders = orders_collection.find({"status": "pending"})

    results = []

    for order in pending_orders:
        product = products_collection.find_one({"product_id": order["product_id"]})
        category = categories_collection.find_one({"category_id": product["category_id"]})

        result = {
            "order_id": order["order_id"],
            "product_name": product["product_name"],
            "category_name": category["category_name"],
            "quantity": order["quantity"],
            "order_date": order["order_date"],
            "status": order["status"]
        }

        results.append(result)

    return results
