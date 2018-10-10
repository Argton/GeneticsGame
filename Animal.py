# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:53:48 2018

@author: Anton

I try to fiddle around with some concepts for a game. This game will be based
on genetics and mutations and a lot of randomness.
"""

import random

animalList=["bat", "monkey", "dog", "fly", "bee", "spider", "snake"]
traitList=["strong", "weak", "intelligent", "lethargic", "fertile", "wasting"]

class Animal():
    def __init__(self,animal):
        self.animalType=animal
        traitList2=traitList
        traitIndex=random.randint(0,len(traitList2)-1)
        self.activeTrait=traitList2[traitIndex]
        traitList2.pop(traitIndex)
        traitIndex2=random.randint(0,len(traitList2)-1)
        self.passiveTrait=traitList2[traitIndex2]
        
    def __repr__(self):
        '''Returns representation of the object'''
        return("{}('{}')".format(self.__class__.__name__, self.animalType))
        
    def __str__(self):
        '''Returns representation of the object'''
        return "Active trait: {}. Passive trait: {}.".format(self.activeTrait, self.passiveTrait) 
    
    def setAnimalType(self,var):
        self.animalType=var
        
    def setTraits(self):
        self.activeTrait=var    
        
    def getAnimalType(self):
        return(self.animalType)
        
    def mate(self,other):
        if self.getAnimalType()!=other.getAnimalType():
            print("They are not the same animal!")
            return
        child=Animal(self.getAnimalType())
        
        if self.activeTrait==other.activeTrait: # 66% to inherit
            roll=random.randint(1,3)
            if roll==1 or roll==2:
                child.activeTrait==self.activeTrait
                # if 3 -> keep the randomly generated activeTrait 
        else:
            roll=random.randint(1,3)
            if roll==1:
                child.activeTrait==self.activeTrait # 33% to inherit
            elif roll==2:
                child.activeTrait==other.activeTrait # 33% to inherit
            # if 3 -> keep the randomly generated activeTrait
        
        if self.passiveTrait==other.passiveTrait: # 66% to inherit
            roll=random.randint(1,3)
            if roll==1 or roll==2:
                child.passiveTrait==self.passiveTrait
                # if 3 -> keep the randomly generated activeTrait 
        else:
            roll=random.randint(1,3)
            if roll==1:
                child.passiveTrait==self.passiveTrait # 33% to inherit
            elif roll==2:
                child.passiveTrait==other.passiveTrait # 33% to inherit
            # if 3 -> keep the randomly generated activeTrait
        return child
                
        
   
        
 
animal1=Animal("bat")
#animal1.setAnimalType("bat")
animal2=Animal("bat")
#animal2.setAnimalType("bat")
print(animal1)
print(animal2)
print(animal1.mate(animal2))



