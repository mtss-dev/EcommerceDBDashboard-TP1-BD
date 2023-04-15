from insert import *
import re

def line_generator(file, n_cat):
    for i in range(n_cat):
        line = file.readline()
        if not line:
            break
        yield line

def populate():
    try:
        with open('amazon-meta.txt', 'r') as file:
            categories = []
            asin = title = group = salesrank = ''
            for line in file:
                if 'discontinued' in line:
                    asin = title = group = salesrank = ''
                    continue
                match = re.search(r"ASIN:\s*(.*)", line)
                if match:
                    asin = match.group(1).strip()
                    continue
                match = re.search(r"title:\s*(.*)", line)
                if match:
                    title = match.group(1).strip()
                    continue
                match = re.search(r"group:\s*(.*)", line)
                if match:
                    group = match.group(1).strip()
                    continue
                match = re.search(r"salesrank:\s*(.*)", line)
                if match:
                    salesrank = match.group(1).strip()
                    continue
                if 'similar' in line:
                    similar = [x.strip() for x in line.split()[2:]]
                        
                if 'categories' in line:
                    categories = []
                    n_cat = int(line.split()[1])
                    for cat_line in line_generator(file, n_cat):
                        result = re.findall(r"\|(\w+)\[(\d+)\]", cat_line)
                        categories.append(result)

                    # Criar a lista de lista com o nome e id extraídos
                    results = [[item[0], item[1]] for sublist in categories for item in sublist]
                    add_product(asin,title,group,salesrank,similar,[],results)  
                    asin = title = group = salesrank = ''  
    except FileNotFoundError as e:
        print(f"O arquivo não foi encontrado: {e}")
    except ValueError as e:
        print(f"O valor é inválido: {e}")
    except IndexError as e:
        print(f"Ocorreu um erro de índice: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == '__main__':
    populate()