from project import test_rule
from project import is_cheater
from project import binomial_distribution
import pytest

def test_some_scenarios():
    assert test_rule(0.5, 0.75, 0.05, 0.8) == (23,15)
    assert test_rule(0.5, 0.75, 0.06, 0.85) == (25,16)
    assert test_rule(0.5, 0.75, 0.01, 0.9) == (50,33)

def test_ht_results():
    #11 heads and 14 tails
    results = ['T', 'T', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'H', 'H', 'H', 'H', 'T', 'H', 'T', 'T', 'T', 'T', 'T', 'H']
    assert is_cheater(results, "H", 25, 10) == "unfair player"
    assert is_cheater(results, "H", 25, 15) == "fair player"
    assert is_cheater(results, "H", 30, 15) == "test cannot be applied"

def test_numbers():
    assert binomial_distribution(4,0,0.5) == 0.0625
    assert binomial_distribution(100,20,0.4) == 1.053055286238778e-05
    assert binomial_distribution(5,5,0.8) == 0.3276800000000001

def test_others():
    with pytest.raises(TypeError):
        binomial_distribution(4.5,0,0.5)
        binomial_distribution(4,0.4,0.5)
        binomial_distribution(4.5,0,2)