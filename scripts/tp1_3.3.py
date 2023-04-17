import os
from sql_queries import *

def interface():

    quited = invalid = False
    while (not quited):
        print('------------------------Bem vindo ao Dashboard---------------------')
        print('selecione uma opção(q para sair): \n')
        print(""" a) Dado um produto:
        Listar os 5 comentários mais úteis e com maior avaliação
        Listar os 5 5 comentários mais úteis e com menor avaliação\n""")
        print(""" b) Dado um produto:
        Listar os produtos similares com maiores vendas do que ele\n""")
        print(""" c) Dado um produto: 
        Mostrar a evolução diária das médias de avaliação ao longo
        do intervalo de tempo coberto no arquivo de entrada\n""")
        print(""" d) Listar os 10 produtos líderes de venda em cada grupo de
    produtos\n""")
        print(""" e) Listar os 10 produtos com a maior média de  avaliações úteis
    positivas por produto\n""")
        print(""" f) Listar a 5 categorias de produto com a maior média de
    avaliações úteis positivas por produto\n""")
        print(""" g) Listar os 10 clientes que mais fizeram comentários por
    grupo de produto\n""")
        if invalid:
            print('Comando inválido!')
        quited, invalid = options(input())
        os.system('cls' if os.name == 'nt' else 'clear')


def options(selected):

    if selected == 'a':
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            entry = input('Insira o ASIN de um produto (r para retornar): ')
            
            if confirm_return(entry):
                return False, False
            
            if check_product_exists(entry):
                top_reviews(entry)
                input("Press Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Produto não encontrado!")

    elif selected == 'b':
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            entry = input('Insira o ASIN de um produto (r para retornar): ')
        
            
            if confirm_return(entry):
                return False, False
            
            if check_product_exists(entry):
                get_similar_products(entry)
                input("Press Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Produto não encontrado!")
    
    elif selected == 'c':
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            entry = input('Insira o ASIN de um produto (r para retornar): ')
            if confirm_return(entry):
                return False, False

            n = int(input('Insira a quantidade de dias que deseja analisar: '))
            
            if check_product_exists(entry):
                get_avg_rating_by_day(entry,n)
                input("Press Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Produto não encontrado!")
    
    elif selected == 'd':
        os.system('cls' if os.name == 'nt' else 'clear')

        top_10_sold_for_group()

        input("Press Enter para continuar...")
        return False, False
    
    elif selected == 'e':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'f':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'g':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        input("Press Enter para continuar...")
        return False, False
    elif selected == 'q':
        os.system('cls' if os.name == 'nt' else 'clear')
        #insira a função aqui
        print('volte sempre! :D')
        return True, False
    else:
        return False, True

def confirm_return(entry): 
    if entry == 'r':
        return True

if __name__ == '__main__':
    interface()