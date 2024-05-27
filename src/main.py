from kybra import StableBTreeMap, update, query, void, Opt
from structures import CardId, Deputy, Voting

print("Uruchamianie aplikacji...")

deputies = StableBTreeMap[CardId, Deputy](
    memory_id=0, max_key_size=9, max_value_size=1000
)
votings = StableBTreeMap[CardId, Voting](
    memory_id=1, max_key_size=9, max_value_size=1000
)

print("Mapy zostały zainicjalizowane.")

@update
def add_deputy(deputy: Deputy) -> void:
    deputies.insert(deputy["card_id"], deputy)
    print(f"Dodano deputowanego: {deputy['card_id']}")

@query
def get_deputy(card_id: CardId) -> Opt[Deputy]:
    result = deputies.get(card_id)
    print(f"Szukanie deputowanego o ID: {card_id}, znaleziono: {result}")
    return result

print("Aplikacja jest gotowa do przyjęcia zapytań.")
