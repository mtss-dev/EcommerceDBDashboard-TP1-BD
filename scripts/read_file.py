
def populate():

    file = open('teste.txt', 'r')

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
        if 'categories' in line:
            print(asin, title, group, salesrank)
            continue

if __name__ == '__main__':
    file = open("teste.txt", "r")
    populate()
