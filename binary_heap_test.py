#!/usr/bin/python
# -*- encoding=utf-8 -*-
# author: Ian
# e-mail: stmayue@gmail.com
# description: 


import binary_heap


def test():
    test_data = [(1, 0), (0.9, 1), (1.1, 2), (1.1, 3), (3.3, 4), (0, 5), (0.93, 6)]
    BH = binary_heap.BinaryHeap(7)

    # empty queue
    print('empty queue')
    print(BH)
    print('max priority')
    print(BH.get_max_priority())

    # insert
    print('\ntest insert')
    for p, i in test_data:
        BH.update(p, i)
    print(BH)
    print(BH.p2e)
    print(BH.e2p)

    # update
    print('\ntest update')
    BH.update(9.9, 0)
    print(BH)
    print(BH.p2e)
    print(BH.e2p)

    # get max priority
    print('\nmax priority')
    print(BH.get_max_priority())

    # re balance
    print('\ntest re_balance')
    BH.balance_tree()
    print(BH)
    print(BH.p2e)
    print(BH.e2p)

    # full insert
    print('\ntest full insert')
    BH.update(9.2, 7)
    print(BH)

    # pop
    print('\ntest pop')
    p, i = BH.pop()
    print('pop out: ', p, i)
    print(BH)
    print(BH.p2e)
    print(BH.e2p)

    # get priority
    print('\ntest get priority')
    print(BH.get_priority())

    # get e id
    print('\ntest e id')
    print(BH.get_e_id())

    # p id to e id
    print('\ntest p id to e id')
    print(BH.priority_to_experience([2, 3, 6]))


def main():
    test()


if __name__ == '__main__':
    main()
