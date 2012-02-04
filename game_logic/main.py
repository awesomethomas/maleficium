#-------------------------------------------------------------------------------
# Name:        Maleficium Game Logic
#                    Made for Maleficium: The Demon Scrolls
#                       malificiumgame.com
#
#           Please note that this is temporarily using the
#           Pathfinder game mechanics.
#
# Author:     Thomas Gull
#
# Created:     29/12/2011
#-------------------------------------------------------------------------------

# 

import base_vars
from entity import Entity
from debugger import *
import inventory

def main():
    sword_of_truth_data = ['Sword of Truth',  base_vars.WEAPON,  1000000,  ['strength:10','armor:12','magic:15'],  ['strength:25']]
    sword_of_truth = inventory.Weapon(sword_of_truth_data[0], sword_of_truth_data[2])
    sword_of_truth.setRequirements(sword_of_truth_data[3])
    sword_of_truth.setAbilityMods(sword_of_truth_data[4])
    tommy = Entity()
    tommy.setName('Tommy Gunn')
    tommy.setRace(base_vars.ELF)
    t = "Name: %s Race: %s" % (str(tommy),  tommy.getRace().capitalize())
    print t
    tommy.setAbilityScore('armor', 12)
    tommy.setAbilityScore('magic', 15)
    print "Ability Scores: "
    for each in base_vars.base_abilities:
        ability_str = '%s: %d' % (each,  tommy.getAbilityScore(each))
        print ability_str
    tommy.giveItem(sword_of_truth)
    if( tommy.equip(sword_of_truth) ):
        print "Ability Scores: "
        for each in base_vars.base_abilities:
            ability_str = '%s: %d' % (each,  tommy.getAbilityScore(each))
            print ability_str
    
if __name__ == '__main__':
    main()
