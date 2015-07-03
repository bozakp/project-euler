class CubeStorage:
    def __init__(self):
        self.counts = dict()

    def gen(self):
        i = 0
        while True:
            j = 0
            leni = len(str(i**3))
            while len(str((i+j)**3)) == leni:
                self.add_cube_to_counts((i+j)**3)
                j += 1
            for k in xrange(j):
                yield (i+k)**3
            i += j

    def add_cube_to_counts(self, cube):
        sc = str(cube)
        srted = "".join(c for c in sorted(sc))
        if srted not in self.counts:
            self.counts[srted] = 0
        self.counts[srted] += 1

def run():
    cube_storage = CubeStorage()
    for cube in cube_storage.gen():
        scube = str(cube)
        srted = "".join(c for c in sorted(scube))
        if cube_storage.counts[srted] == 5:
            return cube

from runner import main
main(run)
