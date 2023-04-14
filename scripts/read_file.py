from insert import *

def populate():

    file = open('teste.txt', 'r')
    categories = []
    for line in file:
        if 'discontinued' in line:
            asin = title = group = salesrank = ''
            continue
        if 'ASIN' in line:
            asin = line.split("ASIN: ")[1]
            continue
        if 'title' in line:
            title = line.split("title: ")[1]
            continue
        if 'group' in line:
            group = line.split("group: ")[1]
            continue
        if 'salesrank' in line:
            salesrank = line.split("salesrank: ")[1]
            continue
        if 'similar' in line:
            similar = line.split()[2:]
        if 'categories' in line:
            add_product(asin, title, group, salesrank,[])
            continue

if __name__ == '__main__':
    file = open("teste.txt", "r")
    populate()