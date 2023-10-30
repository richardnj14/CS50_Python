"""
Needed packages and libraries
"""
import consolemenu
import math
import configparser
from consolemenu import SelectionMenu
import csv
import ast
import random

"""
Import classes
"""
from Player import Player
from Population import Population

"""
Constant
"""
PFAIRCOIN = 0.5

"""
Parameters functions
"""
def create_parameters():
        """
        This functions creates a configuration file to save all needed parameters. Is called in get_parameters when a 'parameters.ini' file is not found.
        """
        config = configparser.ConfigParser()
        config["parameters"] = {"p_fair": PFAIRCOIN,
                                "p_unfair": 0.75,
                                "false_positive_rate": 0.05,
                                "true_positive_rate": 0.8,
                                "face": "H"}
        with open("parameters.ini", "w") as configfile:
            config.write(configfile)

def update_parameters():
    """
    This function allows to update a parameter from configuration file.
    Is called by user in main menu.
    """
    config = configparser.ConfigParser()
    config.read("parameters.ini")
    while True:
        p_unfair = float(config['parameters']['p_unfair'])
        false_positive_rate = float(config['parameters']['false_positive_rate'])
        true_positive_rate = float(config['parameters']['true_positive_rate'])
        face = config['parameters']['face']
        options = [f"Face probability of an unfair coin (%). (Current: {p_unfair*100:.2f}%)", f"How many fair players (%) do we accept to wrongly accuse? (Current: {false_positive_rate*100:.2f}%)", f"How many unfair players (%) do we want to catch? (Current: {true_positive_rate*100:.2f}%)", f"Unfair face ('H' or 'T') (Current: {face})"]
        selection = SelectionMenu.get_selection(options)
        match selection:
            case 0:
                config["parameters"]["p_unfair"] = str(float(input(f"Face probability of an unfair coin (%). (Current: {p_unfair*100:.2f}%)\n"))/100)
                with open("parameters.ini", "w") as configfile:
                    config.write(configfile)
            case 1:
                config["parameters"]["false_positive_rate"] = str(float(input(f"How many fair players (%) do we accept to wrongly accuse? (Current: {false_positive_rate*100:.2f}%)\n"))/100)
                with open("parameters.ini", "w") as configfile:
                    config.write(configfile)
            case 2:
                config["parameters"]["true_positive_rate"] = str(float(input(f"How many unfair players (%) do we want to catch? (Current: {true_positive_rate*100:.2f}%)\n"))/100)
                with open("parameters.ini", "w") as configfile:
                    config.write(configfile)
            case 3:
                config["parameters"]["face"] = input(options[3])
                with open("parameters.ini", "w") as configfile:
                    config.write(configfile)
            case 4:
                break

def get_parameter(param):
    """
    This function get a parameter from 'parameters.ini' file
    :param param: parameter to get
    :type param: str
    :return: a parameter readed from 'parameters.ini'
    :rtype: str
    """
    try:
        open("parameters.ini", "r")
    except FileNotFoundError:
        create_parameters()
    config = configparser.ConfigParser()
    config.read("parameters.ini")
    return config['parameters'][param]

"""
Test functions
"""

def binomial_distribution(n, h, p):
    """
    Calculates probability of h successes in n individual experiments using the binomial distribution

    :param n: number of individual experiments
    :type n: int
    :param h: number of successes
    :type h: int
    :param p: success probability for a single observation
    :type p: float
    :return: probability of h successes in n individual experiments
    :rtype: float
    """
    return math.factorial(n)/(math.factorial(h)*math.factorial(n-h))*pow(p,h)*pow(1-p,n-h)

def test_rule(p_fair, p_unfair, fp_rate, tp_rate):
    """
    Calculates the minimun experiments number and the minimun success observation needed to accuse a player of cheating.
    For a fixed n, the higher h is, the less fair players are wrongly accused and the less unfair players are catched.
    An couple of n and h need to be found to satisfy user criteria.

    :param p_fair: probability of success (head or tail) with a fair coin
    :type p_fair: float
    :param p_unfair: probability of success (head or tail) with an unfair coin
    :type p_unfair: float
    :param fp_rate: false positive rate, how many fair players we accept to wrongly accuse ?
    :type fp_rate: float
    :param tp_rate: true positive rate, how many unfair player do we want to catch ?
    :type tp_rate: float
    :return: minimun experiments number and the minimun success observation needed to accuse a player of cheating
    :rtype: tupple
    """
    n = 1
    while True:
        h = 0
        fair_coin = 0
        unfair_coin = 0
        while h <= n:
            fair_coin += binomial_distribution(n, h, p_fair)
            unfair_coin += binomial_distribution(n, h, p_unfair)
            if 1-fair_coin < fp_rate and 1-unfair_coin > tp_rate:
                return n, h
            else:
                h += 1
        n += 1

def is_cheater(results, face, n, h):
    """
    Hypothesis testing: use test parameters results to determine if a player is actually a unfair player or not.

    :param results: a list with each plays result
    :type results: list
    :param n: number of individual experiments needed to satisfy user criteria
    :type n: int
    :param h: number of successes needed to accuse a player
    :type h: int
    :param face: face supposed to land often
    :type face: str
    :return: Test result
    :rtype: str
    """
    if len(results) == n:
        if results.count(face) > h:
            return "an unfair player"
        else:
            return "a fair player"
    else:
        return "test cannot be applied"

"""
In live function
"""

def get_results(n):
    """
    Ask for flip result and only accepts 'h' or 't' case insensitive

    :param n: minimun observations needed
    :type n: int
    :return: a list with all flips results when user enter all needed observations
    :rtype: list
    """
    print("Use enter to save a new flip result. Entry must be 'H' for 'head' or 'T' for 'tail'")
    print(f"Note: {n} observations needed")
    i=1
    results = list()
    while len(results) < n:
        try:
            result = input(f"Flip {i}: ")
            if result.upper() in ["H", "T"]:
                results.append(result.upper())
                i += 1
            else:
                raise ValueError
        except ValueError:
            print("Make sure to enter H for'head' or T for'tail'")
    return results

"""
csv mode
"""

def csv_mode(file, face, n, h):
    """
    This function read a generated scenario with players results and write a new csv file with players results on hypothesis test.
    At the end print population class that sums all population properties up.
    :param file: csv file name with players results
    :type file: str
    :param face: face supposed to land often
    :type face: str
    :param n: number of individual experiments
    :type n: int
    :param h: number of successes
    :type h: int
    """
    with open(f"{file}", newline='') as csvread:
        reader = csv.DictReader(csvread, delimiter=";")
        rows = list(reader)
    with open(f"check_{file}", "w", newline='') as csvwrite:
        writer = csv.DictWriter(csvwrite, fieldnames=["player","results","true_label","test_label"], delimiter=";")
        writer.writeheader()
        for i, row in enumerate(rows):
            player = Player(row["results"],row["true_label"])
            player.test_label = is_cheater(player.results, face, n, h)
            writer.writerow({"player":f"player{i+1:02}","results":player.results,"true_label":player.true_label,"test_label":player.test_label})
    with open(f"check_{file}", newline='') as csvread:
        reader = csv.DictReader(csvread, delimiter=";")
        rows = list(reader)
        result = len(ast.literal_eval(rows[0]["results"]))
        population = Population(rows, n, result)
    print(population)

"""
Scenarios generator
"""

def results_gen(p, face, n):
    """
    This function creates scenarios for a player (flips results) with a given probability weight for each face.
    :param p: probability of getting "face" in a flip
    :type p: float
    :param face: supposed unfair face
    :type face: str
    :param n: number of flips to simulate
    :type n: int
    :return: a list with player results, 'H' for head and 'T' for tail
    :rtype: list
    """
    return random.choices("HT", cum_weights=(p, 1), k=n) if face == "H" else random.choices("TH", cum_weights=(p, 1), k=n)

def csv_gen(f, u, p_unfair, face, n):
    """
    This function generates an csv with 'f' fair players and 'u' unfair players and their results.
    :param f: number of fair players to simulate
    :type f: int
    :param u: number of unfair players to simulate
    :type u: int
    :param p_unfair: probability en % of getting 'face' with this unfair coin (it is not correlated with test parameter 'p_unfair')
    :type p_unfair: float
    :param face: face supposed to land often
    :param n: number of flips for each player (it's not correlated with test parameter 'n')
    :type n: int
    """
    p_unfair = p_unfair/100
    probabilitys = [0.5 for _ in range(f)] + [p_unfair for _ in range(u)]
    probabilitys = random.sample(probabilitys, k=len(probabilitys))
    with open(f"scenario_{f}_{u}.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["player","results","true_label"], delimiter=";")
        writer.writeheader()
        for i, p in enumerate(probabilitys):
            if p == 0.5:
                player = Player(results_gen(p,face, n), "fair player")
            else:
                player = Player(results_gen(p, face, n), "unfair player")
            writer.writerow({"player":f"player{i+1:02}","results":player.results,"true_label":player.true_label})

"""
Main menu
"""

def main_menu():
    """
    Creates main menu with consolemenu library
    :return: user selection
    :rtype: int
    """
    options = ["In live mode", "CSV mode", "Scenarios generator", "Test parameters"]
    menu = consolemenu.SelectionMenu(options)
    return menu.get_selection(options)

"""
Main function
"""

def main():
    """
    Main function, initialize parameters and call program functions based on user selection.
    """
    while True:
        p_fair = float(get_parameter("p_fair"))
        p_unfair = float(get_parameter("p_unfair"))
        false_positive_rate = float(get_parameter("false_positive_rate"))
        true_positive_rate = float(get_parameter("true_positive_rate"))
        face = str(get_parameter("face"))
        n, h = test_rule(p_fair, p_unfair, false_positive_rate, true_positive_rate)
        match main_menu():
            case 0:
                player = Player(get_results(n))
                print(f"Test rule: If a player gets {h+1} times '{face}' in {n} flips, they are probably a cheater.")
                player.test_label = is_cheater(player.results, face, n, h)
                print(player)
                break
            case 1:
                csv_mode(input("Enter csv filename: "), face, n, h)
                break
            case 2:
                try:
                    sim_inputs = [int(input("How many fair players in the population?\n")),
                                int(input("How many unfair players in the population?\n")),
                                float(input("What's the unfair coin face probability? (%)\n")),
                                (input("What's the unfair face? ('H' or 'T')\n")),
                                int(input("How many times each player flip the coin?\n"))]
                    csv_gen(*sim_inputs)
                except ValueError:
                    print("Scenario could not be generated. Make sure to enter compatible inputs.")
                    break
            case 3:
                update_parameters()
            case 4:
                break

if __name__ == "__main__":
    main()