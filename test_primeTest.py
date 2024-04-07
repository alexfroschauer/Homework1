from primeTest import isInt
from primeTest import isNatural
from primeTest import isPrime

def test_isInt():
    assert isInt(1) == True
    assert isInt(-1) == True
    assert isInt(0.5) == False

def test_isNatural():
    assert isNatural(1) == True
    assert isNatural(10) == True
    assert isNatural(0.5) == False
    assert isNatural(-1) == False

def test_isPrime():
    assert isPrime(-3) == False
    assert isPrime(1.3) == False
    assert isPrime(4) == False
    assert isPrime(10) == False
    assert isPrime(3) == True
    assert isPrime(11) == True
