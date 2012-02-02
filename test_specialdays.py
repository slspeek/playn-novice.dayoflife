from specialdays import daysalive, inthefuture, makerange, primedays
from datetime import date, timedelta


def test_daysalive():
    dob = date(1971,1,21)
    today = date(1972,1,21)
    assert daysalive(today, dob) == 365
    

def test_inthefuture():
    dob = date(1971,1,21)
    today = date(1971,1,31)
    assert inthefuture(today,dob, timedelta(days=+5)) == 15
    

def test_range():
    dob = date(1993,3,11)
    today = date(2013,3,11)
    r = makerange(today, dob, timedelta(days=+3652))
    l = list(r)
    assert len(l) == 3652
    
def test_primedays():
    dob = date(2000,1,1)
    today = date(2000,1,11)
    r = primedays(today, dob, timedelta(days=+10))
    l = list(r)
    assert l == [11,13,17,19]

