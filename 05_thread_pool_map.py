import concurrent.futures
from count_three_count import read_ints, count_three_sum


if __name__ == '__main__':
    print('started main')

    data = read_ints('data/1Kints.txt')
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(count_three_sum, (data, data), ('t1', 't2'))
        print('After map')
        for r in results:
            print(f'{r=}')
        print('end of map')

    print('ended map')