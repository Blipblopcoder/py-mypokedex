### This is my Project: The Pokédex. The idea is to search for a Pokémon
# and to get the stats through the Pokémon API
# we will get name, type, stats, and first movements.

# First of all we will import the API and the way to normalize the 
# names so it doesn't matter if the user uses capital cases. 

import requests
import unicodedata

# Then, we will normalize the names of the Pokémon to a formate compatible 
# with the API

def normalize_name(name):
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
    name = name.lower().replace(' ', '-')
    return name

# Then, we will consult the Pokémon's API to get the data of an specific Pokémon

url = f'https://pokeapi.co/api/v2/pokemon/{name}'
response = requests.get(url)
if response.status_code == 200:
    return response.json()
else:
    print("❌ Pokémon not found or invalid name.")
    return None

### With the following we will show a summary with the pokemon's name, type, stats, and movements.

def show_pokemon_summary(data):
    print(f"\n📄 Pokémon Sheet: {data['name'].title()}")
    
    print("\n✨ Types:")
    for tipo in data['types']:
        print(f" - {tipo['type']['name'].title()}")

    print("\n📊 Stats:")
    for stat in data['stats']:
        print(f" - {stat['stat']['name'].title()}: {stat['base_stat']}")

    print("\n🎯 Movements (first 5):")
    for move in data['moves'][:5]:
        print(f" - {move['move']['name'].title()}")

def main():
    print("📘 Welcome to the interactive Pokédex!")
    while true: 
        name_user = input("\n🔍 Write the name of a Pokémon (or 'exit' to finish): ")
        if name_user.lower() == "exit":
            print("👋 See you later, trainer!")
            break

        name_api = normalize_name(name_user)
        data = get_pokemon_data(name_api)
        if data:
            show_pokemon_summary(data)
    

if __name__ == "__main__":
    main()