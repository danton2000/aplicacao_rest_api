# Utilizando as libs que foram instaladas com o arquivo Dockerfile
import requests
import pymongo

# Conectar ao MongoDB
mongo_client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
mongo_db = mongo_client["pokemon_db"]
mongo_collection = mongo_db["pokedex"]

# Definir a URL da API e parâmetros
url = "https://pokeapi.co/api/v2/pokemon?limit=151"

# Fazendo a requisição GET para capturar os dados da url(lista de pokemons)
response = requests.get(url)

# Realizando uma conversão dos dados para o tipo json(dict)
items_json = response.json()

# Limpar os dados da collection pokedex
#mongo_collection.deleteMany()

for item in items_json["results"]:
    #Inserindo na collection os dados obtidos pela api
    # print(str(item["name"]))
    mongo_collection.insert_one({"name": str(item["name"])})
    
# Listando os pokemons
def lista_pokemons():
    try:
        print("Listando os pokemons.")
        pokemons = mongo_collection.find()
        for pokemon in pokemons:
            print(pokemon["name"])
    except Exception as e:
        print(f"Erro ao transferir dados: {e}")
 
#Executando a função       
lista_pokemons()