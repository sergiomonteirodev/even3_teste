# even3_teste

 Sistema/funcionalidades criada para participação na seleção da even3, foi usado como linguagem backend o python e seu microframework Flask, bem como para o frontend: HTML, CSS(BOOSTRAP4) e JS. Para envio dos emails usei o modulo sendgrid para python.
OBS: Esse passo a passo supõe que se tenha conhecimento necessario em S.O linux e linguagem de programação python, tal qual, o gerenciador de pacotes pip e criação de ambientes virtuais usando virtualenv.
 
# CONFIGURANDO O SENDGRID:
 
1º - Para criar um ambiente desenvolvimento é necessario executar os seguintes comandos:

    $ echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
    $ echo "sendgrid.env" >> .gitignore
    $ source ./sendgrid.env
    
# CONFIGURANDO AS DEPENDÊNCIAS:

2º - Caso deseje (é aconselhavel) criar ambiente virtual usando virtualenv :

    $ virtualenv env
    
3º Instalar as dependências do  a partir do aqruivo requirements.txt
    
    $ pip install -r requirements.txt

# RODANDO O SISTEMA:

4º Executar o comando:
    
    $ python run.py

# ACESSAR O SISTEMA:

5º Acessar navegador
    
    Digitar no browser/navegador de sua preferência: 
    localhost:5000
    



