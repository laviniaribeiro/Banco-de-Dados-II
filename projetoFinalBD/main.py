from database import Database
from CRUD import GameCRUD
from cli import SimpleCLI
from cli import GameCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.198.186.125:7687", "neo4j", "jigs-prism-gaskets")
db.drop_all()

game_db = GameCRUD(db)

game_db.create_game("Counter-Strike","Shooter",2000)
game_db.create_game("Grand Theft Auto V","Ação",2013)
game_db.create_game("Firewatch","Aventura",2016)

game_db.create_jurado("Lavinia")
game_db.create_jurado("Ana")
game_db.create_jurado("Joao")


game_db.create_avaliacao("Counter-Strike","Lavinia",10,200)
game_db.create_avaliacao("Firewatch","Ana",8,150)
game_db.create_avaliacao("Grand Theft Auto V", "Joao", 10, 400)


gameCLI = GameCLI(game_db)
gameCLI.run()

db.close()