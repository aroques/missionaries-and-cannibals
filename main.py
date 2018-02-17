from state import State
from search import iterative_deepening_search
from missionaries_and_cannibals import MissionariesAndCannibals


def main():
    initial_state = State((3, 3, 1))
    goal_state = State((0, 0, 0))

    actions = [
        (1, 0, 1),
        (2, 0, 1),
        (0, 1, 1),
        (0, 2, 1),
        (1, 1, 1)
    ]

    problem = MissionariesAndCannibals(initial_state, goal_state, actions)

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
