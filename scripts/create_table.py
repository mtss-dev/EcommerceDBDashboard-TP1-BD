import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE SEQUENCE product_id_seq
            START WITH 0
            INCREMENT BY 1
            MINVALUE 0
            NO MAXVALUE
            CACHE 1;
        CREATE TABLE product (
            id INTEGER DEFAULT NEXTVAL('product_id_seq') PRIMARY KEY,
            asin varchar(10)  NOT NULL,
            title varchar(255)  NOT NULL,
            product_group varchar(10)  NOT NULL,
            sales_rank int  NOT NULL
        )
        """,
        """ 
        CREATE TABLE review (
            product_id int  NOT NULL,
            costumer varchar(20)  NOT NULL,
            date date  NOT NULL,
            rate int  NOT NULL,
            vote int  NOT NULL,
            helpful int  NOT NULL,
            CONSTRAINT review_pk PRIMARY KEY (product_id,costumer),
            FOREIGN KEY (product_id)
                REFERENCES product (id)
                NOT DEFERRABLE 
                INITIALLY IMMEDIATE
        )
        """,
        """
        CREATE TABLE similar_products (
            product_id int  NOT NULL,
            asin_similar varchar(10)  NOT NULL,
            CONSTRAINT similar_products_pk PRIMARY KEY (product_id,asin_similar),
            FOREIGN KEY (product_id)
                REFERENCES product (id)  
                NOT DEFERRABLE 
                INITIALLY IMMEDIATE
        )
        """,
        """
        CREATE TABLE category (
            product_id int  NOT NULL,
            id int  NOT NULL,
            CONSTRAINT category_pk PRIMARY KEY (id),
            FOREIGN KEY (product_id)
                REFERENCES product (id)  
                NOT DEFERRABLE 
                INITIALLY IMMEDIATE
        )
        """,
        """
        CREATE TABLE category_info (
            category_id int  NOT NULL,
            name varchar(50)  NOT NULL,
            CONSTRAINT category_info_pk PRIMARY KEY (category_id,name),
            FOREIGN KEY (category_id)
                REFERENCES category (id)  
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