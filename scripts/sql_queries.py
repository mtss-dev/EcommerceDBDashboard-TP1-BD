import psycopg2
from config import config
import datetime

def line():
    print("-------------------------------------------------")

def check_product_exists(asin):
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM product WHERE asin = %s", (asin,))
    exists = cursor.fetchone()[0] > 0
    cursor.close()
    return exists

#Letra A
def top_reviews(asin):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    # 5 comentários mais úteis e com maior avaliação
    sql_query1 = f"""
        SELECT * FROM (
            SELECT ROW_NUMBER() OVER (ORDER BY rate DESC, helpful DESC) AS top,
                costumer, date, rate, vote, helpful
            FROM review
            WHERE asin_product = '{asin}'
        ) AS top_reviews
        WHERE top <= 5
    """

    # 5 comentários mais úteis e com menor avaliação
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
        # Execução da consulta SQL
        line()
        print("Estes são os 5 comentários mais úteis e com maior avaliação, onde cada linha segue o formato:")
        print("(top,customer,date,rate,votes,helpful)\n")
        cur.execute(sql_query1)
        rows = cur.fetchall()

        # Exibição dos resultados
        for row in rows:
            print(row)

        line()

        print("Estes são os 5 comentários mais úteis e com menor avaliação, onde cada linha segue o formato:")
        print("(top,customer,date,rate,votes,helpful)\n")
        # Execução da consulta SQL
        cur.execute(sql_query2)
        rows = cur.fetchall()
        # Exibição dos resultados
        for row in rows:
            print(row)

        line()

    except Exception as e:
        print(f"Ocorreu um erro ao executar a consulta SQL: {e}")
    finally:
        cur.close()
        conn.close()

#Letra B
def get_similar_products(asin):
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
    for product in rows:
        print(f'Product {cont}:\n')
        print(f'asin_similar: {product[0]}')
        print(f'title: {product[1]}')
        print(f'sales_rank: {product[2]}')
        line()
        cont += 1
    cur.close()
    conn.close()

#Letra C
def get_avg_rating_by_day(asin,n):
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
    print(f"Daily evolution of the evaluation averages on {n} days:\n")
    for day in rows:
        data = day[0]
        data_formatada = data.strftime('%Y-%-m-%-d')
        print(f'date: {data_formatada}   avg_rating: {day[1]:.2f}')


    cur.close()
    conn.close()


#Letra D
def top_10_sold_for_group():

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT product_group FROM product")
    books_rows = cur.fetchall()
    
    for group in books_rows:
        line()
        print(f'Category: {group[0]}')
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
        print()
        
    cur.close()

if __name__ == '__main__':
    #top_10_vendidos_por_grupo()
    #top_reviews('1234565767')
    #get_similar_products('0764546252')
    get_avg_rating_by_day('0385504209',10)