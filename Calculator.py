import ArrayStack


class Calculator:
    def __init__(self):
        self.dict = None

    def balanced_parens(self, s: str) -> bool:
        """
        This function checks if the string s contains balanced parentheses
        :param s: str type; the string to be checked
        :return: bool type; True if the string s contains balanced parentheses
        """
        for char in s:
            if char == '(':
                self.stack.add(0, char)
            elif char == ')':
                if self.stack.size() == 0:
                    return False
                self.stack.remove(0)
        return self.stack.size() == 0