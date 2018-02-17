from problem_base import ProblemBase
from node import Node

class MissionariesAndCannibalsProblem(ProblemBase):

    """Missionaries and Cannibals problem class"""

    def __init__(self, initial_state, goal_state, actions):
        """The constructor specifies the initial state, and goal state."""
        self.all_possible_actions = actions
        super().__init__(initial_state, goal_state)

    def actions(self, node):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        all_nodes = [self.__perform_action(node, action) for action in self.all_possible_actions]
        valid_nodes = filter(lambda n: n.state.is_valid, all_nodes)
        return [n.action for n in valid_nodes]

    def result(self, node, action):
        """Return the node that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        if action not in self.actions(node):
            raise Exception('action not in actions!')

        return self.__perform_action(node, action)

    @staticmethod
    def __perform_action(node, action):
        """Return the node that results from executing the given
        action in the given state."""
        if node.depth % 2 == 0:
            state = node.state - action
        else:
            state = node.state + action

        return Node(state, node, action)

    def value(self, state):
        pass
