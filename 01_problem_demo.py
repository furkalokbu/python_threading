from count_three_count import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')

    ints = read_ints('data/1Kints.txt')
    count_three_sum(ints)

    print('What are we waiting for?')
    print('ended main')