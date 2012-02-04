#-------------------------------------------------------------------------------
# Name:        Maleficium Game Logic
#                    Made for Maleficium: The Demon Scrolls
#                       malificiumgame.com
#
# Author:      Thomas Gull
#
# Created:     29/12/2011
#-------------------------------------------------------------------------------

WEAPON = 'weapon'
ARMOR = 'armor'
USABLE = 'usable'
COLLECTABLE = 'collectable'

item_types = [WEAPON,  ARMOR,  USABLE,  COLLECTABLE]

sword_of_truth = ['Sword of Truth',  WEAPON,  1000000,  ['STRENGTH:10','ARMOR:12','MAGIC:15'],  ['STRENGTH:25']]

# Inventory class
# Any inventory has a size (how much content an inventory can have)
# and the contents it contains.
class Inventory:
    def __init__(self,  size):
        self.size = size
        self.contents = set()
        
    def checkFull(self):
        if len(self.contents) >= self.size:
            return True
        else:
            return False
            
    def itemInsert(self, item):
        if self.checkFull() == True:
            return False
        print item
        self.contents.add(item)
        
    def itemRemove(self,  item):
        self.contents.remove(item)
        return item
        
    def itemRemoveNumber(self,  number):
        self.contents.remove(number)
        
    def getContents(self):
        return self.contents
        
    def getItem(self,  item_number):
        return self.contents[item_number]
        

# Any in-game items, must be of a valid type
# Returns true if the item is valid, or false if not.
# Every item has an equip ability, whenever an item is
# equipped, this method should be run.  It also checks
# to see if the item is EQUIPPABLE by returning
# the necessary requirements.
class Item:
    def __init__(self, type,  name,  value=0):
        if type not in item_types:
            return False
            
        self.type = type
        self.name = name
        self.value = value
        self.requirements = []
        self.ability_mods = []
        return True
        
    def getRequirements(self):
        return self.requirements
        
    def setRequirements(self,  requirements):
        self.requirements = requirements
        
    def setAbilityMods(self,  ability_mods):
        self.ability_mods = ability_mods
        
    def getAbilityMods(self):
        return self.ability_mods
        
    def setName(self,  name):
        self.name = name
        
    def getName(self):
        return self.name
        
    def getValue(self):
        return self.value
        
    def setValue(self,  value):
        self.value = value
        
    def equip(self):
        raise NotImplementedError()
        # This is the equip method
        
    def equippable(self):
        raise NotImplementedError()
        
    def __str__(self):
        return self.name
        
class Weapon(Item):
    def __init__(self,  name,  value=0):
        Item.__init__(self, WEAPON,  name,  value)
        
    def equippable(self):
        return self.getRequirements()
        
    def equip(self):
        return self.AbilityMods()
