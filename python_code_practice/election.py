class Candidate:
    def __init__(self, name, area_code, votes):
        self.name = name
        self.area_code = area_code
        self.votes = votes
    
    def __str__(self):
        return f"{self.name}: {self.votes}"


class ElectionResult:
    def __init__(self):
        self.candidates = []
        self.area_votes = {}

    def __str__(self):
        print("Candidates:")
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes}: {candidate.area_code}")
        print("Area Votes:")
        for area_code, votes in self.area_votes.items():
            print(f"{area_code}: {votes}")
        return ""

    def add_candidate(self, candidate):
        self.candidates.append(candidate)
        if candidate.area_code not in self.area_votes:
            self.area_votes[candidate.area_code] = 0
        self.area_votes[candidate.area_code] += candidate.votes

    def get_winner_by_area(self, area_code):
        area_candidates = [c for c in self.candidates if c.area_code == area_code]
        if not area_candidates:
            return None  # No candidates for the given area code
        winner = max(area_candidates, key=lambda x: x.votes)
        return winner.name

    def get_overall_winner(self):
        winner = max(self.candidates, key=lambda x: x.votes)
        return winner.name

    def get_winner_percentage_by_area(self, area_code):
        if area_code not in self.area_votes:
            return None  # No votes for the given area code
        total_votes_area = self.area_votes[area_code]
        area_candidates = [c for c in self.candidates if c.area_code == area_code]
        if not area_candidates:
            return None  # No candidates for the given area code
        winner = max(area_candidates, key=lambda x: x.votes)
        winner_percentage = (winner.votes / total_votes_area) * 100
        return winner.name, winner_percentage

    def get_overall_winner_percentage(self):
        total_votes = sum(self.area_votes.values())
        winner = max(self.candidates, key=lambda x: x.votes)
        overall_winner_percentage = (winner.votes / total_votes) * 100
        return winner.name, overall_winner_percentage


# Example usage:

# Creating candidates
candidate1 = Candidate("Candidate A", "Area1", 500)
candidate2 = Candidate("Candidate B", "Area1", 700)
candidate3 = Candidate("Candidate C", "Area2", 800)

# Creating ElectionResult instance
election_result = ElectionResult()

# Adding candidates to the election result
election_result.add_candidate(candidate1)
election_result.add_candidate(candidate2)
election_result.add_candidate(candidate3)

# Query 1: Given the area code, find the winner
area_winner = election_result.get_winner_by_area("Area1")
print(f"Winner in Area1: {area_winner}")

# Query 2: Find the winner vote percentage-wise among all the area codes
overall_winner, overall_percentage = election_result.get_overall_winner_percentage()
print(f"Overall Winner: {overall_winner}, Percentage: {overall_percentage}%")

print("Election Result: ",  election_result)
print("Candidate 1: ", candidate1)
print("Candidate 2: ", candidate2)
print("Candidate 3: ", candidate3)