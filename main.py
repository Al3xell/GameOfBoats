#!/usr/bin/python -u
# -*- coding: utf-8 -*-

'''
Class that define the player
'''

import sys
import os
import termios
import tty
import select
import time

from player import Player
from background import Background
from island import Island

def main():
  timestep = 0.001
  
  old_settings = termios.tcgetattr(sys.stdin.fileno())
  tty.setcbreak(sys.stdin.fileno())#Keyboard interaction
  sys.stdout.write("\033c")#clear terminal
  sys.stdout.write("\033[?25l")#remove cursor 
  
  player = Player('Alex')
  background = Background(player)
  
  islandShapes = Island.init_shape('Maps/Island_shapes.txt')
  islands=[]
  for shape in range(0,len(islandShapes)):
    x,y = background.putIsland(islandShapes[shape])
    islands.append(Island(x=x, y=y, shape=islandShapes[shape]))
  
  while True :
    if isData(): #If a key has been pressed
      key = sys.stdin.read(1) #Reading key
      if key == '\x1b': #Quit if ESC
        quitGame(old_settings)
      elif key == 'z' or 'q' or 's' or 'd':
        player.changeDrct(key)
        
    background.move(player)
    background.player = player
    background.show()
    player.show()
    time.sleep(timestep)
    
    
def isData():
  #return True if a key as been pressed
  return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])  

def quitGame(old_settings):
    
    sys.stdout.write("\033c")#clear terminal
    sys.stdout.write("\033[37m")#color white
    sys.stdout.write("\033[40m")#color background black
    sys.stdout.write("\033[?25h")#Cursor restored
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)#apply old settings
    sys.exit()#quit
    
if __name__ == '__main__':
    main()    
      