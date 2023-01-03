import threading
from decorations import measure_time
from count_three_count import read_ints, count_three_sum


@measure_time
def run_in_parallel(ints):
    t1 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't1'))
    t2 = threading.Thread(target=count_three_sum, daemon=True, args=(ints, 't2'))

    t1.start()
    t2.start()

    print('Going to wait for threads...')

    t1.join()
    t2.join()


@measure_time
def run_in_sequentialy(ints):
    count_three_sum(ints, 'main')
    count_three_sum(ints, 'main')


if __name__ == '__main__':

    print('started main')
    ints = read_ints('data/1Kints.txt')

    run_in_parallel(ints)
    run_in_sequentialy(ints)

    print('ended main')