import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE product (
            asin varchar(15)  NOT NULL PRIMARY KEY,
            title varchar(500)  NOT NULL,
            product_group varchar(10)  NOT NULL,
            sales_rank int  NOT NULL
        )
        """,
        """
        CREATE SEQUENCE review_id_seq
            START WITH 0
            INCREMENT BY 1
            MINVALUE 0
            NO MAXVALUE
            CACHE 1;
        CREATE TABLE review (
            id INTEGER DEFAULT NEXTVAL('review_id_seq'),
            asin_product varchar(15)  NOT NULL,
            costumer varchar(20)  NOT NULL,
            date date  NOT NULL,
            rate int  NOT NULL,
            vote int  NOT NULL,
            helpful int  NOT NULL,
            CONSTRAINT review_pk PRIMARY KEY (id,asin_product,costumer),
            FOREIGN KEY (asin_product)
                REFERENCES product (asin)
                ON DELETE CASCADE
                NOT DEFERRABLE 
                INITIALLY IMMEDIATE
        )
        """,
        """
        CREATE TABLE similar_products (
            asin_product  varchar(15)  NOT NULL,
            asin_similar varchar(15),
            CONSTRAINT similar_products_pk PRIMARY KEY (asin_product ,asin_similar),
            FOREIGN KEY (asin_product )
                REFERENCES product (asin)  
                ON DELETE CASCADE
                NOT DEFERRABLE 
                INITIALLY IMMEDIATE
        )
        """,
        """
        CREATE TABLE category_info (
            category_id int  NOT NULL PRIMARY KEY,
            name varchar(50)  NOT NULL 
        )
        """,
        """
        CREATE TABLE category (
            asin_product  varchar(15)  NOT NULL,
            category_id int  NOT NULL,
            CONSTRAINT category_pk PRIMARY KEY (asin_product ,category_id),
            FOREIGN KEY (asin_product)
                REFERENCES product (asin)  
                ON DELETE CASCADE
                NOT DEFERRABLE 
                INITIALLY IMMEDIATE,
            FOREIGN KEY (category_id)
                REFERENCES category_info (category_id)  
                ON DELETE CASCADE
                NOT DEFERRABLE 
                INITIALLY IMMEDIATE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()