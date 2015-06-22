statics = {
        0: 0,
        1: len("one"),
        2: len("two"),
        3: len("three"),
        4: len("four"),
        5: len("five"),
        6: len("six"),
        7: len("seven"),
        8: len("eight"),
        9: len("nine"),
        10: len("ten"),
        11: len("eleven"),
        12: len("twelve"),
        13: len("thirteen"),
        14: len("fourteen"),
        15: len("fifteen"),
        16: len("sixteen"),
        17: len("seventeen"),
        18: len("eighteen"),
        19: len("nineteen"),
        }
tens = {
        2: len("twenty"),
        3: len("thirty"),
        4: len("forty"),
        5: len("fifty"),
        6: len("sixty"),
        7: len("seventy"),
        8: len("eighty"),
        9: len("ninety"),
        }

def n_letters(n):
    if n in statics:
        return statics[n]
    if n < 100:
        return tens[n // 10] + n_letters(n % 10)
    if n == 1000:
        return len("one") + len("thousand")
    ltr = n_letters(n % 100) + n_letters(n // 100) + len("hundred")
    if n % 100 == 0:
        return ltr
    else:
        return ltr + len("and")

def run():
    letters = 0
    for i in xrange(1, 1001):
        letters += n_letters(i)
    return letters

from runner import main
main(run)
