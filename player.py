#!/usr/bin/python -u
# -*- coding: utf-8 -*-

'''
Class that define the player
'''

import sys
import os
 
class Player(object):
#-----Class Variables-----#
 
#-----Constructor-----#
  def __init__(self, name, x=1, y=1, pv=20, gold=50, drct=4, shapes=[]):
      
    self.__name = name
    self.__x = x
    self.__y = y
    self.__pv = pv
    self.__gold = gold
    self.__drct = drct
    self.__shapes = shapes
    
    self.init_shapes('Shapes/bateau.txt')
    
#-----Getter-----#

  @property
  def name(self):
    return self.__name

  @property
  def x(self):
    return self.__x

  @property
  def y(self):
    return self.__y

  @property
  def pv(self):
    return self.__pv

  @property
  def gold(self):
    return self.__gold

  @property
  def drct(self):
    return self.__drct

  @property
  def shapes(self):
    return self.__shapes[:]

#-----Setter-----#

  @name.setter
  def name(self,newName):
    self.__name = newName
    
  @x.setter
  def x(self,newX):
    self.__x = newX
    
  @y.setter
  def y(self,newY):
    self.__y = newY
    
  @pv.setter
  def pv(self,newPv):
    self.__pv = newPv
    
  @gold.setter
  def gold(self,newGold):
    self.__gold = newGold
    
  @drct.setter
  def drct(self,newDrct):
    self.__drct = newDrct
    
  @shapes.setter
  def shapes(self, newShapes):
    assert type(newShapes) is list
    self.__shapes = newShapes
    
#-----Methods-----#
  
  def init_shapes(self,filename):
      file = open(filename, 'r')
      chains = file.read()
      fin_shapes = chains.split('\nshape\n')
      
      for shapes in range(len(fin_shapes)) :
        fin_shapes[shapes] = fin_shapes[shapes].split('\n')
        for lines in range(len(fin_shapes[shapes])):
          fin_shapes[shapes][lines] = list(fin_shapes[shapes][lines])
        
      self.shapes = fin_shapes
              
  def show(self):
    
    x_view = int(os.get_terminal_size().columns/2)-int(len(self.shapes[self.drct])/2)
    y_view = int(os.get_terminal_size().lines/2)
    for y in range(len(self.shapes[self.drct])):
      for x in range(len(self.shapes[self.drct][y])):
        sys.stdout.write(f"\033[{y_view+y};{x_view+x}H")
        sys.stdout.write(self.shapes[self.drct][y][x])
        sys.stdout.flush()
        
  #Background will move the player using changeDrct()
  
  def changeDrct(self,inputKey):
    if inputKey == 'q':
      self.drct = 0
    elif inputKey == 'd':
      self.drct = 1
    elif inputKey == 'z':
      self.drct = 2
    elif inputKey == 's':
      self.drct = 3
    elif inputKey == 'r':
      self.drct = 4
    
              
if __name__ == '__main__':
  player = Player('Alex')
  player.init_shapes('Shapes/bateau.txt')
  player.show()