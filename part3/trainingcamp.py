"""
Learning Step:
  - isinstance
  - factory pattern
  - random generation
  - Funcs Array or Funcs Methods for specialized.
"""
from base.warrior import Warrior
from base.archer import Archer
from base.knight import Knight
from base.berserk import Berserk


class TrainingCamp:
  class __OnlyOne:
    def __init__(self, training_month=6, available_years=3):
      self.last_months = available_years * 12
      self.lenght_training = training_month

    def recruit(self, strenght=5, life_point=25):
      """Return a random Human"""
      if life_point <= 0:
        return None
      return Warrior(strenght, life_point)

    def training(self, fighter, cls):
      if fighter.isalive():
        return cls(fighter)
      return fighter

    def check(self, fighter_type, cls):
      """Verify if fighter_type is authorized to become a cls"""
      auth = {
          Warrior: [Archer, Berserk, Knight],
          Archer: [],
          Berserk: [],
          Knight: [],
      }
      return cls in auth[fighter_type]

    def train(self, fighter, cls):
      """
      Specialize fighter:
        warrior => archer
        warrior => knight
        warrior => Berserk

        Archer => Elite Archer
        Knight => Elite Knight
        Berserk => Captain
      """
      if self.last_months <= 0:
        return fighter
      self.last_months -= self.lenght_training
      if self.check(type(fighter), cls):
        return self.training(fighter, cls)
      return fighter

  instance = None

  def __init__(self, *args, **kwargs):
    if not TrainingCamp.instance:
        TrainingCamp.instance = TrainingCamp.__OnlyOne(*args, **kwargs)

  def __getattr__(self, name):
    return getattr(self.instance, name)
