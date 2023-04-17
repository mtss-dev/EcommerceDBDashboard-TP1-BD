import re

def populate():

    with open('teste.txt', 'r') as file:
        data = file.read()
        items = re.findall(r'ASIN:.*?(?=Id:|$)', data, re.DOTALL)

    products = []

    for item in items:
        product = {}
        
        if 'discontinued product' in item:
            continue

        asin = re.search(r'ASIN:\s+(\w+)\n', item)
        if asin:
            product['asin'] = asin.group(1)

        title = re.search(r'title:\s*(.*)\n', item)
        if title:
            product['title'] = title.group(1)

        group = re.search(r'group:\s+(.*)\n', item)
        if group:
            product['group'] = group.group(1)

        salesrank = re.search(r'salesrank:\s+(.*)\n', item)
        if salesrank:
            product['sales_rank'] = salesrank.group(1)

        similar = re.search(r'similar:\s+(.*)\n', item)
        if similar:
            product['similar'] = similar.group(1).split()[1:]

        categories = re.findall(r'categories:\s\d+([\s\S]*?)reviews:', item)
        if categories:
            temp = re.findall(r'\|(.*?)\[(\d+)\]', categories[0])
            product['categories'] = temp

        reviews =  re.findall(r'(\d{4}-\d{1,2}-\d{1,2})\s+cutomer:\s+(\w+)\s+rating:\s+(\d+)\s+votes:\s+(\d+)\s+helpful:\s+(\d+)', item)
        if reviews:
            product['reviews'] = reviews
            
        products.append(product)
        print(item)
        break
        

    print(products[0])

populate()