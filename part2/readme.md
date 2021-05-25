
# Part2 Learn and imitate.

Take your files from part1 and copy them.
You will have to update your Battlefield class and functions.
Let's add some new Classes

## The Vampire

Vampire should be a subclass of the Warrior class and have the additional "vampirism" parameter, which helps him to heal himself.
When the Vampire hits another unit, he regains health by up to 50% of the damage he dealt (enemy defense lowers the damage dealt).
The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%

You should store vampirism attribute as an integer (50 for 50%).

# The Knight

Knight should be a subclass of the Warrior class and should attack in a specific way - when he
hits the other unit, he also deals 50% of the deal damage to the next enemy unit in line (the one standing behind the
target). In case of a float number it should always be rounded down. (3.6 => 3, 2.1 => 2)

The basic parameters of the Knight:
health = 50
attack = 6

# The Healer

The battle continues and each army is losing good warriors. Let's try to fix that and add a new unit type - the Healer.
Healer won't be fighting (his attack = 0, so he can't deal damage). But his role is also very important - every time an allied soldier hits the enemy, the Healer will heal the ally standing right in front of him by +2 health points with the heal() method. Note that the health after healing can't be greater than the maximum health of the unit. For example, if the Healer heals a Warrior with 49 health points remaining, the Warrior will have 50 hp, because this is the maximum for him.

The basic parameters of the Healer:
health = 60
attack = 0

# Warlord

 Warlord should be a subclass of the Warrior class and have the following characteristics:

health = 100
attack = 4
defense = 2

Also, when the Warlord is included in any of the armies, that particular army gets to use  `moveUnits()`
method which allows rearranging the units of that army for a better battle result.
The rearrangement is done not only before the battle,
but during the battle too, each time any allied units die.
The rules for the rearrangement are as follow:

    If there are Knights in the army, they should be placed in front of everyone else.
    If there is a Healer in the army, he should be placed right after the first soldier to heal him during the fight.
    If the number of Healers is > 1, all of them should be placed right behind the first Healer.
    If there are no more Knights in the army, but there are other soldiers who can deal damage, they also should be
       placed in first position, and the Healer should stay in the 2nd row (if army still has Healers).
    Warlord should always stay way in the back to look over the battle and rearrange the soldiers when it's needed.
    Every army can not have no more than 1 Warlord.
    If the army doesn’t have a Warlord, it can’t use the moveUnits() method.
