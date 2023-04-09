import psycopg2
from config import config

#A função abaixo insere dados somente na tabela product
def insert_product_list(product_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO product(asin,title,product_group,sales_rank) VALUES(%s,%s,%s,%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,product_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


#A função abaixo insere dados na tabela product e similar_products
def add_product(asin,title,product_group,sales_rank, assins_list):
    # statement for inserting a new row into the parts table
    insert_product = "INSERT INTO product(asin,title,product_group,sales_rank) VALUES(%s,%s,%s,%s) RETURNING id;"
    # statement for inserting a new row into the vendor_parts table
    assing_similar = "INSERT INTO similar_products(asin_similar,product_id) VALUES(%s,%s)"

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # insert a new part
        cur.execute(insert_product, (asin,title,product_group,sales_rank,))
        # get the part id
        id = cur.fetchone()[0]
        # assign parts provided by vendors
        for asin_similar in assins_list:
            cur.execute(assing_similar, (asin_similar, id))

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




if __name__ == '__main__':
    #insert_product_list([
        #('0827229534','Patterns of Preaching: A Sermon Sampler','Book','396585')])
    add_product('0827229534','Patterns of Preaching: A Sermon Sampler','Book','396585', ('0804215715','156101074X','0687023955','0687074231','082721619X'))