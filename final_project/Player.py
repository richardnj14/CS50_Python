"""
Needed packages and libraries
"""
import ast

"""
Player class represents a player with their results and labels (fair or unfair player)

Atributes
---------------
results : list
player results 'H' or 'T' in a list
@property : returns results list
setter : set results as a list, even if results is a string read by a csv reader, uses ast.literal_eval() to convert string in to a list

flips : int
number of elements in results
heads : int
number of heads 'H' in results
tails : int
number of heads 'T' in results
test_label : str
test result (fair or unfair player), initialized as 'Unknown'
true_label : str
true label in the case of generated players from scenarios generator, initialized as NA
"""


class Player:
    def __init__(self, results, true_label="NA", test_label = "Unknow"):
        self.results = results
        self.flips = len(self.results)
        self.heads = results.count("H")
        self.tails = results.count("T")
        self.test_label = test_label
        self.true_label = true_label

    def __str__(self):
        return f"This player got {self.heads} 'heads' and {self.tails} 'tails' in {self.flips} flips.\nI suppose this is {self.test_label} {emoji(self.test_label)}"

    @property
    def results(self):
        return self._results

    """
    Results setter guarantees that results for a player are always stored in a list with strings 'H' or 'T'
    When a list is passed as a string by csv readers, it converts the string in a list with ast library
    """
    @results.setter
    def results(self, results):
        if type(results) == str:
            self._results = ast.literal_eval(results)
        elif type(results) == list:
            self._results = results
        else:
            raise TypeError("Player results expected as list")

def emoji(test_label):
    if test_label == "fair player":
        return "✅"
    else:
        return "❌"