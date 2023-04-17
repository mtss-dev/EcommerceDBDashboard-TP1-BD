import psycopg2
from config import config


def top_10_vendidos_por_grupo():

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
    top_10_vendidos_por_grupo()