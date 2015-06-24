from common import lcm

def run():
    nums = (x for x in xrange(1,21))
    return lcm(*nums)

from runner import main
main(run)
