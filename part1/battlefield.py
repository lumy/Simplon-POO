
class Battlefield():
  """Battlefield used to battle two army against each other"""

  def simpleFight(self, army, army2):
    """
    :param army: First army
    :param army2: Second army
    :return bool: Did the first army won ?
    """
    unit_1 = army.pop()
    unit_2 = army2.pop()
    while True:
      ret = fight(unit_1, unit_2)
      if not ret:
        unit_1 = army.pop()
      else:
        unit_2 = army2.pop()
      return unit_1.isalive()
