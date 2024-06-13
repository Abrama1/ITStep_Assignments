import unittest
from pymongo import MongoClient
from db_operations import (
    insert_category,
    insert_product,
    remove_product,
    update_product,
    insert_order,
    get_pending_orders
)


def list_collections_in_db():
    client = MongoClient('localhost', 27017)
    db = client['testdb']
    collections = db.list_collection_names()
    client.close()
    return collections


class TestMongoDBOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = MongoClient('localhost', 27017)
        cls.db = cls.client['testdb']
        cls.categories_collection = cls.db['categories']
        cls.products_collection = cls.db['products']
        cls.orders_collection = cls.db['orders']

    @classmethod
    def tearDownClass(cls):
        cls.client.drop_database('testdb')
        cls.client.close()

    def setUp(self):
        # Clear collections before each test
        self.categories_collection.delete_many({})
        self.products_collection.delete_many({})
        self.orders_collection.delete_many({})

    def test_insert_category(self):
        category = insert_category(1, "Electronics")
        self.assertEqual(category['category_id'], 1)
        self.assertEqual(category['category_name'], "Electronics")
        self.assertIsNotNone(self.categories_collection.find_one({"category_id": 1}))

    def test_insert_product(self):
        insert_category(1, "Electronics")
        product = insert_product(1, "Laptop", 999.99, 10, 1)
        self.assertEqual(product['product_id'], 1)
        self.assertEqual(product['product_name'], "Laptop")
        self.assertIsNotNone(self.products_collection.find_one({"product_id": 1}))

    def test_remove_product(self):
        insert_category(1, "Electronics")
        insert_product(1, "Laptop", 999.99, 10, 1)
        self.assertTrue(remove_product("Laptop"))
        self.assertIsNone(self.products_collection.find_one({"product_name": "Laptop"}))

    def test_update_product(self):
        insert_category(1, "Electronics")
        insert_product(1, "Laptop", 999.99, 10, 1)
        self.assertTrue(update_product("Laptop", product_price=1099.99, stock_quantity=8))
        product = self.products_collection.find_one({"product_name": "Laptop"})
        self.assertEqual(product['product_price'], 1099.99)
        self.assertEqual(product['stock_quantity'], 8)

    def test_insert_order(self):
        insert_category(1, "Electronics")
        insert_product(1, "Laptop", 999.99, 10, 1)
        order = insert_order(1, 1, 2, "pending")
        self.assertEqual(order['order_id'], 1)
        self.assertEqual(order['quantity'], 2)
        self.assertEqual(order['status'], "pending")
        product = self.products_collection.find_one({"product_id": 1})
        self.assertEqual(product['stock_quantity'], 8)

    def test_get_pending_orders(self):
        insert_category(1, "Electronics")
        insert_product(1, "Laptop", 999.99, 10, 1)
        insert_order(1, 1, 2, "pending")
        insert_order(2, 1, 3, "delivered")
        pending_orders = get_pending_orders()
        self.assertEqual(len(pending_orders), 1)
        self.assertEqual(pending_orders[0]['order_id'], 1)
        self.assertEqual(pending_orders[0]['product_name'], "Laptop")
        self.assertEqual(pending_orders[0]['category_name'], "Electronics")

    def test_list_collections_in_db(self):
        # Insert some data to create collections
        insert_category(1, "Electronics")
        insert_product(1, "Laptop", 999.99, 10, 1)
        insert_order(1, 1, 2, "pending")

        collections = list_collections_in_db()
        self.assertIn("categories", collections)
        self.assertIn("products", collections)
        self.assertIn("orders", collections)


if __name__ == '__main__':
    unittest.main()
