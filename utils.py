#
# Source: https://github.com/aimacode/aima-python/blob/master/utils.py
#

def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)
