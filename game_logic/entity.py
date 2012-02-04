#-------------------------------------------------------------------------------
# Name:        Maleficium Game Logic
#                    Made for Maleficium: The Demon Scrolls
#                       malificiumgame.com
#
# Author:      Thomas Gull
#
# Created:     29/12/2011
#-------------------------------------------------------------------------------

import base_vars
from inventory import Inventory

class Entity:
    def __init__(self):
        self.name = None
        self.race = None
        self.abilities = {}
        for each in base_vars.base_abilities:
            self.abilities[each] = 10
        self.inventory = Inventory(10)
        self.initPermVar()

    def initPermVar(self):
        # This method is used to keep track of
        # character's permanent values in case
        # of temporary changes.
        pass

    def setName(self, new_name):
        self.name = new_name

    def getName(self):
        return self.name

    def setRace(self, new_race):
        if new_race in base_vars.races:
            self.race = new_race

    def getRace(self):
        return self.race

    def getAbilityScore(self, ability):
        return self.abilities[ability]
        
    def setAbilityScore(self,  ability,  score):
        self.abilities[ability] = score
        
    def incAbilityScore(self,  ability,  value):
        self.abilities[ability] += value
        
    def giveItem(self,  item):
        self.inventory.itemInsert(item)
    
    def removeItem(self,  item):
        removed_item = self.inventory.itemRemove(item)
        return removed_item
        
    def checkRequirements(self,  requirements):
        req_success = False
        req_met = 0
        req_needed = len(requirements)
        for each in requirements:
            ability,  score = each.split(':')
            if self.getAbilityScore(ability) >= int(score):
                req_met += 1
            else:
                req_met += 0
        if( req_met == req_needed ):
            req_success = True
        else:
            req_success = False
        return req_success
        
    def equip(self,  item):
        if self.checkRequirements(item.getRequirements()) == False:
            return False
        for each in item.getAbilityMods():
            ability,  score = each.split(':')
            self.incAbilityScore(ability,  int(score))
        return True
        
    def getInventory(self):
        return self.inventory.getContents()
        
    def __str__(self):
        return self.name
