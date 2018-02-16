from operator import sub

MISSIONARY_IDX = 0
CANNIBAL_IDX = 1
BOAT_IDX = 2

class State:
    def __init__(self, wrong_side):
        self.wrong_side = wrong_side

    def __str__(self):
        return 'W: ' + str(self.wrong_side) + '   R: ' + str(self.right_side)

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
        return self.num_missionaries > 0 and self.num_missionaries >= self.num_cannibals

    @property
    def is_valid(self):
        num_missionaries_valid = 0 <= self.num_missionaries <= 3
        num_cannibals_valid = 0 <= self.num_cannibals <= 3
        num_boat_valid = 0 <= self.num_boat <= 1

        return num_missionaries_valid and num_cannibals_valid and num_boat_valid and self.missionaries_are_safe

