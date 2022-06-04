import primefactor
import pytest
def testsone():
    with pytest.raises(ValueError):
        assert primefactor.generate_prime_factors("hi")

def teststwo():
    assert primefactor.generate_prime_factors(1) == []

def teststhree():
    assert primefactor.generate_prime_factors(2) == [2]

def testsfour():
    assert primefactor.generate_prime_factors(3) == [3]

def testsfive():
    assert primefactor.generate_prime_factors(4) == [2,2]
