#-------------------------------------------------------------------------------
# Name:        Maleficium Game Logic
#                    Made for Maleficium: The Demon Scrolls
#                       malificiumgame.com
#
# Author:      Thomas Gull
#
# Created:     29/12/2011
#-------------------------------------------------------------------------------

DEBUG = False

DWARF = 'dwarf'
ELF = 'elf'
GRIMVALKIN = 'grimvalkin'
CONSTRUCT = 'construct'
HUMAN = 'human'

races = [DWARF, ELF, GRIMVALKIN, CONSTRUCT, HUMAN]

levels = []
for i in range(1,21):
    levels.append(i)

exp_medium = [0, 2000, 5000, 9000, 15000, 23000, 35000, \
    51000, 75000, 105000, 155000, 220000, 315000, 445000, \
    635000, 890000, 1300000, 1800000, 2550000, 3600000]

STRENGTH = 'strength'
ARMOR = 'armor'
MAGIC = 'magic'

WEAPON = 'weapon'
ARMOR = 'armor'

base_abilities = [STRENGTH,  ARMOR,  MAGIC]
base_abilities_dictionary = {STRENGTH:STRENGTH,  ARMOR:ARMOR,  MAGIC:MAGIC}
