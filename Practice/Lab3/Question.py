def is_valid(sequence):
    stack = []
    for i in sequence:
        if i in '({[':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if i == ")" and stack[-1] != '(':
                return False
            if i == "}" and stack[-1] != '{':
                return False
            if i == "]" and stack[-1] != '[':
                return False
            stack.pop(-1)
    if len(stack) != 0:
        return False
    return True


class Sequence():
    def __init__(self, string):
        self.cor = True
        self.string = string
    
    def validity(self):
        return is_valid(self.string)
    
    """def validity2(self):
        stack = []
        for i in self.string:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ")" and stack[-1] != '(':
                    return False
                if i == "}" and stack[-1] != '{':
                    return False
                if i == "]" and stack[-1] != '[':
                    return False
                stack.pop(-1)
        if len(stack) != 0:
            return False
        return True
"""

test = Sequence(input())
test2 = Sequence("{[(]})")
print(test.validity())
print(test2.validity())