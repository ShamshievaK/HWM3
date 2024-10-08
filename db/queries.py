CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
    )
"""


INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""

# CREATE_TABLE_PRODUCTS_DETAIL="""
# CREATE TABLE IF NOT EXISTS products_detail (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# product_id INTEGER,
# category VARCHAR(255),
# info_product TEXT
# )"""

# INSERT_INTO_PRODUCT_DETAIL="""
# INSERT INTO products_detail (product_id, category, info_product) VALUES (?,?,?)"""


CREATE_TABLE_PRODUCTS_DETAILS="""
    CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(255),
    category VARCHAR(255),
    info_product VARCHAR(255)
    )
"""

INSERT_PRODUCTS_QUERY_DETAILS="""
INSERT INTO products_details (product_id, category, info_product) VALUES (?, ?, ?)"""


CREATE_TABLE_COLLECTION_PRODUCTS="""
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(255),
    collection VARCHAR(255)
    )
"""

INSERT_COLLECTION_PRODUCTS_QUERY="""
INSERT INTO collection_products (product_id, collection) VALUES (?, ?)"""

