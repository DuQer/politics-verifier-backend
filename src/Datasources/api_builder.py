from parliament_documents import ParliamentDocuments
from voting_data import VotingData
from deputies_data import DeputiesData
from term_of_office_data import TermOfOfficeData
from parliamentary_club_data import ParliamentaryClubData
from parliamentary_committee_data import ParliamentaryCommitteeData
from parliament_broadcasts import ParliamentBroadcasts

class APIBuilder:
    def __init__(self):
        self.term = None
        self.nr = None
        self.fileName = None
        self.sitting = None
        self.voting_num = None
        self.leg = None
        self.date = None
        self.id = None
        self.code = None
        self.num = None
        self.sum = None

    def set_term(self, term):
        self.term = term
        return self

    def set_nr(self, nr):
        self.nr = nr
        return self

    def set_fileName(self, fileName):
        self.fileName = fileName
        return self

    def set_sitting(self, sitting):
        self.sitting = sitting
        return self

    def set_voting_num(self, voting_num):
        self.voting_num = voting_num
        return self

    def set_leg(self, leg):
        self.leg = leg
        return self

    def set_date(self, date):
        self.date = date
        return self
    
    def set_id(self, id):
        self.id = id
        return id
    
    def set_code(self, code):
        self.code = code
        return code
    
    def set_sum(self, sum):
        self.id = sum
        return sum
    
    def set_num(self, num):
        self.num = num
        return num

    def build_parliament_documents(self):
        return ParliamentDocuments(self.term, self.nr, self.fileName)

    def build_voting_data(self):
        return VotingData(self.term, self.sitting, self.voting_num, self.leg, self.date)
    
    def build_deputy_data(self):
        return DeputiesData(self.term, self.leg, self.sitting, self.date)
    
    def build_term_of_office(self):
        return TermOfOfficeData(self.term)
    
    def build_parliamentary_club_data(self):
        return ParliamentaryClubData(self.term, self.id)
    
    def build_parliamentary_committee_data(self):
        return ParliamentaryCommitteeData(self.term, self.code, self.sum, self.num)
    
    def build_parliament_broadcasts(self):
        return ParliamentBroadcasts(self.term)


# Example 1
# builder = APIBuilder()
# voting_data = builder.set_term('term10').set_sitting(1).set_leg(1).build_voting_data()
# print(voting_data.votings_list())

# Example 2
# builder = APIBuilder()
# deputies_data = builder.set_term("term10").set_leg("1").set_sitting(1).set_date("2024-05-14").build_deputy_data()
# print(deputies_data.get_all_deputies())
