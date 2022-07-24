from stacks_queues import Queue


def multi_bracket_validation(self, string):
    open_brackets = ('{[')
    closed_bracket = ('}]')
    map = (open_brackets, closed_bracket)
    q = Queue()

    for i in string:

        if i in open_brackets:
            q.enqueue(map)
        elif i in closed_bracket:
                return True

    for i in string:
        if i not in open_brackets:
            return False

    if q.is_empty:
        return True