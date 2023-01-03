import time
import threading
from count_three_count import read_ints, count_three_sum


if __name__ == '__main__':
    print('started main')

    ints = read_ints('data/1Kints.txt')
    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
    t1.start()

    time.sleep(3)
    print("timer end")

    t1.join()
    print('ended main')