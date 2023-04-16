from insert2 import *
import re

def line_generator(file, n_cat):
    for i in range(n_cat):
        line = file.readline()
        if not line:
            break
        yield line

def populate():
    try:
        with open('teste.txt', 'r') as file:
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
                        result = re.findall(r"\|(\w+)\[(\d+)\]", cat_line)
                        categories.append(result)

                    # Criar a lista de lista com o nome e id extraídos
                    results = [[item[0], item[1]] for sublist in categories for item in sublist]
                    product['categories'] = results
                    products.append(product)
                    product = {}
                    
            return products
            
    except FileNotFoundError as e:
        print(f"O arquivo não foi encontrado: {e}")
    except ValueError as e:
        print(f"O valor é inválido: {e}")
    except IndexError as e:
        print(f"Ocorreu um erro de índice: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    products = populate()
    add_products(products)