from insert import *
import re

def line_generator(file, n_cat):
    for i in range(n_cat):
        line = file.readline()
        if not line:
            break
        yield line

def data_extraction(filename):
    try:
        with open(filename, 'r') as file:
            products = []
            product = {}
            for line in file:
                if 'discontinued' in line:
                    products.append(product)
                    product = {}
                    continue
                match = re.search(r"ASIN:\s*(.*)", line)
                if match:
                    product['asin'] = match.group(1).strip()
                    continue
                match = re.search(r"title:\s*(.*)", line)
                if match:
                    product['title'] = match.group(1).strip()
                    continue
                match = re.search(r"group:\s*(.*)", line)
                if match:
                    product['product_group'] = match.group(1).strip()
                match = re.search(r"salesrank:\s*(.*)", line)
                if match:
                    product['sales_rank'] = match.group(1).strip()
                    continue
                if 'similar' in line:
                    product['similar'] = [x.strip() for x in line.split()[2:]]
                        
                if 'categories' in line:
                    categories = []
                    n_cat = int(line.split()[1])
                    for cat_line in line_generator(file, n_cat):

                        result = re.findall(r"\|(.*?)\[(\d+)\]", cat_line)
                        categories.append(result)

                    # Create list list with extracted name and id
                    results = [[item[0], item[1]] for sublist in categories for item in sublist]
                    product['categories'] = results
                
                if "reviews" in line:
                    aux = []
                    reviews = re.findall(r'(\d{4}-\d{1,2}-\d{1,2})\s+cutomer:\s+(\w+)\s+rating:\s+(\d+)\s+votes:\s+(\d+)\s+helpful:\s+(\d+)', file.readline())
                    while reviews:
                        aux.append(reviews)
                        reviews = re.findall(r'(\d{4}-\d{1,2}-\d{1,2})\s+cutomer:\s+(\w+)\s+rating:\s+(\d+)\s+votes:\s+(\d+)\s+helpful:\s+(\d+)', file.readline())
                    if len(aux) > 0:
                        product['reviews'] = aux
                    products.append(product)
                    product = {}

            print("Reading of the file finished successfully!")
            return products
            
    except FileNotFoundError as e:
        print(f"The file was not found: {e}")
    except ValueError as e:
        print(f"The value is invalid: {e}")
    except IndexError as e:
        print(f"An index error has occurred: {e}")
    except Exception as e:
        print(f"An error has occurred: {e}")