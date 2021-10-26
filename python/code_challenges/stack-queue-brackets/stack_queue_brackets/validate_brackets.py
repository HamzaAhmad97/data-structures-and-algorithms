from stack import Stack

def validate_brackets(sequence):
    brackets = Stack()
    for ch in sequence:
        if ch in '[]{}()':
            brackets.push(ch)
    return brackets.is_empty()


