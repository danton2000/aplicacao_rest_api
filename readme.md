# AVALIAÇÃO 1: Consultando dados de uma API e armazenando em um Banco de Dados
## Objetivo:
    Escrever uma aplicação em Python que:
    Consulte dados em alguma API Pública de escolha livre
    Insira os dados recebidos em alguma base relacional ou noSQL (MongoDB, MySQL, etc...)
    Crie consultas para analisar os dados recebidos
## Recomendações:
    Não usar as API's que já utilizamos em aula como exemplos
    Não tem limite mínimo de registros para importar na base, mas vamos tentar colocar uma quantidade relevante de dados que faça sentido criar uma base de dados para isso
    Tentem buscar informações relevantes que deem sentido à análise que vocês vão fazer com as consultas
    Entregável:
    Postem um arquivo com o nome_de_voces.md no formato markdown (igual aos arquivos que eu tenho postado para vocês) com informações da API, um exemplo de dado que ela retorna, o código que vocês criaram e exemplos de consultas criadas.
## Prazo:
    Até as 23:59 do dia 26/09/2024!!!
    Vale nota?
    Sim! o Trabalho corresponde à nossa primeira avaliação da disciplina (que irá compor o conceito final) e a presença do sábado letivo de 21/09.
    Alguns exemplos de API's públicas (algumas necessitam cadastro e uso de tokens, postei um exemplo de implementação em api_auth.md na pasta da aula 5):
    Catálogo de APIs Governamentais: https://www.gov.br/conecta/catalogo/
    Ny Times API: https://developer.nytimes.com/docs/most-popular-product/1/overview
    Pokémon API: https://pokeapi.co/
    Rick And Morty API: https://rickandmortyapi.com/documentation/#rest
    Fixer API (cotações de moedas): https://fixer.io/
    Coingecko Api (cotações de criptomoedas): https://www.coingecko.com/en/api
    API Futebol: https://www.api-futebol.com.br/

## Api e Database escolhidos:
    Banco de dados MongoDB
    APi(https://pokeapi.co/api/v2/pokemon?limit=151)
## Objetivo 
    é puxar da api pokeapi.co/api todos os 151 pokemons da regição de Kanto e inserir no banco de dados mongo.
    Collection: pokedex
    Funcionamento:
    Apagar collection pokedex
    Capturar com a api os dados dos pokemons
    Inserir na collection pokedex
    Mostrar os pokemons pela collection

#### Comandos
    docker build -t meu_python_app . - Construindo/atualizando o container
    docker run pasta_projeto - Executando o containe
    docker-compose up -d - Subindo os containers do docker-compose
    docker exec -it mongodb bash - acessar o terminal do banco de dados mongodb
    mongosh -u admin -p admin - acessando o banco de dados mongodb com o usuario admin
    use mydb - criando um banco de dados(pokemon_db)
    db.createCollection('pokedex'); - criando uma collection
    Interface para o mongodb(mongo-express) - http://localhost:8081/
