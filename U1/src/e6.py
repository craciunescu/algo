from time import time
import math

################################################################################
# 6. Program a function to determine if a number received as parameter is
# perfect. Analyze the efficiency and complexity.
################################################################################

# A perfect number is a positive integer such that it is equal to the sum of its
# divisors. As with all problems, there are many ways to implement this.

# a) Naive way.
# - Calculate all divisors up to N.
# - Check if sum is equal to number.
def isPerfectNaive(num):
    """Return if a number is perfect."""
    
    start = time()
    result = (num == sum([n for n in range (1, num+1) if num % n == 0]))
    end = time()

    print("isPerfectNaive(",num,") \t|| RESULT",result,"|| TIME", (end-start), "sec.")

################################################################################

# b) Not-so-naive way.
# - Divisors present themselves in pairs when calculating.
# - Calculate up to square root of number.
# - Can iteratively calculate sum instead of occupying memory with list of 
#   divisors.

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

#isPerfect(6)

# Testing

# Correct cases.
#isPerfectNaive(33550336)
#isPerfect(33550336)

#print()

# Incorrect cases.
#isPerfectNaive(33550333)
#isPerfect(33560336)
def isPerfectTest(n):
    for number in n:
        isPerfect(number)
isPerfectTest(range(1, 1000))