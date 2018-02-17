#
# Adapted from https://github.com/aimacode/aima-python/blob/master/search.py
#

from node import Node

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
