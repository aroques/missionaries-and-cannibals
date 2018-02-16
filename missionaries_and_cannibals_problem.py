from problem_base import ProblemBase
from node import Node
from state import State
from operator import sub, add

class MissionariesAndCannibalsProblem(ProblemBase):

    """Missionaries and Cannibals problem class"""

    def __init__(self, initial_state, goal, actions):
        """The constructor specifies the initial state, and goal state."""
        self.actions = actions
        super.__init__(initial_state, goal)

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        all_states = [self.result(state, action) for action in self.actions]
        valid_states = filter(lambda state: state.is_valid, all_states)
        return [state.action for state in valid_states]

        for action in self.actions:
            self.result(state, action)

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        if action not in self.actions:
            raise Exception('action not in actions!')

        if state.depth % 2 == 0:
            result = self.perform_action(sub, state, action)
        else:
            result = self.perform_action(add, state, action)

        return result

    def value(self, state):
        pass

    @staticmethod
    def perform_action(arithmetic_operator, action, state):
        new_state_tuple = tuple(map(arithmetic_operator, state, action))
        new_state = State(new_state_tuple)
        return Node(new_state)
