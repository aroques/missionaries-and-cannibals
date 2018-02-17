import unittest
from state import State
from node import Node
from missionaries_and_cannibals_problem import MissionariesAndCannibalsProblem


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
        self.assertEqual(self.state.num_boat, 1)
        self.assertEqual(self.state.num_missionaries, 3)
        self.assertEqual(self.state.num_cannibals, 3)

    def test_missionaries_are_safe(self):
        exp_safe = [
            State((3, 0, 1)),
            State((3, 0, 0)),
            State((0, 3, 1)),
            State((0, 3, 0)),
            State((2, 2, 1)),
            State((2, 2, 0)),
            State((3, 2, 1))
        ]

        for state in exp_safe:
            self.assertTrue(state.missionaries_are_safe, 'missionaries should be safe. state: {}'.format(state))

class TestMissAndCannProblem(unittest.TestCase):
    def setUp(self):
        initial_state = State((3, 3, 1))
        goal_state = State((0, 0, 0))

        actions = [
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        ]

        self.problem = MissionariesAndCannibalsProblem(initial_state, goal_state, actions)
        self.root_node = Node(self.problem.initial_state)

    def tearDown(self):
        pass

    def test_actions(self):
        actions = self.problem.actions(self.root_node)

        self.assertEqual(3, len(actions))

        expected_actions = [
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        ]

        for i, exp_action in enumerate(expected_actions):
            self.assertEqual(exp_action, actions[i])

    def test_result(self):
        actions = self.problem.actions(self.root_node)
        result = self.problem.result(self.root_node, actions[0])
        exp_node = Node(State((3, 2, 0)), self.root_node, actions[0])
        self.assertEqual(exp_node, result)

    def test_goal_is(self):
        node = Node(State((0, 0, 0)))
        node_is_goal = self.problem.goal_is(node.state)
        self.assertTrue(node_is_goal)

class TestNode(unittest.TestCase):
    def setUp(self):
        initial_state = State((3, 3, 1))
        goal_state = State((0, 0, 0))

        actions = [
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        ]

        self.problem = MissionariesAndCannibalsProblem(initial_state, goal_state, actions)
        self.root_node = Node(self.problem.initial_state)
        self.actions = self.problem.actions(self.root_node)

    def tearDown(self):
        pass

    def test_expand(self):
        next_nodes = self.root_node.expand(self.problem)
        exp_nodes = [
            Node(State((3, 2, 0)), self.root_node, self.actions[0]),
            Node(State((3, 1, 0)), self.root_node, self.actions[1]),
            Node(State((2, 2, 0)), self.root_node, self.actions[2])
        ]
        self.assertEqual(3, len(next_nodes))

        for i, nxt_node in enumerate(next_nodes):
            self.assertEqual(exp_nodes[i], nxt_node)

    def test_child_node(self):
        child = self.root_node.child_node(self.problem, self.actions[0])
        exp_child = Node(State((3, 2, 0)), self.root_node, self.actions[0])

        self.assertEqual(exp_child, child)


if __name__ == '__main__':
    unittest.main()
