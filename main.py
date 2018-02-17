from missionaries_and_cannibals import iterative_deepening_search
from missionaries_and_cannibals import MissionariesAndCannibals


def main():

    problem = MissionariesAndCannibals()

    result = iterative_deepening_search(problem)

    if result:
        print_result(result)

def print_result(result):
    for i, node in enumerate(result.path):
        if node.depth % 2 == 0:
            sign = '+'
        else:
            sign = '-'
        print('{}{}'.format(sign, node.action))
        print('depth: {}'.format(node.depth))
        print(' {}'.format(node.state.wrong_side))


if __name__ == '__main__':
    main()
