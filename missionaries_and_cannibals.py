from state import State
from node import Node
from missionaries_and_cannibals_problem import MissionariesAndCannibalsProblem


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

    problem = MissionariesAndCannibalsProblem(initial_state, goal_state, actions)

    result = iterative_deepening_search(problem)

    if result:
        for i, node in enumerate(result.path):
            if node.depth % 2 == 0:
                sign = '+'
            else:
                sign = '-'
            print('{}{}'.format(sign, node.action))
            print('depth: {}'.format(node.depth))
            print(' {}'.format(node.state.wrong_side))


def iterative_deepening_search(problem):
    limit = 13
    for depth in range(limit):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


def depth_limited_search(problem, limit):
    return recursive_dls(Node(problem.initial_state), problem, limit)


def recursive_dls(node, problem, limit):
    if problem.goal_is(node.state):
        print('solution found at depth {}!'.format(node.depth))
        return node
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        for child in node.expand(problem):
            result = recursive_dls(child, problem, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                return result
        return 'cutoff' if cutoff_occurred else None


if __name__ == '__main__':
    main()
