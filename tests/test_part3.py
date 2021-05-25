import unittest
from part3.fighter import warrior, vampire, defender, healer, knight, warlord
from part3 import elves, dwarfs, humans, battle
from part3.weapon import weapons

# Todo Test all Charactere with all Weapons ?
# Is it necessary ? not sure because i would provide the tournament code and check their codes.
# But at same way, it would help me check everything in case of.

class TestPartThreeWeapons(unittest.TestCase):
  class FakeWeapon(weapons.Weapon):
    def __init__(self):
      super().__init__()

  def test_weapon_no_instance(self):
    self.assertRaises(TypeError, lambda: weapons.Weapon(),
                      msg="""Weapon Class should be an Abstract class with Astract Method.
                      We should not be able to make an instance of if""")
    self.assertTrue(issubclass(weapons.Sword, weapons.Weapon))

  def test_simple_stats_weapon(self):
    # LifePoint: 50 / Strenght: 5
    w = warrior.Warrior()

    # Health +5 attack +2 vampirism -10
    a = weapons.Sword()
    if True:
      r = w.equipWeapon(a)
      self.assertIsNone(r)
      self.assertEqual(w.health, 55)
      self.assertEqual(w.strength, 7)
      self.assertEqual(getattr(w, "vampirism", None), None)

    # Health +20 attack -1 defense +2 vampirism +10
    b = weapons.Shield()
    if True:
      # 70 4 def 0 vamp 0
      _a = w.equipWeapon(b)
      self.assertIs(a, _a)
      self.assertIsInstance(_a, type(a))
      self.assertEqual(w.health, 70)
      self.assertEqual(w.strength, 4)
      self.assertEqual(getattr(w, "defense", None), None)
      self.assertEqual(getattr(w, "vampirism", None), None)

    # H -15 a +5 d -2 v +10
    c = weapons.GreatAxe()
    if True:
      # h 35 A 10 d 0 v 0
      _b = w.equipWeapon(c)
      self.assertIs(b, _b)
      self.assertIsInstance(_b, type(b))
      self.assertEqual(w.health, 35)
      self.assertEqual(w.strength, 10)
      self.assertEqual(getattr(w, "defense", None), None)
      self.assertEqual(getattr(w, "vampirism", None), None)

    # H -20 a +6 d -5 v +40
    d = weapons.Katana()
    if True:
      # h 30 a 11 d 0 v 0
      w.equipWeapon(d)
      self.assertEqual(w.health, 30)
      self.assertEqual(w.strength, 11)
      self.assertEqual(getattr(w, "defense", None), None)
      self.assertEqual(getattr(w, "vampirism", None), None)

    # H +30 a +3 hl +3
    e = weapons.MagicWand()
    if True:
      # h 80 a 8 hl 0
      w.equipWeapon(e)
      self.assertEqual(w.health, 80)
      self.assertEqual(w.strength, 8)
      self.assertEqual(getattr(w, "heal_power", None), None)

  def test_vampirism_stat(self):
    # 5 2 -10
    s = weapons.Sword()
    v = vampire.Vampire()
    self.assertIsNone(v.equipWeapon(s))
    self.assertEqual(v.health, 45)
    self.assertEqual(v.strength, 6)
    self.assertEqual(v.vampirism, 40)
    s = weapons.Shield()
    self.assertIsNotNone(v.equipWeapon(s))
    self.assertEqual(v.health, 60)
    self.assertEqual(v.strength, 3)
    self.assertEqual(v.vampirism, 30)
    # test if math.floor is used
    v.damaged(1)
    self.assertEqual(v.health, 59)
    v.getBlood()
    self.assertEqual(v.health, 59)
    v.equipWeapon(TestPartThreeWeapons.FakeWeapon())
    self.assertEqual(v.vampirism, 50)
    # TODO finish test all weapon vampirism stat

  def test_defense_start(self):
    d = defender.Defender()
    s = weapons.Sword()
    self.assertIsNone(d.equipWeapon(s))
    self.assertEqual(d.strength, 5)
    self.assertEqual(d.health, 60)
    self.assertEqual(getattr(d, "vampirism", None), None)
    self.assertEqual(d.defense, 2)
    s = weapons.Shield()
    self.assertIsNotNone(d.equipWeapon(s))
    self.assertEqual(d.strength, 2)
    self.assertEqual(d.health, 75)
    self.assertEqual(getattr(d, "vampirism", None), None)
    self.assertEqual(d.defense, 4)
    d.damaged(4)
    self.assertEqual(d.health, 75)
    d.damaged(6)
    self.assertEqual(d.health, 73)
    # TODO write test with all weapons

  def test_heal_power(self):
    h = healer.Healer()
    s = weapons.Sword()
    m = weapons.MagicWand()
    self.assertIsNone(h.equipWeapon(m))
    self.assertEqual(h.health, 90)
    self.assertEqual(h.strength, 3)
    self.assertEqual(h.heal(), 5)
    self.assertIsNotNone(h.equipWeapon(s))
    self.assertEqual(h.health, 65)
    self.assertEqual(h.strength, 2)
    self.assertEqual(h.heal(), 2)
    # Todo Test with other weapon

class TestPartThreeRaces(unittest.TestCase):
  def test_sword_master(self):
    s1 = elves.swordmaster.SwordMaster()
    self.assertEqual(s1.health, 65)
    self.assertEqual(s1.strength, 5)
    self.assertEqual(s1.defense, 4)
    self.assertTrue(issubclass(elves.swordmaster.SwordMaster, defender.Defender))
    self.assertTrue(issubclass(dwarfs.swordmaster.SwordMaster, defender.Defender))
    s2 = dwarfs.swordmaster.SwordMaster()
    self.assertEqual(s2.health, 60)
    self.assertEqual(s2.strength, 4)
    self.assertEqual(s2.defense, 3)
    s1.damaged(5)
    self.assertEqual(s1.health, 64)
    s2.damaged(4)
    self.assertEqual(s2.health, 59)

  def test_cavalry_master(self):
    c1 = elves.cavalry.CavalryMaster()
    c2 = humans.cavalry.CavalryMaster()
    self.assertEqual(c1.health, 55)
    self.assertEqual(c1.strength, 6)
    self.assertEqual(c1.defense, 2)
    self.assertTrue(issubclass(elves.cavalry.CavalryMaster, knight.Knight))
    self.assertTrue(issubclass(humans.cavalry.CavalryMaster, knight.Knight))
    self.assertEqual(c2.health, 60)
    self.assertEqual(c2.strength, 7)
    self.assertEqual(c2.defense, 3)
    c1.damaged(3)
    self.assertEqual(c1.health, 54)
    c2.damaged(4)
    self.assertEqual(c2.health, 59)

  def test_magician(self):
    m1 = humans.magician.Magician()
    m2 = dwarfs.magician.Magician()
    self.assertEqual(m1.health, 65)
    self.assertEqual(m1.strength, 2)
    self.assertEqual(m1.defense, 2)
    self.assertTrue(issubclass(humans.magician.Magician, healer.Healer))
    self.assertTrue(issubclass(dwarfs.magician.Magician, healer.Healer))
    self.assertEqual(m2.health, 65)
    self.assertEqual(m2.strength, 5)
    self.assertEqual(m2.defense, 3)
    m1.damaged(3)
    self.assertEqual(m1.health, 64)
    m2.damaged(4)
    self.assertEqual(m2.health, 64)

class TestPartThreeTrainingCamp(unittest.TestCase):

  def test_training_level_training_camp(self):
    """This test create one unit of each type, One specialized Unit of each type. Assert if a specialization
    shoudln't be in a race."""
    def train_all(tr, us):
      us[0] = tr.trainDefender(us[0])
      self.assertIsInstance(us[0], defender.Defender)
      us[1] = tr.trainKnight(us[1])
      self.assertIsInstance(us[1], knight.Knight)
      us[2] = tr.trainHealer(us[2])
      self.assertIsInstance(us[2], healer.Healer)
      us[3] = tr.trainVampire(us[3])
      self.assertIsInstance(us[3], vampire.Vampire)
      us[4] = tr.trainWarlord(us[4])
      self.assertIsInstance(us[4], warlord.Warlord)

    def _test_race_camp(camp, race):
      etr = camp(30, 30, 3)
      us = [etr.recruitWarrior() for _ in range(30)]
      train_all(etr, us)
      # Defender, Knight, Healer, Vampire, Warlord, Warriors...
      self.assertIsInstance(us[0], defender.Defender)
      us[0] = etr.trainDefender(us[0])
      self.assertIsInstance(us[0], defender.Defender)
      us[0] = etr.trainKnight(us[0])
      self.assertIsInstance(us[0], defender.Defender)

      if race is humans:
        l = lambda: etr.trainSwordMaster(us[0])
        # msg="%s camp should not be able to train cavalry" % race.__name__
        self.assertRaises(NotImplementedError, l)
      else:
        us[0] = etr.trainSwordMaster(us[0])
        self.assertIsInstance(us[0], getattr(race, "swordmaster").SwordMaster)

      if race is dwarfs:
        l = lambda: etr.trainCavalryMaster(us[1])
        # msg="%s camp should not be able to train cavalry" % race.__name__
        self.assertRaises(NotImplementedError, l)
      else:
        us[1] = etr.trainCavalryMaster(us[1])
        self.assertIsInstance(us[1], getattr(race, "cavalry").CavalryMaster)

      if race is elves:
        l = lambda: etr.trainMagician(us[2])
        # msg="%s camp should not be able to train magician" % race.__name__
        self.assertRaises(NotImplementedError, l)
      else:
        us[2] = etr.trainMagician(us[2])
        self.assertIsInstance(us[2], getattr(race, "magician").Magician)

    _test_race_camp(dwarfs.trainingcamp.TrainingCamp, dwarfs)
    _test_race_camp(elves.trainingcamp.TrainingCamp, elves)
    _test_race_camp(humans.trainingcamp.TrainingCamp, humans)

  def test_amount_time_training(self):
    def _test_(train, amount, time, tr_max):
      check = False
      if (amount*12) % time != 0:
        check = (amount*12)%time
      tr = train(300, amount, time)
      wl = [tr.recruitWarrior() for _ in range(100)]
      r = []
      for i, o in enumerate(wl):
        if tr_max > 0:
          r.append(tr.trainDefender(o))
          tr_max -= 1
        else:
          if check is not False:
            self.assertEqual(check, tr.time_available)
          self.assertTrue(type(tr.trainDefender(o)) == warrior.Warrior, msg="First Loop")

    for i in [elves.trainingcamp.TrainingCamp, dwarfs.trainingcamp.TrainingCamp, humans.trainingcamp.TrainingCamp]:
      _test_(i, 1, 3, 4)
      _test_(i, 1, 5, 2)
      _test_(i, 1, 2, 6)
      _test_(i, 1, 11, 1)
      _test_(i, 4, 5, 9)
      _test_(i, 4, 3, 16)

  def test_amount_warrior(self):
    def _test_(train, num):
      tr = train(num, 0, 0)
      wl = [tr.recruitWarrior() for _ in range(num)]
      self.assertEqual(len(wl), num)
      [self.assertIsNone(tr.recruitWarrior()) for i in range(num)]

    _test_(elves.trainingcamp.TrainingCamp, 30)
    _test_(dwarfs.trainingcamp.TrainingCamp, 30)
    _test_(humans.trainingcamp.TrainingCamp, 30)

class TestPartThreeArmy(unittest.TestCase):
  """
  Should Test:
    doesn't recruit more than possible: max_recruit
    keep same size at all train operation and doesnt goes higher than traning time: max_training_time
    can train all units and not train the outside classes/races
  """
  def test_max_recruit(self):
    t = elves.trainingcamp.TrainingCamp(12, 1000, 1)
    army = battle.army.Army(t)
    army.recruitWarriors(15)
    self.assertEqual(len(army), 12)
    self.assertIsNone(getattr(army, "addUnits", None))

  def test_all_training(self):

    def _test_(self, t, fs):
      army = battle.army.Army(t)
      army.recruitWarriors(12)
      self.assertEqual(len(army), 12)
      army.trainUnit(defender.Defender)
      army.trainUnit(vampire.Vampire)
      army.trainUnit(healer.Healer)
      army.trainUnit(knight.Knight)
      army.trainUnit(warlord.Warlord)
      self.assertEqual(len(army), 12)
      self.assertEqual([type(army[i]) == defender.Defender for i in range(len(army))].count(True), 1)
      self.assertEqual([type(army[i]) == vampire.Vampire for i in range(len(army))].count(True), 1)
      self.assertEqual([type(army[i]) == healer.Healer for i in range(len(army))].count(True), 1)
      self.assertEqual([type(army[i]) == knight.Knight for i in range(len(army))].count(True), 1)
      self.assertEqual([type(army[i]) == warlord.Warlord for i in range(len(army))].count(True), 1)
      self.assertEqual([type(army[i]) == warrior.Warrior for i in range(len(army))].count(True), 7)
      for f in fs:
        f[0](army)
        f[1](army)
      self.assertEqual([type(army[i]) == warrior.Warrior for i in range(len(army))].count(True), 7)

    elves_tests = (
      (lambda x: x.trainUnit(elves.cavalry.CavalryMaster),
       lambda x: self.assertEqual([type(x[i]) == elves.cavalry.CavalryMaster for i in range(len(x))].count(True), 1)),
      (lambda x: x.trainUnit(elves.swordmaster.SwordMaster),
       lambda x: self.assertEqual([type(x[i]) == elves.swordmaster.SwordMaster for i in range(len(x))].count(True), 1)),
      (lambda x: self.assertRaises(NotImplementedError, lambda: x.trainUnit(dwarfs.magician.Magician)),
       lambda x: self.assertEqual([type(x[i]) == dwarfs.magician.Magician for i in range(len(x))].count(True), 0)))
    t = elves.trainingcamp.TrainingCamp(12, 1000, 1)
    _test_(self, t, elves_tests)

    elves_tests = (
      (lambda x: x.trainUnit(humans.cavalry.CavalryMaster),
       lambda x: self.assertEqual([type(x[i]) == elves.cavalry.CavalryMaster for i in range(len(x))].count(True), 1)),
      (lambda x: x.trainUnit(dwarfs.swordmaster.SwordMaster),
       lambda x: self.assertEqual([type(x[i]) == elves.swordmaster.SwordMaster for i in range(len(x))].count(True), 1)),
      (lambda x: self.assertRaises(NotImplementedError, lambda: x.trainUnit(dwarfs.magician.Magician)),
       lambda x: self.assertEqual([type(x[i]) == dwarfs.magician.Magician for i in range(len(x))].count(True), 0)))
    t = elves.trainingcamp.TrainingCamp(12, 1000, 1)
    _test_(self, t, elves_tests)

    fs = (
      (lambda x: x.trainUnit(dwarfs.magician.Magician),
       lambda x: self.assertEqual([type(x[i]) == dwarfs.magician.Magician for i in range(len(x))].count(True), 1)),
      (lambda x: x.trainUnit(dwarfs.swordmaster.SwordMaster),
       lambda x: self.assertEqual([type(x[i]) == dwarfs.swordmaster.SwordMaster for i in range(len(x))].count(True),                                  1)),
      (lambda x: self.assertRaises(NotImplementedError, lambda: x.trainUnit(humans.cavalry.CavalryMaster)),
       lambda x: self.assertEqual([type(x[i]) == humans.cavalry.CavalryMaster for i in range(len(x))].count(True), 0)))
    t = dwarfs.trainingcamp.TrainingCamp(12, 1000, 1)
    _test_(self, t, fs)
    fs = (
      (lambda x: x.trainUnit(humans.magician.Magician),
       lambda x: self.assertEqual([type(x[i]) == dwarfs.magician.Magician for i in range(len(x))].count(True), 1)),
      (lambda x: x.trainUnit(elves.swordmaster.SwordMaster),
       lambda x: self.assertEqual([type(x[i]) == dwarfs.swordmaster.SwordMaster for i in range(len(x))].count(True),1)),
      (lambda x: self.assertRaises(NotImplementedError, lambda: x.trainUnit(elves.cavalry.CavalryMaster)),
       lambda x: self.assertEqual([type(x[i]) == elves.cavalry.CavalryMaster for i in range(len(x))].count(True), 0)))
    t = dwarfs.trainingcamp.TrainingCamp(12, 1000, 1)
    _test_(self, t, fs)

    fs = (
      (lambda x: x.trainUnit(humans.magician.Magician),
       lambda x: self.assertEqual([type(x[i]) == humans.magician.Magician for i in range(len(x))].count(True), 1)),
      (lambda x: x.trainUnit(humans.cavalry.CavalryMaster),
       lambda x: self.assertEqual([type(x[i]) == humans.cavalry.CavalryMaster for i in range(len(x))].count(True), 1)),
      (lambda x: self.assertRaises(NotImplementedError, lambda: x.trainUnit(dwarfs.swordmaster.SwordMaster)),
       lambda x: self.assertEqual([type(x[i]) == dwarfs.swordmaster.SwordMaster for i in range(len(x))].count(True), 0)))
    t = humans.trainingcamp.TrainingCamp(12, 1000, 1)
    _test_(self, t, fs)

    fs = (
      (lambda x: x.trainUnit(dwarfs.magician.Magician),
       lambda x: self.assertEqual([type(x[i]) == humans.magician.Magician for i in range(len(x))].count(True), 1)),
      (lambda x: x.trainUnit(elves.cavalry.CavalryMaster),
       lambda x: self.assertEqual([type(x[i]) == humans.cavalry.CavalryMaster for i in range(len(x))].count(True), 1)),
      (lambda x: self.assertRaises(NotImplementedError, lambda: x.trainUnit(elves.swordmaster.SwordMaster)),
       lambda x: self.assertEqual([type(x[i]) == elves.swordmaster.SwordMaster for i in range(len(x))].count(True), 0)))
    t = humans.trainingcamp.TrainingCamp(12, 1000, 1)
    _test_(self, t, fs)

  def test_max_training_time(self):
    t = elves.trainingcamp.TrainingCamp(12, 1, 6)
    army = battle.army.Army(t)
    army.recruitWarriors(12)
    self.assertEqual(len(army), 12)
    army.trainUnit(defender.Defender)
    army.trainUnit(defender.Defender)
    self.assertEqual(len(army), 12)
    self.assertEqual([type(army[i]) == defender.Defender for i in range(len(army))].count(True), 2)
    self.assertEqual([type(army[i]) == warrior.Warrior for i in range(len(army))].count(True), 10)
    army.trainUnit(defender.Defender)
    army.trainUnit(defender.Defender)
    self.assertEqual(len(army), 12)
    self.assertEqual([type(army[i]) == defender.Defender for i in range(len(army))].count(True), 2)
    self.assertEqual([type(army[i]) == warrior.Warrior for i in range(len(army))].count(True), 10)

class TestPartThreeBattle(unittest.TestCase):
  """
  Should Test 2 Army battling:
    Cavalry fight like knight
    Magician Can heal and fight (can he fight from 2nd position ?)
    Warlod Organization is left at free: No test
  """
  def test_knight(self):
    """TODO Create a GodArmy and verify player army"""
    b = battle.battlefield.Battlefield()
    tr = elves.trainingcamp.TrainingCamp(300, 10, 1)
    tr2 = humans.trainingcamp.TrainingCamp(300, 10, 1)
    a = battle.army.Army(tr)
    a2 = battle.army.Army(tr2)
    a.recruitWarriors(7)
    a2.recruitWarriors(1)
    a2.trainUnit(knight.Knight)
    a2.trainUnit(humans.cavalry.CavalryMaster)
    r = b.simpleFight(a, a2)
    self.assertTrue(r)
    self.assertEqual(a[0].health, 28)
    self.assertEqual(a[1].health, 47)

  # def test_magician(self):
  #   b = battle.battlefield.Battlefield()
  #   tr = elves.trainingcamp.TrainingCamp(300, 10, 1)
  #   tr2 = dwarfs.trainingcamp.TrainingCamp(300, 10, 1)
  #   a = battle.army.Army(tr)
  #   a2 = battle.army.Army(tr2)

  # def test_battle_with_weapons():
  #  pass