from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import sys
import datetime
import dateutil
import dateutil.parser
STANDARD_DELTA = timedelta(days=+10 * 365.25)

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def daysalive(today, dayofbirth):
    answer = today - dayofbirth
    return answer.days
         
def inthefuture(today, dayofbirth, delta):
    inthefuture = today + delta
    return daysalive(inthefuture, dayofbirth)
    
def makerange(today, dob, delta):
    return range(daysalive(today, dob), inthefuture(today, dob, delta))

def primedays(today, dayofbirth, delta):
    r = makerange(today, dayofbirth, delta)
    return filter(isprime, r)

def fromdayoflife2date(dayofbirth, dayoflife):
    return dayofbirth + timedelta(days=+dayoflife)

def main():
    dayofbirth_string = sys.argv[1]
    dayofbirth = dateutil.parser.parse(dayofbirth_string).date()
    l = list(primedays(date.today(), dayofbirth, STANDARD_DELTA))
    for special_day in l:
        special_date = fromdayoflife2date(dayofbirth, special_day)
        print special_date, special_day
    
if __name__ == "__main__":
    main()

        
