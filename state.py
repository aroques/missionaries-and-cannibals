from operator import sub, add

MISSIONARY_IDX = 0
CANNIBAL_IDX = 1
BOAT_IDX = 2


class State:
    def __init__(self, wrong_side):
        self.wrong_side = wrong_side

    def __repr__(self):
        return 'W: ' + str(self.wrong_side) + '   R: ' + str(self.right_side)

    def __str__(self):
        return 'W: ' + str(self.wrong_side) + '   R: ' + str(self.right_side)

    def __eq__(self, other):
        return self.wrong_side == other.wrong_side

    def __add__(self, other):
        if not isinstance(other, tuple):
            raise TypeError('Cannot add state and {}'.format(type(other)))
        new_state_tuple = tuple(map(add, self.wrong_side, other))
        return State(new_state_tuple)

    def __sub__(self, other):
        if not isinstance(other, tuple):
            raise TypeError('Cannot subtract {} from state'.format(type(other)))
        new_state_tuple = tuple(map(sub, self.wrong_side, other))
        return State(new_state_tuple)

    @property
    def right_side(self):
        total = (3, 3, 1)
        return tuple(map(sub, total, self.wrong_side))

    @property
    def num_missionaries(self):
        return self.wrong_side[MISSIONARY_IDX]

    @property
    def num_cannibals(self):
        return self.wrong_side[CANNIBAL_IDX]

    @property
    def num_boat(self):
        return self.wrong_side[BOAT_IDX]

    @property
    def missionaries_are_safe(self):
        rs = State(self.right_side)

        return (self.num_missionaries == 0 or self.num_missionaries >= self.num_cannibals) and \
               (rs.num_missionaries == 0 or rs.num_missionaries >= rs.num_cannibals)

    @property
    def is_valid(self):
        rs = State(self.right_side)

        num_missionaries_valid = (0 <= self.num_missionaries <= 3) and (0 <= rs.num_missionaries <= 3)
        num_cannibals_valid = (0 <= self.num_cannibals <= 3) and (0 <= rs.num_cannibals <= 3)
        num_boat_valid = (0 <= self.num_boat <= 1) and (0 <= rs.num_boat <= 1)

        return num_missionaries_valid and num_cannibals_valid and num_boat_valid and self.missionaries_are_safe
