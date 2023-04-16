import time
from create_database import create_db
from create_tables import create_tables
from insert import add_products
from read_file import data_extraction
from drop_database import drop_db

if __name__ == '__main__':
    start_time = time.time()
    
    create_db()
    create_tables()
    filename = 'amazon-meta.txt'
    products = data_extraction(filename)
    add_products(products)
    #drop_db()
    
    end_time = time.time()
    
    total_time = end_time - start_time
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)
    
    print(f"All operations completed successfully in {minutes} minutes and {seconds} seconds.")