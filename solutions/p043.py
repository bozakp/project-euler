from itertools import permutations

def run():
    all_digits = set(xrange(10))
    s = 0
    for perm in permutations(all_digits):
        n_str = "".join(str(x) for x in perm)
        if (int(n_str[1:4]) % 2 == 0 and
            int(n_str[2:5]) % 3 == 0 and
            int(n_str[3:6]) % 5 == 0 and
            int(n_str[4:7]) % 7 == 0 and
            int(n_str[5:8]) % 11 == 0 and
            int(n_str[6:9]) % 13 == 0 and
            int(n_str[7:10]) % 17 == 0):
            s += int(n_str)
    return s

from runner import main
main(run)
