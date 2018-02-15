import unittest
from missionaries_and_cannibals import State
from missionaries_and_cannibals import perform_action
from operator import sub, add


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State((3, 3, 1))

    def tearDown(self):
        pass

    def test_initial_properties(self):
        self.assertEqual(self.state.wrong_side, (3, 3, 1))
        self.assertEqual(self.state.right_side, (0, 0, 0))
        self.assertEqual(self.state.num_boat('w'), 1)
        self.assertEqual(self.state.num_boat('r'), 0)
        self.assertEqual(self.state.num_missionaries('w'), 3)
        self.assertEqual(self.state.num_missionaries('r'), 0)
        self.assertEqual(self.state.num_cannibals('w'), 3)
        self.assertEqual(self.state.num_cannibals('r'), 0)


class TestPerformAction(unittest.TestCase):
    def setUp(self):
        self.actions = [
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        ]
        self.state = State((3, 3, 1))

    def tearDown(self):
        pass

    def test_perform_action(self):
        new_state = perform_action(sub, self.actions[0], self.state.wrong_side)
        self.assertEqual(new_state.wrong_side, (2, 3, 0))


if __name__ == '__main__':
    unittest.main()
