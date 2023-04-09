import psycopg2
from config import config

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


if __name__ == '__main__':
    insert_product_list([
        ('0827229534','Patterns of Preaching: A Sermon Sampler','Book','396585')
    ])