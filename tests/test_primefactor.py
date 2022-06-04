"""These are the tests for prime factoring"""
import primefactor
import pytest
def testsone():
    """test ValueError"""
    with pytest.raises(ValueError):
        assert primefactor.generate_prime_factors("hi")

def teststwo():
    """test integer one's prime factors"""
    assert primefactor.generate_prime_factors(1) == []

def teststhree():
    """test integer two's prime factors"""
    assert primefactor.generate_prime_factors(2) == [2]

def testsfour():
    """test integer three's prime factors"""
    assert primefactor.generate_prime_factors(3) == [3]

def testsfive():
    """test integer four's prime factors"""
    assert primefactor.generate_prime_factors(4) == [2,2]

def testssix():
    """test integer six's prime factors"""
    assert primefactor.generate_prime_factors(6) == [2,3]

def testsseven():
    """test integer eight's prime factors"""
    assert primefactor.generate_prime_factors(8) == [2,2,2]

def testseight():
    """test integer nine's prime factors"""
    assert primefactor.generate_prime_factors(9) == [3,3]
