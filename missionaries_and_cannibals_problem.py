from problem_base import ProblemBase
from state import State


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
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def value(self, state):
        pass