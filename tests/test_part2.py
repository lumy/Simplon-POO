import unittest
from part2.warrior import Warrior
from part2.healer import Healer
from part2.knight import Knight
from part2.army import Army
from part2.vampire import Vampire
from part2.warlord import Warlord
from part2.battlefield import Battlefield


class TestPartTwo(unittest.TestCase):
  def _check_order(self, army, lst):
    self.assertEqual(len(army), len(lst))
    for elem in zip(army, lst):
      self.assertTrue(isinstance(elem[0], elem[1]))

  def test_army_move_unit(self):
    a = Army()
    a.addUnits(Healer, 2)
    a.addUnits(Knight, 1)
    a.addUnits(Warrior, 3)
    a.moveUnits()
    self._check_order(a, [Healer, Healer, Knight, Warrior, Warrior, Warrior])
    a.addUnits(Warlord, 3)
    self._check_order(a, [Healer, Healer, Knight, Warrior, Warrior, Warrior, Warlord])
    a.moveUnits()
    self._check_order(a, [Knight, Healer, Healer, Warrior, Warrior, Warrior, Warlord])
    a.pop()
    a.moveUnits()
    self._check_order(a, [Warrior, Healer, Healer, Warrior, Warrior, Warlord])

  def test_max_life(self):
    a1 = Army()
    a2 = Army()
    a1.addUnits(Vampire)
    a2.addUnits(Healer)
    b = Battlefield()
    self.assertTrue(b.simpleFight(a1, a2))
    self.assertEqual(a1[0].health, 40)
    a1 = Army()
    a2 = Army()
    a1.addUnits(Vampire)
    a1.addUnits(Healer)
    a2.addUnits(Healer, 2)
    self.assertTrue(b.simpleFight(a1, a2))
    self.assertEqual(a1[0].health, 40)

  def test_vampire(self):
    a1 = Army()
    a2 = Army()
    a1.addUnits(Vampire)
    a2.addUnits(Warrior)
    b = Battlefield()
    self.assertEqual(a1[0].health, 40)
    self.assertEqual(a1[0].strength, 4)
    self.assertEqual(a1[0].vampirism, 50)
    self.assertTrue(b.simpleFight(a1, a2))
    self.assertEqual(a1[0].health, 4)

  def test_army_knight(self):
    """           1    2    1    2    1   2    1    2     1   2     1   2    1    2    1    2    1     2   1    2
    K: 50 - 6  | 50 | 45 | 45 | 40 | 40 | 35 | 35 | 30 | 30 | 25 | 25 | 20 | 20 | 15 | 15 | 10 | 10 | 5  | 5  | 0
    W1: 50 - 5 | 44 | 44 | 38 | 38 | 32 | 32 | 26 | 26 | 20 | 20 | 14 | 14 | 8  | 8  | 2  | 2  | 0  | -  | - |
    W2: 50 - 5 | 47 | 47 | 44 | 44 | 41 | 41 | 38 | 38 | 35 | 35 | 32 | 32 | 29 | 29 | 26 | 26 | 23 | 23 | 17 | 17
    """
    a1 = Army()
    a2 = Army()
    a1.addUnits(Knight, 1)
    a2.addUnits(Warrior, 2)
    self.assertEqual(a1[0].health, 50)
    self.assertEqual(a1[0].strength, 6)
    b = Battlefield()
    ret = b.simpleFight(a1, a2)
    print(ret)
    print(len(a1), len(a2))
    self.assertFalse(ret)
    self.assertEqual(a2[0].health, 17)

  def test_healer(self):
    """    0       1   2    1    2    1    2     1    2   1    2    1    2    1    2     1    2   1    2    1   2     1
      H: 60 - 0 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 | 60 ----
      K: 50 - 6 | 50 | 45 | 47 | 42 | 44 | 39 | 41 | 36 | 38 | 33 | 35 | 30 | 32 | 27 | 29 | 24 | 26 | 21 | 23 | 18 | 20|15 | 17| 14| 14
     w1: 50 - 5 | 44 | 44 | 38 | 38 | 32 | 32 | 26 | 26 | 20 | 20 | 14 | 14 | 8  | 8  | 3  |  0  | - |  - | -  | -
     w2: 50 - 5 | 47 | 47 | 44 | 44 | 41 | 41 | 38 | 38 | 35 | 35 | 32 | 32 | 29 | 29 | 26 | 26 | 20 | 20 | 14 | 14 | 8 | 8 | 2 | 2 | 0
    """
    a1 = Army()
    a2 = Army()
    a1.addUnits(Knight, 1)
    a1.addUnits(Healer, 1)
    a2.addUnits(Warrior, 2)
    self.assertEqual(a1[1].strength, 0)
    self.assertEqual(a1[1].health, 60)
    b = Battlefield()
    self.assertTrue(b.simpleFight(a1, a2))
    self.assertEqual(a1[0].health, 14)

  def test_warlord(self):
    w = Warlord()
    self.assertEqual(w.strength, 4)
    self.assertEqual(w.defense, 2)
    self.assertEqual(w.health, 100)
    a1 = Army()
    a2 = Army()
    a1.addUnits(Warlord, 1)
    a2.addUnits(Warrior, 2)
    b = Battlefield()
    self.assertTrue(b.simpleFight(a1, a2))
    a1.addUnits(Warlord, 3)
    self.assertEqual(len(a1), 1)