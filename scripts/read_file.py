def read_asin(line):
    if 'ASIN' in line:
        asin = line.split("ASIN: ")[1]
    return asin

def read_title(line):
    if 'title' in line:
        title = line.split("title: ")[1]
    return title

def read_group(line):
    if 'group' in line:
        group = line.split("group: ")[1]
    return group

def read_salesrank(line):
    if 'salesrank' in line:
        salesrank = line.split("salesrank: ")[1]
    return salesrank

def build_product(file):
    while True:
        line = file.readline()
        asin = read_asin(file.readline())


if __name__ == '__main__':
    file = open("teste.txt", "r")
    print(build_product(file))
