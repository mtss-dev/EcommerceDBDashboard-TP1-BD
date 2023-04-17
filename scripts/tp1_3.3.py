import os
from sql_queries import *

def interface():
    quited = invalid = False
    while (not quited):
        print('------------------------Welcome to the Dashboard---------------------')
        print('select an option(q to quit): \n')
        print(""" a) Given a product:
        List the 5 most useful and highest rated reviews
        List the 5 most useful and lowest rated reviews\n""")
        print(""" b) Given a product:
        List the products that are similar and have higher sales than it\n""")
        print(""" c) Given a product:
        Show the daily evolution of the rating averages
        over the desired time interval\n""")
        print(""" d) List the 10 best selling products in each product group\n""")
        print(""" e) List the 10 products with the highest average of positive
    useful reviews per product\n""")
        print(""" f) List the top 5 product categories with the highest average of positive
    useful reviews per product\n""")
        print(""" g) List the top 10 customers who made the most comments per
    product group\n""")
        if invalid:
            print('Invalid command!')
        quited, invalid = options(input())
        os.system('cls' if os.name == 'nt' else 'clear')

def options(selected):
    if selected == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            entry = input('Insert the ASIN of a product (r to return): ')
            
            if confirm_return(entry):
                return False, False
            
            if check_product_exists(entry):
                top_reviews(entry)
                input("Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Product not found!")

    elif selected == 'b':
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            entry = input('Insert the ASIN of a product (r to return): ')
        
            if confirm_return(entry):
                return False, False
            
            if check_product_exists(entry):
                get_similar_products(entry)
                input("Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Product not found!")

    elif selected == 'c':
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            entry = input('Insert the ASIN of a product (r to return): ')
            if confirm_return(entry):
                return False, False

            n = int(input('Insert the number of days you want to analyze: '))
            
            if check_product_exists(entry):
                get_avg_rating_by_day(entry,n)
                input("Press Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Product not found!")

    elif selected == 'd':
        os.system('cls' if os.name == 'nt' else 'clear')

        top_10_sold_for_group()

        input("Press Enter to continue...")
        return False, False

    elif selected == 'e':
        os.system('cls' if os.name == 'nt' else 'clear')

        get_top_products_by_helpful()

        input("Press Enter to continue...")
        return False, False
    elif selected == 'f':
        os.system('cls' if os.name == 'nt' else 'clear')

        get_top_categories_by_helpful()

        input("Press Enter to continue...")
        return False, False
    elif selected == 'g':
        os.system('cls' if os.name == 'nt' else 'clear')

        get_top_commenters_for_groups()

        input("Press Enter to continue...")
        return False, False
    elif selected == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Goodbye! :D')
        return True, False
    else:
        return False, True

def confirm_return(entry): 
    if entry == 'r':
        return True

if __name__ == '__main__':
    interface()