import psycopg2
from psycopg2.extras import execute_values
from config import config

def add_products(product_dicts):
    # statement for inserting a new row into the product table
    insert_product = "INSERT INTO product(asin,title,product_group,sales_rank) VALUES %s RETURNING asin;"
    # statement for inserting a new row into the similar_products table
    insert_assin_similars = "INSERT INTO similar_products(asin_similar,asin_product) VALUES %s "
    # statement for inserting a new row into the review table
    insert_product_review = "INSERT INTO review(asin_product,date,costumer,rate,vote,helpful) VALUES %s"
    # statement for inserting a new row into the category_info table
    insert_category_info = "INSERT INTO category_info(category_id,name) VALUES %s ON CONFLICT DO NOTHING"
    # statement for inserting a new row into the category table
    insert_category = "INSERT INTO category(asin_product,category_id) VALUES %s"
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        conn.autocommit = False  # disable automatic commit mode
        cur = conn.cursor()

        # start transaction
        cur.execute("BEGIN")

        # insert products
        products = [(product_dict['asin'], product_dict['title'], product_dict['product_group'], product_dict['sales_rank']) for product_dict in product_dicts if len(product_dict) > 1]
        execute_values(cur, insert_product, products, page_size=10000)
        print("Todos os produtos inseridos")

        
        # fetch all products
        cur.execute("SELECT asin FROM product")
        product_rows = cur.fetchall()
        
        if product_rows:
            for i, row in enumerate(product_rows):
                asin_product = row[0]
                product_dict = product_dicts[i]

                # insert similar products
                if 'similar' in product_dict:
                    similar_products = product_dict['similar']
                    if similar_products:
                        similar_values = [(asin_similar, asin_product) for asin_similar in similar_products]
                        execute_values(cur, insert_assin_similars, similar_values, page_size=1000)

                # insert categories and categories_info
                if 'categories' in product_dict:
                    categories = product_dict['categories']
                    if categories:
                        categorys_info = list(set([(category[1], category[0]) for category in categories]))
                        execute_values(cur,insert_category_info,categorys_info, page_size=1000)
                        category_values = list(set([(asin_product, category[-1]) for category in categories]))
                        execute_values(cur, insert_category, category_values, page_size=1000)

                #insert reviews
                if 'reviews' in product_dict:
                    reviews = product_dict['reviews']
                    if reviews:
                        rev = [(asin_product, *review[0][:5]) for review in reviews]
                        execute_values(cur, insert_product_review, rev, page_size=1000)
        # commit
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()  # rollback in case of error
    finally:
        if conn is not None:
            conn.close()