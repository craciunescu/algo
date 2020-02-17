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

# There are many ways in which one could do this. We could reuse the isPrime(n)
# function that we wrote in E5, but that would yield an extremely inefficient
# program: we would have to check all the numbers up to i each time we check for
# a prime.

# I propose two different implementations:
# - Sieve of Erastothenes
#   This is a very ingenious old algorithm that simply and effectively yields
#   all prime numbers up to a given number N. It has its drawbacks, since it has
#   to store all numbers up to n in memory, which can become very memory
#   consuming with large primes.
# - Modify isPerfect(n) so that it returns the amount of primes between 1 and n
#   instead of a boolean confirming the given number is prime.
# - 

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
