from operator import sub, add

def main():

    stack = []

    # missionaries, cannibals, and boat
    state = State((3, 3, 1))

    # subtract then add then subtract then add actions to state transition (get to new depth)
    actions = [
        (1, 0, 1),
        (2, 0, 1),
        (0, 1, 1),
        (0, 2, 1),
        (1, 1, 1)
    ]

    for i, action in enumerate(actions):
        if i % 2 == 0:
            new_state = state.perform_action(sub, action)
        else:
            new_state = state.perform_action(add, action)

        stack.append(new_state)

    print(stack.pop())
    print()

    for s in stack:
        print(s)


class States:
    pass


class State:
    def __init__(self, wrong_side):
        self.wrong_side = wrong_side

    def __str__(self):
        return 'R: ' + str(self.wrong_side) + '   W: ' + str(self.right_side)

    @property
    def right_side(self):
        total = (3, 3, 1)
        return tuple(map(sub, total, self.wrong_side))

    def num_missionaries(self, side):
        if side == 'w':
            return self.wrong_side[0]
        elif side == 'r':
            return self.right_side[0]

    def num_cannibals(self, side):
        if side == 'w':
            return self.wrong_side[1]
        elif side == 'r':
            return self.right_side[1]

    def num_boat(self, side):
        if side == 'w':
            return self.wrong_side[2]
        elif side == 'r':
            return self.right_side[2]

    def perform_action(self, arithmetic_operator, action):
        state_tuple = tuple(map(arithmetic_operator, self.wrong_side, action))
        new_state = State(state_tuple)
        if self.is_valid(new_state):
            return new_state
        else:
            raise TransitionError(self.wrong_side, state_tuple, 'invalid state transition!')

    @staticmethod
    def is_valid(state):
        missionaries_valid = 0 >= state.num_missionaries('w') >= 3 and 0 >= state.num_missionaries('r') >= 3
        cannibals_valid = 0 >= state.num_cannibals('w') >= 3 and 0 >= state.num_cannibals('r') >= 3
        boat_valid = 0 >= state.num_boat('w') >= 1 and 0 >= state.num_boat('r') >= 1
        if missionaries_valid and cannibals_valid and boat_valid:
            return True
        else:
            return False


class TransitionError(Exception):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


if __name__ == '__main__':
    main()
