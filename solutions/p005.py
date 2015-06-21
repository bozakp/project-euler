def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

def run():
    nums = (x for x in xrange(1,21))
    return lcm(*nums)

from runner import main
main(run)
