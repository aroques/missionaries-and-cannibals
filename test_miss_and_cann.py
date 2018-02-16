import unittest
from missionaries_and_cannibals import State
from missionaries_and_cannibals import perform_action
from operator import sub, add


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State((3, 3, 1))
        self.actions = [
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        ]

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

    def test_is_valid(self):
        try:

            expected_valid = [
                False,
                False,
                True,
                True,
                True
            ]

            state_tuple = self.state.wrong_side

            for i, action in enumerate(self.actions):
                new_state = perform_action(sub, action, state_tuple)
                self.assertEqual(expected_valid[i], new_state.is_valid())

        except AssertionError as e:
            print(e)
            print('state: {}'.format(new_state))

    def test_perform_action(self):

        expected_ws_tuples = [
            (2, 3, 0),
            (1, 3, 0),
            (3, 2, 0),
            (3, 1, 0),
            (2, 2, 0)
        ]

        expected_rs_tuples = [
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        ]

        state_tuple = self.state.wrong_side

        for i, action in enumerate(self.actions):
            new_state = perform_action(sub, action, state_tuple)
            self.assertEqual(expected_ws_tuples[i], new_state.wrong_side)
            self.assertEqual(expected_rs_tuples[i], new_state.right_side)


if __name__ == '__main__':
    unittest.main()
