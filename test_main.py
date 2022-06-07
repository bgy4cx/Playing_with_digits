from main import dig_pow

def test_dig_pow_1():
    assert dig_pow(89, 1) == 1

def test_dig_pow_2():
    assert dig_pow(92, 1) == -1

def test_dig_pow_3():
    assert dig_pow(46288, 3) == 51

