from create_database import create_db
from create_tables import create_tables
from insert import add_products
from read_file import data_extraction
from drop_database import drop_db

if __name__ == '__main__':
    create_db()
    create_tables()
    filename = 'teste.txt'
    products = data_extraction(filename)
    add_products(products)
    #drop_db()
    print("All operations completed successfully!")