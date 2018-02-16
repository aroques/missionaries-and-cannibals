from operator import sub


class State:
    def __init__(self, wrong_side):
        self.wrong_side = wrong_side

    def __str__(self):
        return 'W: ' + str(self.wrong_side) + '   R: ' + str(self.right_side)

    @property
    def right_side(self):
        total = (3, 3, 1)
        return tuple(map(sub, total, self.wrong_side))

    def num_missionaries(self, side):
        if side == 'w':
            return self.wrong_side[0]
        elif side == 'r':
            return self.right_side[0]
        else:
            raise ValueError('Invalid index: ' + side)

    def num_cannibals(self, side):
        if side == 'w':
            return self.wrong_side[1]
        elif side == 'r':
            return self.right_side[1]
        else:
            raise ValueError('Invalid index: ' + side)

    def num_boat(self, side):
        if side == 'w':
            return self.wrong_side[2]
        elif side == 'r':
            return self.right_side[2]
        else:
            raise ValueError('Invalid index: ' + side)

    def is_valid(self):
        missionaries_valid = 0 <= self.num_missionaries('w') <= 3 and 0 <= self.num_missionaries('r') <= 3
        cannibals_valid = 0 <= self.num_cannibals('w') <= 3 and 0 <= self.num_cannibals('r') <= 3
        boat_valid = 0 <= self.num_boat('w') <= 1 and 0 <= self.num_boat('r') <= 1

        if missionaries_valid and cannibals_valid and boat_valid and self.missionaries_are_safe():
            return True
        else:
            return False

    def missionaries_are_safe(self):
        missionaries_are_safe = True
        if 0 < self.num_missionaries('w') < self.num_cannibals('w'):
            missionaries_are_safe = False
        if 0 < self.num_missionaries('r') < self.num_cannibals('r'):
            missionaries_are_safe = False

        return missionaries_are_safe
