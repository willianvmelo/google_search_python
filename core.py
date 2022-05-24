# Importando pacotes necessários

import sys
from googlesearch import search
from datetime import datetime
import os.path

# Verificando se o script foi chamado corretamente.

if len(sys.argv):
    arquivo = sys.argv[1]
else:
    print("Sintaxe 'python meu_programa.py [arquivo]’")
    sys.exit()


# Verificando se o usuário definiu a quantidade de URLS por termo.
# Se não for definida a quantidade de URLS utilizaremos o padrão de 10.

if len(sys.argv) > 2:
    num_urls = int(sys.argv[2])

else:
    num_urls = 10

# Abrindo o arquivo de entrada para leitura.
arquivo_entrada = open(arquivo, 'r')

# Verificando se existe um arquivo saída 1.txt no diretório atual.

if not (os.path.isfile('saída 1.txt')):

    # Abrindo arquivo de saída.
    arquivo_saida = open(
        'saída 1.txt', "w+")

    # Realizando a busca no Google e gravando as saídas no documento de Saída.

    for termo in arquivo_entrada:
        
        query = termo.rstrip('\n')

        busca = search(
            query, tld="co.in", num=num_urls, stop=num_urls, pause=2)

        # Gravando saída 1
        for url in busca:
            arquivo_saida.write(query+'|' + url+'\n')
        

    # Fechando arquivos
    arquivo_entrada.close()
    arquivo_saida.close()

else:
    # Abrindo arquivo de saída.
    saida_1 = open(
        'saída 1.txt', "r")
    
   # realizando pesquisa no google 
    segunda_busca = []   
    for termo in arquivo_entrada:
    
        query = termo.rstrip('\n')

        busca = search(
            query, tld="co.in", num=num_urls, stop=num_urls, pause=2)
        for url in busca:
            segunda_busca.append(query+'|'+url+'\n')

   # Comparando os  dados de saída 1.txt com os da segunda busca e obtendo a diferença

    a = set(saida_1)
    b = set(segunda_busca)
    urls_diferentes = list(b-a)

   # Gravando saída 2
   
    arquivo_saida_2 = open(
    'saída 2_'+datetime.today().strftime('%d-%m-%Y_%H:%M:%S')+'.txt', "w+")

    for url in urls_diferentes:
        arquivo_saida_2.write(url)

   # Fechando arquivos     
    arquivo_entrada.close()
    arquivo_saida_2.close()   
