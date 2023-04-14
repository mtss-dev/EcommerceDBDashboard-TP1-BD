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

