class StackException(Exception):
  """this class implementing StackException"""

  def __init__(self, message=None):
    self.message = message
    super().__init__(message)

class Stack(object):
  """this class implementing stack, and support read and extraction"""
  """in this stack you can store only 512 values"""

  def __init__(self):
    self.vault = []

  def __enter__(self):
    return Stack()

  def __exit__(self,exc_type, exc_val, exc_tb):
    return 1

  def get(self):
    if len(self.vault) == 0:
      raise StackException("stack is empty")
    else:
      return self.vault[len(self.vault) - 1]

  def add(self, value):
    if len(self.vault) == 512:
      raise StackException("stack overflow")
    else:
      self.vault.append(value)
      return 1

  def invert(self):
    self.vault = self.vault[::-1]
    return 1




