import time

def main(run):
    start = time.time()
    print("Answer: %s" % str(run()))
    elapse = time.time() - start
    print("Time(ms): %.2f" % (elapse*1000))
