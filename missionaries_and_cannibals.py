from operator import sub, add
from state import State


def main():
    goal_state = (0, 0, 0)

    frontier = []

    # missionaries, cannibals, and boat
    state = State((3, 3, 1))

    print(state)

    frontier.append(state)

    i = 0
    while state.wrong_side != goal_state:
        state = frontier.pop()
        frontier = increase_depth_of_search_tree(i, state, frontier)
        i += 1

    print(state)


def increase_depth_of_search_tree(i, state, frontier):
    # subtract then add then subtract then add actions to state transition (get to new depth)
    actions = [
        (1, 0, 1),
        (2, 0, 1),
        (0, 1, 1),
        (0, 2, 1),
        (1, 1, 1)
    ]

    for action in actions:
        if i % 2 == 0:
            new_state = perform_action(sub, action, state.wrong_side)
        else:
            new_state = perform_action(add, action, state.wrong_side)

        if new_state.is_valid:
            frontier.append(new_state)

    return frontier


def perform_action(arithmetic_operator, action, state):
    new_state_tuple = tuple(map(arithmetic_operator, state, action))
    new_state = State(new_state_tuple)
    return new_state


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


if __name__ == '__main__':
    main()
