import requests

h = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"}

while True:
    inicio = int(input('digite a pagina inicial: '))
    if inicio < 1 or inicio > 50:
        print('Digite um numero no range de 1 a 50!')
    else:
        final = int(input('digite a pagina final: '))
        if final < 1 or final > 50:
            print('Digite um numero no range de 1 a 50!')
        elif final < inicio:
            print('digite um valor maior do que o inicial!')
        else:
            break

print()

try:

    with open(f'contas{inicio}_{final}.txt', 'r',encoding='utf-8') as arquivo:
        print('o arquivo ja existe,aqui esta ele: ')
        print()
        for linha in arquivo:
            print(linha.rstrip())

except (FileExistsError,FileNotFoundError):
    print('Arquivo criado com sucesso,aqui esta: ')
    print()
    for i in range(inicio,final+1):
        url = f'https://www.leagueofgraphs.com/rankings/summoners/br/page-{i}'
        response = requests.get(url,headers=h)
        site = response.text
        with open (f'contas{inicio}_{final}.txt','a',newline='\n',encoding='UTF-8') as arquivo:
            for line in site.splitlines():
                    if '<span class="name">' in line:
                        maiorQue = line.find('>') + 1
                        menorQue = line.find('<', maiorQue)
                        nick = line[maiorQue:menorQue]
                        arquivo.write(nick + '\n')
                        print(nick)




'''
web scraping

receber dois input de valores que podem ir de 1 a 50
criar um arquivo txt com o formato de nome: contas{inicio}_{fim}.txt baseado nos dois numeros passados.
retornar os nicks com as # de cada pagina no range passado no site 

https://www.leagueofgraphs.com/rankings/summoners/br/page- (no final por a pagina que voce quer)

puxar só regiao br

se a pessoa pedir um range que ja foi pedido anteriormente(o txt ja existe) o programa fala que ja existe
e retorna o conteudo desse txt.
coisas para levar em consideração: o inicio tem que ser um numero menor que o fim.
se o inicio e fim forem iguais retorne so a pagina pedida.
ex: 1 e 1 cria contas1_1.txt
regras: nao usar o chatgpt

'''