import math

################################################################################
# 7. Write a program which asks the user for a positive number (N) and obtain
# and obtains how many prime numbers there are between 1 and that number N,
# and how many perfects between 1 and N. Analyze the efficiency and complexity.
################################################################################

# For this, we could reuse the isPrime(n) from E5, but that would yield a highly
# unefficient program. Instead, we will implement the Sieve of Erastothenes.

#def getPrimes(n):
#   """ Returns all prime numbers up to n. """
#   
#    primes = []
#    for number in range(2,n):
#        if number not in primes:
#            for prime in primes:
#                if number % prime == 0

def isPerfect(n):
    """Return if a number is perfect."""
    start = time()
    divs = 0

    for i in range (1, int(math.sqrt(n)+1)):
        # Is divisor of the number.
        if (n % i == 0):
            divs += i

            # The quotient is also a divisor of n.
            if (n / i != i):
                divs += (n // i)
    
    # We're counting n twice in the sum.
    result = (n*2 == divs)
    end = time()

    print("isPerfect(",n,") \t\t|| RESULT",result,"|| TIME", (end-start), "sec.")

def primes(n):
    """Returns the amount of prime numbers between 1 and n."""
    return len(list(filter(isPrime, range(1,n))))

def perfects(n):
    """Returns the amount of perfect numbers between 1 and n."""
    return len(list(filter(isPerfect, range(1,n))))

print(primes(1000))
print(perfects(1000))