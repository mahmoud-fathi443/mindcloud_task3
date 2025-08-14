class Candidate():
    def __init__(self, name):
        self.__name = name
        self.__numVotes = 0

    def get_name(self):
        return self.__name
    
    def get_num_votes(self):
        return self.__numVotes

    def add_vote(self):
        self.__numVotes+=1


class VoteSystem():
    def __init__(self):
        self.__candidates = []

    def add_candidate(self, candidate):
        if candidate not in self.__candidates:
            self.__candidates.append(candidate)
        else:
            print("Candidate already exists in the system!")

    def remove_candidate(self, candidate):
        if candidate  in self.__candidates:
            self.__candidates.remove(candidate)
        else:
            print("Candidate doesn't exist in the system!")

    def vote_to_candidate(self, candidate):
        candidate.add_vote()

    def display_the_winner(self):
        if self.__candidates:
            winner = max(self.__candidates, key=lambda cand: cand.get_num_votes()) # gets the candidate with the highest vote count
            print(winner.get_name())
        else:
            print("No Candidates added to the system!")

            

        


# Example
voteSystem = VoteSystem()
cand1 = Candidate("Mahmoud")
cand2 = Candidate("Ahmed")

voteSystem.add_candidate(cand1)
voteSystem.add_candidate(cand2)

voteSystem.vote_to_candidate(cand1)

voteSystem.display_the_winner()





    