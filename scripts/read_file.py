from insert import *
import re

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

        if 'review' in line:
            reviews = []
            n_review = int(line.split(' ')[4].strip())
            for i in range(n_review):
                line = file.readline()
                result = [x.strip() for x in re.split(r"\s+|cutomer: |rating: |votes: |helpful:|\*|\n", line) if x.strip()]
                reviews.append(result)

            add_product(asin,title,group,salesrank,similar,reviews)                


if __name__ == '__main__':
    file = open("teste.txt", "r")
    populate()