from kybra import Alias, Record, Variant, Opt
from kybra import nat8, nat16, nat32, text, null

CardId = Alias[nat16]
DistrictNum = Alias[nat8]


class EducationLevel(Variant, total=True):
    podstawowe: null
    zawodowe: null
    średnie_zawodowe: null
    średnie_ogólne: null
    wyższe: null


class Voivodeship(Variant, total=True):
    dolnośląskie: null
    kujawsko_pomorskie: null
    lubelskie: null
    lubuskie: null
    łódzkie: null
    małopolskie: null
    mazowieckie: null
    opolskie: null
    podkarpackie: null
    podlaskie: null
    pomorskie: null
    śląskie: null
    świętokrzyskie: null
    warmińsko_mazurskie: null
    wielkopolskie: null
    zachodniopomorskie: null


class Kind(Variant, total=True):
    on_list: null
    electronic: null


class Deputy(Record):
    card_id: CardId
    active: bool
    birth_date: text
    birth_location: text
    club: text
    district_name: text
    district_num: DistrictNum
    education_level: EducationLevel  #! Check this
    email: text
    first_name: text
    second_name: Opt[text]
    last_name: text
    number_of_votes: nat32
    profession: text
    voivodeship: Voivodeship  #! Check this


class Voting(Record):
    date: text
    description: text
    kind: Kind  #! Check this
    title: text
    topic: text
    vote: str  #! Check this
