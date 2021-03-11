#!/usr/bin/python -u
# -*- coding: utf-8 -*-
 
'''
Class that define the background
'''

import os
import sys
import random

from player import Player
 
class Background(object):
#-----Class Variables-----#

#-----Constructor-----#
  def __init__(self, player, maps = [], filename = 'Maps/maps.txt'):
    self.__maps = maps
    self.__player = player
    self.init_maps(filename)
    
#-----Getter-----#
  @property
  def maps(self):
    return self.__maps[:]
  
  @property
  def player(self):
    return self.__player

#-----Setter-----#
  @maps.setter
  def maps(self,newMaps):
    self.__maps = newMaps
  @player.setter
  def player(self,newPlayer):
    self.__player = newPlayer
    
#-----Methods-----#
  def init_maps(self, filename):
    file = open(filename, 'r')
    chains = file.read()
    fin_maps = chains.split('\n')
    for lines in range(len(fin_maps)):
      fin_maps[lines] = list(fin_maps[lines])
    self.maps = fin_maps
    
  def show(self):
    x_term = os.get_terminal_size().columns
    y_term = os.get_terminal_size().lines
    
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[44m")

    for y in range(0,y_term):
      for x in range(0,x_term):
        x_view = self.player.x - int(x_term/2)+x+1
        y_view = self.player.y - int(y_term/2)+y
        sys.stdout.write(f"\033[{y};{x}H")
        if int(y_term/2) <= y <= int(y_term/2+len(self.player.shapes[self.player.drct])-1) and int(x_term/2)-int(len(self.player.shapes[self.player.drct][0])/2-2) <= x <= int(x_term/2) + int(len(self.player.shapes[self.player.drct][0])/2+2):
          pass
        elif x_view < 0 or y_view < 0 or y_view >= len(self.maps) or x_view >= len(self.maps[y_view]):
          sys.stdout.write(" ")
        else:
          sys.stdout.write(self.maps[y_view][x_view])
        sys.stdout.flush()
          
  def move(self,entity):
    if entity.drct == 0:
      if self.maps[entity.y][entity.x-1] == ' ':
        entity.x-=1
      else:
        entity.drct = 4
    elif entity.drct == 1:
      if self.maps[entity.y][entity.x+len(entity.shapes[entity.drct][0])+1] == ' ':
        entity.x+=1
      else:
        entity.drct = 4
    elif entity.drct == 2:
      if self.maps[entity.y-1][entity.x] == ' ':
        entity.y-=1
      else:
        entity.drct = 4
    elif entity.drct == 3:
      if self.maps[entity.y+len(entity.shapes[entity.drct])][entity.x] == ' ':
        entity.y+=1
      else:
        entity.drct = 4
    elif entity.drct == 4:
      pass
  
  def putIsland(self,island):
    find_position = True

    while find_position:
      x = random.randint(1,len(self.maps[0]))
      y = random.randint(1,len(self.maps))
      possible = True
      
      while possible:
        for y_elem in range(0,len(island)):
          for x_elem in range(0,len(island[y_elem])):
            try:
              if self.maps[y+y_elem][x+x_elem] != ' ':
                possible = False
            except :
              possible = False
        try:
          for y_elem in range(0,len(island)):
            for x_elem in range(0,len(island[y_elem])):
              self.maps[y+y_elem][x+x_elem] = island[y_elem][x_elem]
          return x, y
        except :
          possible = False

  
if __name__ == '__main__':
  player = Player('Alex')
  background = Background(player)
  background.show()

  