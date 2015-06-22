with open('data/p022_names.txt', 'r') as f:
    qn = f.read().split(",")

names = [n[1:-1] for n in qn]

def run():
    names.sort()
    s = 0
    for i in xrange(len(names)):
        s += sum(ord(c) - 64 for c in names[i]) * (i + 1)
    return s

from runner import main
main(run)
