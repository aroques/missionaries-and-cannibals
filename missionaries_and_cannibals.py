
from state import State
from node import Node
from missionaries_and_cannibals_problem import MissionariesAndCannibalsProblem
import sys

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

    print(result.solution)

def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result

def depth_limited_search(problem, limit=12):
    return recursive_dls(Node(problem.initial_state), problem, limit)

def recursive_dls(node, problem, limit):
    if problem.goal_is(node.state):
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
