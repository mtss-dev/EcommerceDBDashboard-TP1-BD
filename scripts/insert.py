import psycopg2
from config import config


#A função abaixo insere dados na tabela product e similar_products
def add_product(asin,title,product_group,sales_rank, assins_list):
    # statement for inserting a new row into the parts table
    insert_product = "INSERT INTO product(asin,title,product_group,sales_rank) VALUES(%s,%s,%s,%s) RETURNING asin;"
    # statement for inserting a new row into the vendor_parts table
    assing_similar = "INSERT INTO similar_products(asin_similar,asin_id) VALUES(%s,%s)"

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        conn.autocommit = False  # desabilita o modo de commit automático
        cur = conn.cursor()
        cur.execute("BEGIN")  # inicia a transação
        cur.execute(insert_product, (asin,title,product_group,sales_rank))
        row = cur.fetchone()
        if row is not None:
            aid = row[0]
            for asin_similar in assins_list:
                cur.execute(assing_similar, (asin_similar, aid))
            conn.commit()
        else:
            print("Insertion failed")
            conn.rollback()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()  # desfaz a transação em caso de erro
    finally:
        if conn is not None:
            conn.close()

#SELECT asin_similar FROM similar_products WHERE asin_id = '0827229525';

if __name__ == '__main__':
    #insert_product_list([
        #('0827229534','Patterns of Preaching: A Sermon Sampler','Book','396585')])
    add_product('0827229525','Patterns of Preaching: A Sermon Sampler','Book','396585', ('0804215715','156101074X','0687023955','0687074231','082721619X'))