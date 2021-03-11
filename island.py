#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Class Island
'''
 
class Island(object):
#-----Class Variables-----#

#-----Constructor-----#
  def __init__(self,shape, x=1, y=1, name="Unknown"):
    self.__name = name
    self.__shape = shape
    self.__x = x
    self.__y = y
    
    
#-----Getter-----#
  @property
  def name(self):
    return self.__name

  @property
  def shape(self):
    return self.__shape

  @property
  def x(self):
    return self.__x

  @property
  def y(self):
    return self.__y
#-----Setter-----#
  @name.setter
  def name(self,newName):
    self.__name = newName
    
  @shape.setter
  def shape(self,newShape):
    self.__shape = newShape
  
  @x.setter
  def x(self,newX):
    self.__x = newX
    
  @y.setter
  def y(self,newY):
    self.__y = newY  
#-----Methods-----#
  @staticmethod  
  def init_shape(filename):
    
    #splitting all shapes
    shapeisland = open(filename,'r').read().split('\nshape\n')
    
    shape = []
    #splitting all lines of each shapes
    for ls in shapeisland :
        shape.append(ls.split('\n'))

    #seperate every char
    for i in range(0,len(shape)):
        shape[i] = list(shape[i])
        for j in range(0,len(shape[i])):
            shape[i][j] = list(shape[i][j])
        
    return shape

if __name__ == '__main__':
    island = Island()
    print(island.shape[0])
    