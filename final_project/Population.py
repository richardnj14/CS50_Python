"""
Population class represents a whole population of players readed by a csv reader.
It sums up all population properties.

Atributes
-------------
players : int
number of tested players in the population

true_positive : int
number of true positive results

false_positve : int
number of false negative results

fair_players : int
number of true fair players in the population

unfair_players : int
number of true unfair players in the population

n : int
expected number of flips for each player

true_n : int
real number of players for each player

String
--------
___str___ return a string that sums tested population results up
"""
class Population:
    def __init__(self,players,n, true_n):
        self.players = len(list(filter(is_tested, players)))
        self.true_positive = len(list(filter(true_positive, players)))
        self.false_positive = len(list(filter(false_positive, players)))
        self.fair_players = len(list(filter(is_fair, players)))
        self.unfair_players = len(list(filter(is_unfair, players)))
        self.n = n
        self.true_n = true_n

    def __str__(self):
        if self.true_n != self.n:
            return f"Test could not be applied. Check on number of flips needed : Expected {self.n} flips, got {self.true_n} flips."
        else:
            return f"Test results for this population:\n{self.players} players checked\nTest could catch {self.true_positive} ({self.true_positive/self.unfair_players*100:.2f}%) unfair players from {self.unfair_players} ✅.\nTest have wrongly accused {self.false_positive} ({self.false_positive/self.fair_players*100:.2f}%) players ❌."



def true_positive(results):
    """
    Filter function to get all true positive results
    """
    return results["test_label"] == results["true_label"] and results["true_label"] == "unfair player"
def false_positive(results):
    """
    Filter function to get all false positive results
    """
    return results["test_label"] == "an unfair player" and results["true_label"] == "fair player"
def is_fair(results):
    """
    Filter function to get all true fair players
    """
    return results["true_label"] == "fair player"
def is_unfair(results):
    """
    Filter function to get all true unfair players
    """
    return results["true_label"] == "unfair player"
def is_tested(results):
    """
    Filter function to get all tested players
    """
    return results["test_label"] is not None