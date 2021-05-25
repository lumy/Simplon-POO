
# Base

## Warrior:

LifePoint: 50
Strenght: 5

## Defender

LifePoint: 55
attack = 3
defense = 2

## Vampire

health = 40
attack = 4
vampirism = 50%

## Healer

health = 60
attack = 0

## Warlord

Attack 100
defense 2
health 100

## Knight

health = 50
attack = 6

# Evolution

Warrior:
  - Defender
    - SwordMaster (Elves & Dwarfs)
  - Knight:
    - CavalryMaster (Humans & Elves)
  - Healer:
    - Magician (Dwarfs & Humans)
  - vampire
  - Warlord

# Races:
All Races use Base class as fighter but they can have their own specialisations

# Dwarf

## Dwarf.SwordMaster --:

LifePoint: 60
attack = 4
defense = 3


## Dwarf.Magician ++:

health = 65
attack = 5
defense = 3

# Elves

## Elves.SwordMaster ++:

LifePoint: 65
attack = 5
defense = 4


## Elves.CavalryMaster --:

health = 55
attack = 6
defense = 2

# Humans

## Humans.CavalryMaster ++:

health = 60
attack = 7
defense = 3

## Humans.Magician --:

health = 65
attack = 3
defense = 2

# Weapons

## Weapon

attack = 0
health = 0
defense = 0
vampirism = 0
heal_power = 0

## Sword

Sword - health +5, attack +2, vampirism -10%

## Shield

Shield - health +20, attack -1, defense +2, vampirism -20%

## GreatAxe

GreatAxe - health -15, attack +5, defense -2, vampirism +10%

## Katana

Katana - health -20, attack +6, defense -5, vampirism +40%

## MagicWand

MagicWand - health +30, attack +3, heal_power +3