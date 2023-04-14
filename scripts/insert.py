import psycopg2
from config import config


#A função abaixo insere dados na tabela product e similar_products
def add_product(asin,title,product_group,sales_rank, assins_list):
    # statement for inserting a new row into the product table
    insert_product = "INSERT INTO product(asin,title,product_group,sales_rank) VALUES(%s,%s,%s,%s) RETURNING asin;"
    # statement for inserting a new row into the similar_products table
    insert_assin_similars = "INSERT INTO similar_products(asin_similar,asin_product) VALUES(%s,%s)"
    # statement for inserting a new row into the review table
    insert_product_review = "INSERT INTO review(asin_product,costumer,date,rate,vote,helpful) VALUES(%s,%s,%s,%d,%d,%d)"

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
            asin_product = row[0]
            if len(assins_list) > 1:
                for asin_similar in assins_list:
                    cur.execute(insert_assin_similars, (asin_similar, asin_product))
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

#if __name__ == '__main__':
    #similar_products = []
    #similar_products = [('0738700827','1567184960','1567182836','0738700525','0738700940'),('0804215715','156101074X','0687023955','0687074231','082721619X')]
    #products = [('0738700797','Candlemas: Feast of Flames','Book',168596),('0827229525','Patterns of Preaching: A Sermon Sampler','Book',396585)]
    # file = open("teste.txt", "r")
    # # file = open("amazon-meta.txt", "r")

    # for line in file:
    #     if 'discontinued' in line:
    #         asin = title = group = salesrank = ''
    #         continue
    #     if 'ASIN' in line:
    #         asin = line.split("ASIN: ")[1]
    #         continue
    #     if 'title' in line:
    #         title = line.split("title: ")[1]
    #         continue
    #     if 'group' in line:
    #         group = line.split("group: ")[1]
    #         continue
    #     if 'salesrank' in line:
    #         salesrank = line.split("salesrank: ")[1]
    #         continue
    #     if 'categories' in line:
    #          add_product(asin,title,group,salesrank, [])
    
    # similar_products = ['0738700827','1567184960','1567182836','0738700525','0738700940']
    # add_product(asin,title,group,salesrank, similar_products)