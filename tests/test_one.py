import primefactor
import pytest
def testsone():
    with pytest.raises(ValueError):
        assert primefactor.generate_prime_factors("hi")
