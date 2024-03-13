import db

from helper.writeAJson import writeAJson
from main import db

#pokemon por nome
def getPokemonByName(name: str):
    return db.collection.find({"name": name})

squirtle = getPokemonByName("Squirtle")
writeAJson(squirtle, "Squirtle")

#pokemon por grama ou veneno que tem evolução
tipos = ["Grass", "Poison"]
type = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True}})
writeAJson(type,"pokemonsGramaOuVenenoQueTemEvolucao")

#pokemons que tem apenas uma fraqueza
weakness = db.collection.find({"weaknesses": {"$size": 1})
writeAJson(weakness,"pokemonsDeApenasUmaFraqueza")

#pokemons que tem chance de spawn entre 0.3 e 0.6
chance = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
writeAJson(chance, "pokemonsChanceDeSpawn")

#pokemons que sao de fogo ou fracos contra fogo
fire = db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Fire"}]})
writeAJson(fire, "pokemonsDeFogo")