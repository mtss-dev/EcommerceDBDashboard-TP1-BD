from insert import *

def populate():

    file = open('teste.txt', 'r')
    categories = []
    for line in file:
        if 'discontinued' in line:
            asin = title = group = salesrank = ''
            continue
        if 'ASIN' in line:
            asin = line.split("ASIN: ")[1].strip()
            continue
        if 'title' in line:
            title = line.split("title: ")[1].strip()
            continue
        if 'group' in line:
            group = line.split("group: ")[1].strip()
            continue
        if 'salesrank' in line:
            salesrank = line.split("salesrank: ")[1].strip()
            continue
        if 'similar' in line:
            similar = line.split()[2:]
            for i in range(len(similar)):
                similar[i] = similar[i].strip()
        if 'categories' in line:
            add_product(asin, title, group, salesrank,similar)
            continue

if __name__ == '__main__':
    file = open("teste.txt", "r")
    populate()