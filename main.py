from search import iterative_deepening_search
from missionaries_and_cannibals import MissionariesAndCannibals


def main():

    problem = MissionariesAndCannibals()

    result = iterative_deepening_search(problem)

    print_result(result)

def print_result(result):
    if result:
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
