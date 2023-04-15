import psycopg2
from config import config

#A função abaixo insere dados na tabela product e similar_products
def add_product(asin,title,product_group,sales_rank, assins_list,review_list,categories_list):
    # statement for inserting a new row into the product table
    insert_product = "INSERT INTO product(asin,title,product_group,sales_rank) VALUES(%s,%s,%s,%s) RETURNING asin;"
    # statement for inserting a new row into the similar_products table
    insert_assin_similars = "INSERT INTO similar_products(asin_similar,asin_product) VALUES(%s,%s)"
    # statement for inserting a new row into the review table
    insert_product_review = "INSERT INTO review(asin_product,date,costumer,rate,vote,helpful) VALUES(%s,%s,%s,%s,%s,%s)"
    # statement for inserting a new row into the category_info table
    insert_category_info = "INSERT INTO category_info(category_id,name) VALUES(%s,%s) ON CONFLICT DO NOTHING"
    # statement for inserting a new row into the category table
    insert_category = "INSERT INTO category(asin_product,category_id) VALUES(%s,%s) ON CONFLICT DO NOTHING"


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
            if len(assins_list) >= 1:
                for asin_similar in assins_list:
                    cur.execute(insert_assin_similars, (asin_similar, asin_product))
            if len(review_list) >= 1:
                for review in review_list:
                    cur.execute(insert_product_review, (asin_product,review[0],review[1],review[2],review[3],review[4]))
            if len(categories_list) >= 1:
                for categorie in categories_list:
                    print(categorie[0])
                    print(categorie[1])
                    cur.execute(insert_category_info, (categorie[1], categorie[0]))
                    cur.execute(insert_category,(asin_product,categorie[1]))
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
    #similar_products = []
    #similar_products = [('0738700827','1567184960','1567182836','0738700525','0738700940'),('0804215715','156101074X','0687023955','0687074231','082721619X')]
    #products = [('0738700797','Candlemas: Feast of Flames','Book',168596),('0827229525','Patterns of Preaching: A Sermon Sampler','Book',396585)]

    categories = [['5174','Music'],['5174','Music'],['5174','Music'],['301668','Styles'],['63926','General',['63926','General']]]
    similar_products = ['0738700827','1567184960','1567182836','0738700525','0738700940']
    reviews = [['2001-2-8','AWHGCJOOZBTB5',5,10,10],['2001-10-12','XXXXXXXXXXXXX',7,9,8]]
    add_product('0738700797','Candlemas: Feast of Flames','Book',168596, similar_products,reviews,categories)