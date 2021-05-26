import unittest
from part1.warrior import Warrior
from part1.fight import fight
from part1.defender import Defender
from part1.army import Army
from part1.battlefield import Battlefield

class TestBaseModule(unittest.TestCase):
  def test_warrior(self):
    w = Warrior(10, 20)
    self.assertTrue(getattr(w, "presentation", False))
    self.assertEqual(w.presentation(), "Warrior 20 life point and 10 strength.")
    self.assertEqual(w.strength, 10)
    self.assertEqual(w.isalive(), True)
    self.assertEqual(w.health, 20)
    w.damaged(2)
    self.assertEqual(w.health, 18)
    w.damaged(5)
    self.assertEqual(w.health, 13)
    w.damaged(25)
    self.assertEqual(w.isalive(), False)
    self.assertEqual(w.health, 0)
    self.assertTrue(getattr(w, "presentation", False))
    self.assertEqual(w.presentation(), "Warrior 0 life point and 10 strength.")

  def test_fight_units(self):
    w = Warrior()
    w2 = Warrior()
    self.assertTrue(fight(w, w2))
    w = Warrior(10, 20)
    w2 = Warrior(15, 30)
    self.assertFalse(fight(w, w2))
    w = Warrior(10, 20)
    w2 = Warrior(15, 30)
    self.assertTrue(fight(w2, w))
    self.assertFalse(fight(w, w2))
    w = Warrior(1, 20)
    w2 = Warrior(1, 21)
    self.assertTrue(fight(w2, w))
    w = Warrior(1, 20)
    w2 = Warrior(1, 21)
    self.assertFalse(fight(w, w2))

  def test_defender_units(self):
    k = Defender()
    self.assertTrue(issubclass(type(k), Warrior))
    self.assertEqual(k.strength, 3)
    self.assertEqual(k.health, 55)
    self.assertEqual(k.defense, 2)
    k.damaged(5)
    self.assertEqual(k.health, 52)
    k = Defender(defense=10)
    k.damaged(5)
    self.assertEqual(k.health, 55)

  def test_army(self):
    army = Army()
    army.addUnits(Warrior, 3)
    army.addUnits(Defender, 1)
    self.assertEqual(army[0].strength, 5)
    self.assertEqual(army[3].strength, 3)
    self.assertTrue(isinstance(army[3], Defender))
    self.assertFalse(isinstance(army[0], Defender))

  def test_battlefield(self):
    army = Army()
    army.addUnits(Warrior, 3)
    army.addUnits(Defender, 1)
    army2 = Army()
    army2.addUnits(Warrior, 1)
    army2.addUnits(Defender, 3)
    battlefield = Battlefield()
    self.assertTrue(battlefield.simpleFight(army, army2))
    self.assertEqual(len(army2), 0)
    self.assertEqual(len(army), 1)
    army = Army()
    army.addUnits(Warrior, 2)
    army.addUnits(Defender, 1)
    army2 = Army()
    army2.addUnits(Warrior, 3)
    army2.addUnits(Defender, 3)
    battlefield = Battlefield()
    self.assertFalse(battlefield.simpleFight(army, army2))
    self.assertEqual(len(army), 0)
    self.assertEqual(len(army2), 3)
