import primefactor
import pytest
def testsone():
    with pytest.raises(ValueError):
        assert primefactor.generate_prime_factors("hi")

def teststwo():
    assert primefactor.generate_prime_factors(1) == []

def teststhree():
    assert primefactor.generate_prime_factors(2) == [2]
