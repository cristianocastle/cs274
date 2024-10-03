import ArrayStack
 
 
class Calculator:
    def __init__(self):
        self.stack = ArrayStack.ArrayStack()
 
    def balanced_parens(self, s: str) -> bool:
        """
        This function checks if the string s contains balanced parentheses
        :param s: str type; the string to be checked
        :return: bool type; True if the string s contains balanced parentheses
        """
        # FIXME: Complete this method
        for i in s:
          if i == "(":
              self.stack.push(i)
          elif i == ")":
              if self.stack.size() == 0:
                  return False
              else:
                  self.stack.pop()
        return self.stack.size() == 0