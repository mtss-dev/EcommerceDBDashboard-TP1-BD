import psycopg2
from config import config
import datetime

def line():
    print("-------------------------------------------------")

#Checks whether a product exists or not
def check_product_exists(asin):
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM product WHERE asin = %s", (asin,))
    exists = cursor.fetchone()[0] > 0
    cursor.close()
    return exists

#SQL query letter A
def top_reviews(asin):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    # 5 most useful and top rated comments
    sql_query1 = f"""
        SELECT * FROM (
            SELECT ROW_NUMBER() OVER (ORDER BY rate DESC, helpful DESC) AS top,
                costumer, date, rate, vote, helpful
            FROM review
            WHERE asin_product = '{asin}'
        ) AS top_reviews
        WHERE top <= 5
    """

    # 5 most useful and lowest rated comments
    sql_query2 = f"""
        SELECT * FROM (
            SELECT ROW_NUMBER() OVER (ORDER BY rate ASC, helpful DESC) AS top,
                costumer, date, rate, vote, helpful
            FROM review
            WHERE asin_product = '{asin}'
        ) AS top_reviews
        WHERE top <= 5
    """

    try:
        line()
        print("These are the 5 most useful and highest rated comments, where each line follows the format:")
        print("(top,customer,date,rate,votes,helpful)\n")
        cur.execute(sql_query1)
        rows = cur.fetchall()

        for row in rows:
            print(row)
        line()

        print("These are the 5 most useful and highest rated comments, where each line follows the format:")
        print("(top,customer,date,rate,votes,helpful)\n")

        cur.execute(sql_query2)
        rows = cur.fetchall()

        for row in rows:
            print(row)

        line()

    except Exception as e:
        print(f"An error occurred while executing the SQL query: {e}")
    finally:
        cur.close()
        conn.close()

#SQL query letter B
def get_similar_products(asin):
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"""SELECT sp.asin_similar, p.title, p.sales_rank as sales_rank_similar
                        FROM similar_products sp
                        JOIN product p ON sp.asin_similar = p.asin
                        WHERE sp.asin_product = '{asin}' AND p.sales_rank < (
                            SELECT sales_rank
                            FROM product
                            WHERE asin = '{asin}'
                        )
                        ORDER BY p.sales_rank ASC
                        LIMIT 5""")
        rows = cur.fetchall()
        cont = 1
        line()
        
        if len(rows) > 1:
            print(f"Given the product with asin = {asin}, these are the similar products with higher sales than it:\n")
        else:
            print("The product has no similar products with higher sales than it!")
        for product in rows:
            print(f'Product {cont}:\n')
            print(f'asin_similar: {product[0]}')
            print(f'title: {product[1]}')
            print(f'sales_rank: {product[2]}')
            line()
            cont += 1
    except Exception as error:
        print(f"Error: {error}")
    finally:
        cur.close()
        conn.close()

#SQL query letter C
def get_avg_rating_by_day(asin, n):
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""
            SELECT date_trunc('day', date) AS review_date, AVG(rate) AS avg_rating
            FROM review
            WHERE asin_product = %s
            GROUP BY review_date
            ORDER BY review_date
            LIMIT %s
        """, (asin, n,))

        rows = cur.fetchall()
        line()
        print(f"This is the daily evolution of the average ratings of the product with asin = {asin} over {n} days:\n")
        for day in rows:
            data = day[0]
            data_formatada = data.strftime('%Y-%-m-%-d')
            print(f'date: {data_formatada}   average rating: {day[1]:.2f}')

        line()
        cur.close()
        conn.commit()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

#SQL query letter D
def top_10_sold_for_group():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT DISTINCT product_group FROM product")
        books_rows = cur.fetchall()

        for group in books_rows:
            line()
            print(f'Group: {group[0]}')
            print()
            cur.execute("""
                SELECT product.title, product.sales_rank
                FROM product
                WHERE product.product_group = %s AND product.sales_rank >= 1
                ORDER BY product.sales_rank
                LIMIT 10;
            """, (group,))

            rows = cur.fetchall()
            for product in rows:
                print(f'title: {product[0]}')
                print(f'sales_rank: {product[1]}')
                line()

        print("These are the top 10 selling products in each product group!")
        print("NOTE: If there are less than 10 products, it means that the group has no more than 10 products registered!")
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

#SQL query letter E
def get_top_products_by_helpful():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""
            SELECT p.asin, p.title, AVG(r.helpful) as avg_helpful
            FROM product p
            JOIN review r ON p.asin = r.asin_product
            GROUP BY p.asin, p.title
            ORDER BY avg_helpful DESC
            LIMIT 10;
        """)

        rows = cur.fetchall()
        line()
        cont = 1
        for product in rows:
            print(f'Top {cont}:')
            print(f'asin: {product[0]}')
            print(f'title: {product[1]}')
            print(f'average helpful: {product[2]:.2f}')
            line()
            cont += 1
        print("These are the 10 products with the highest average positive helpful reviews!")
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


#SQL query letter F
def get_top_categories_by_helpful():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""
            SELECT ci.name, AVG(r.helpful) as avg_helpful
            FROM category c
            JOIN product p ON c.asin_product = p.asin
            JOIN review r ON r.asin_product = p.asin
            JOIN category_info ci ON c.category_id = ci.category_id
            WHERE r.helpful > 0
            GROUP BY ci.name
            ORDER BY avg_helpful DESC
            LIMIT 5;
        """)
        rows = cur.fetchall()

        line()
        cont = 1
        for row in rows:
            print(f'Top {cont}')
            print(f"category: {row[0]}\naverage Helpful: {row[1]:.2f}")
            cont += 1
        print("\nThese are the 5 product categories with the highest average positive helpful reviews per product!")
        line()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

#SQL query letter G
def get_top_commenters_for_groups():
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    try:
        cur.execute("SELECT DISTINCT product_group FROM product")
        books_rows = cur.fetchall()

        line()
        for group in books_rows:
            print(f'Group: {group[0]}\n')
            cont = 1
            cur.execute("""
                SELECT costumer, COUNT(*) AS total_comments
                FROM review
                INNER JOIN product ON review.asin_product = product.asin
                WHERE product_group = %s
                GROUP BY costumer
                ORDER BY total_comments DESC
                LIMIT 10
            """, (group[0],))
            
            rows = cur.fetchall()
           
            for user in rows:
                print(f'Top {cont}:')
                print(f'costumer: {user[0]}')
                print(f'total_coments: {user[1]}')
                line()
                cont += 1
            print()
        
        print("These are the 10 customers who made the most comments per product group!")
        print("NOTE: If there is a quantity less than 10, it means that the group does not have 10+ clients!")
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

#if __name__ == '__main__':
    #top_reviews('1234565767')
    #get_similar_products('0764546252')
    #get_avg_rating_by_day('0385504209',10)
    #top_10_sold_for_group()
    #get_top_products_by_helpful()
    #get_top_categories_by_helpful()
    #get_top_commenters_for_groups()