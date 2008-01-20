from mpmath import *

def test_special():
    assert inf == inf
    assert inf != -inf
    assert -inf == -inf
    assert inf != nan
    assert nan != nan
    assert isnan(nan)
    assert --inf == inf
    assert abs(inf) == inf
    assert abs(-inf) == inf
    assert abs(nan) != abs(nan)

    assert isnan(inf - inf)
    assert isnan(inf + (-inf))
    assert isnan(-inf - (-inf))

    assert isnan(inf + nan)
    assert isnan(-inf + nan)

    assert mpf(2) + inf == inf
    assert 2 + inf == inf
    assert mpf(2) - inf == -inf
    assert 2 - inf == -inf

    assert inf > 3
    assert 3 < inf

    assert 3 > -inf
    assert -inf < 3

    assert isnan(inf * 0)
    assert isnan(-inf * 0)
    assert inf * 3 == inf
    assert inf * -3 == -inf
    assert -inf * 3 == -inf
    assert -inf * -3 == inf
    assert inf * inf == inf
    assert -inf * -inf == inf

    assert isnan(nan / 3)
    assert inf / -3 == -inf
    assert inf / 3 == inf
    assert 3 / inf == 0
    assert -3 / inf == 0
    assert 0 / inf == 0
    assert isnan(inf / inf)
    assert isnan(inf / -inf)
    assert isnan(inf / nan)

    assert mpf('inf') == mpf('+inf') == inf
    assert mpf('-inf') == -inf
    assert isnan(mpf('nan'))

def test_special_powers():
    assert inf**3 == inf
    assert isnan(inf**0)
    assert inf**-3 == 0
    assert (-inf)**2 == inf
    assert (-inf)**3 == -inf
    assert isnan((-inf)**0)
    assert (-inf)**-2 == 0
    assert (-inf)**-3 == 0
    assert isnan(nan**5)
    assert isnan(nan**0)

def test_functions_special():
    assert exp(inf) == inf
    assert exp(-inf) == 0
    assert isnan(exp(nan))
    assert log(inf) == inf
    assert isnan(sin(inf))
    assert isnan(sin(nan))
    assert atan(inf).ae(pi/2)
    assert atan(-inf).ae(-pi/2)

def test_convert_special():
    float_inf = 1e1000
    float_ninf = -1e1000
    float_nan = float_inf/float_ninf
    assert mpf(3) * float_inf == inf
    assert mpf(3) * float_ninf == -inf
    assert isnan(mpf(3) * float_nan)
