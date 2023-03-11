# Descrição:
Este script python realiza buscas no google, recebendo termos a serem pesquisados através de um arquivo de entrada. O arquivo de entrada deve conter os termos a serem buscados, um em cada linha. A primeira busca é gravada em um arquivo chamado 'saída 1.txt' onde, cada linha do arquivo é formada por o termo pesquisado e uma url correspondente, separados por '|'. A partir da segunda chamada o script analisa se ouveram mudanças nas urls e grava as mudanças encontradas em um arquivo chamado 'saída 2_[data]_[hora]', onde, data e hora correspondem a data e hora no momento da busca.

# Como executar o script.
- Abra a pasta que contém os arquivos do script no terminal.
- Instale as dependências com o comando:
    ```'pip install -r requeriments.txt'```
- Crie um arquivo .txt com os termos a serem pesquisados no google.
- Execute o script com o comando 'python core.py [termos.txt]' onde [termos.txt] é o nome do arquivo que você criou.

# Observações:
O scrip aceita um terceiro argumento que é o número de urls buscadas por cada termo. Se esse parâmetro não for definido serão buscadas somente 10 URLs.
Exemplo:
'python core.py [termos.txt] 50' lista 50 urls por cada termo.
