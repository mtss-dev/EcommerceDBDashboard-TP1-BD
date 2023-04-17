import psycopg2
from config import config

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
        print("-------------------------------------------------")
        print("Estes são os 5 comentários mais úteis e com maior avaliação, onde cada linha segue o formato:")
        print("(top,customer,date,rate,votes,helpful)\n")
        cur.execute(sql_query1)
        rows = cur.fetchall()

        # Exibição dos resultados
        for row in rows:
            print(row)

        print("-------------------------------------------------")

        print("Estes são os 5 comentários mais úteis e com menor avaliação, onde cada linha segue o formato:")
        print("(top,customer,date,rate,votes,helpful)\n")
        # Execução da consulta SQL
        cur.execute(sql_query2)
        rows = cur.fetchall()
        # Exibição dos resultados
        for row in rows:
            print(row)

        print("-------------------------------------------------")

    except Exception as e:
        print(f"Ocorreu um erro ao executar a consulta SQL: {e}")
    finally:
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
        print("-------------------------------------------------")
        print(f'Categoria: {group[0]}')
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
            print(f'Título: {product[0]}')
            print(f'Sales_Rank: {product[1]}')
            print("-------------------------------------------------")
        print()
        
    cur.close()

if __name__ == '__main__':
    #top_10_vendidos_por_grupo()
    #top_reviews('1234565767')