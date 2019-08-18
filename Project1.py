import numpy as np
import random
import heapq
import math
import matplotlib.pyplot as plt
import time
import xlwt
from xlwt import Workbook
#random cell choosing class
class random_cell:
  def __init__(self, begin,end):
      self.begin= begin
      self.end = end

  def row_column(self):
      for p in range(1):

          x = random.randint(self.begin,self.end)
          y = random.randint(self.begin,self.end)
          return x,y
  def start_end(self):
      for t in range(1):

          x = random.randint(self.begin,self.end)
          y = random.randint(self.begin,self.end)
          return x,y

class cell_blocked:

  def __init__(self, data = None, next_cell=None):
      self.data = data
      self.next_cell = next_cell

  def get_data(self):
      return self.data

  def get_next(self):
      return self.next_cell

  def set_next(self,new_next):
      self.next_cell = new_next

class blocked_linked_list:

  def __init__(self):
      self.head=None

  def insert(self,data):
      new_node = cell_blocked(data)
      new_node.set_next(self.head)
      self.head = new_node

  def print_list(self):
      done = self.head
      while done is not None:
          print(done.data)

          done = done.next_cell
  #searching if the node exists
  def search(self ,data1):
      look = self.head
      while look is not None:
          if look.data == data1:
              return True
          look = look.next_cell



class linked_list:

  def __init__(self):
      self.head=None


  def insert(self,state,cost,total_cost,h,f_values,x,y):
      new_node = Node(state,cost,total_cost,h,f_values,x,y)
      new_node.next= self.head
      self.head = new_node

  def print_list(self):
      done = self.head
      while done is not None:
           print(done.state, done.cost,done.total_cost, done.f_values, '('+str(done.x)+ ','+str(done.y)+')')
           done = done.next

  def print_path(self):
      done = self.head
      while done is not None:
          print('(' + str(done.x) + ',' + str(done.y) + ')')
          done = done.next

  def getCount(self):
      temp = self.head  # Initialise temp
      count = 0  # Initialise count

      # Loop while end of linked list is not reached
      while (temp):
          count += 1
          temp = temp.next
      return count

  def delete_node(self,cost):
      temp = self.head
      # deletes the head node
      if(temp is not None):
          if(temp.cost == cost):
              self.head = temp.next_cell
              temp = None
              return
      while temp is not None :
          if temp.cost == cost:
              break
          prev = temp
          temp = temp.next_cell
      #checking if the node is present
      if (temp == None):
          return
      #deletes a node that is not the head node
      prev.next_cell = temp.next_cell
      temp = None

  def search(self ,data1,data2):
      look = self.head
      while look is not None:
          if look.x == data1 and look.y == data2:
              return True
          look = look.next



class cell_checker:
  def __init__(self):
      None
  def isBlocked(self,location):
       if(location == b'B'):
           return math.inf
       if (location == b'S'):
           return 0
       else:
           return 1
  def isGoal(self,x,y,goalx,goaly):
      if(x==goalx and y==goaly):
          return True
      else:
          return False

  def h_values(self,x,y,goalx,goaly):
      return abs(x - goalx) + abs(y - goaly)

  def is_valid(self,row,column,max):
      if row>=0 and column >= 0 and row <=max and column <=max:
              return True
class Node:
  def __init__(self, state, cost, total_cost,h, f_values, x, y):
      self.state = state
      self.cost = cost
      self.total_cost = total_cost
      self.f_values = f_values
      self.x = x
      self.y = y
      self.h=h
      self.next = None

  def getf(self):
      x = self.f_values
      return int(x)

class PriorityQueue:
  def __init__(self):
      self.front = self.rear = None


  def isEmpty(self):
      return self.front == None

  def enqueue(self, state, cost, total_cost,h, f_values, x, y):
      newNode = Node(state, cost, total_cost,h, f_values, x, y,)
      if not self.rear:
          self.front = self.rear = newNode
          return
      if self.front.f_values > newNode.f_values:
          newNode.next = self.front
          self.front = newNode
          return
      if self.front.f_values == newNode.f_values:
          if self.front.total_cost < newNode.total_cost:
              newNode.next = self.front
              self.front = newNode
          return
      previous = None
      current = self.front
      while (current and newNode.f_values > current.f_values):
          previous = current
          current = current.next

      if current:
          previous.next = newNode
          newNode.next = current
      else:
          self.rear.next = newNode
          self.rear = newNode


  # Removes and returns the next item from the queue, which is the
  # item with the lowest priority.
  def dequeue(self):
      if self.isEmpty():
          print('Queue is empty')

          return
      temp = self.front
      self.front = self.front.next
      if self.front == None:
          self.rear = None
      return temp.x,temp.y,temp.f_values,temp.total_cost,temp.h

  def print_list(self):
      done = self.front
      while done is not None:
          print(done.state, done.cost, done.total_cost, done.f_values, done.x, done.y)
          done = done.next

  #used to determin tie breaking
  def search_f(self,x,y):
      look = self.front
      while look is not None:
          if look.x ==x and look.y==y:
              return look.f_values
          look = look.next


  def search_f_values(self,f):
      look = self.front

      while look is not None:
          if look.f_values == f:
              return True
          look = look.next

  def search_g_f(self,f):
      look = self.front
      while look is not None:
          if look.f_values ==f:
              return look.total_cost
          look = look.next

  def search_g(self,x,y):
      look = self.front
      while look is not None:
          if look.x ==x and look.y==y:
              return look.total_cost
          look = look.next

  def search_B(self, x, y):
      look = self.front
      while look is not None:
          if look.x == x and look.y == y:
              return look.x,look.y
          look = look.next

  def search(self,x,y):
      look = self.front
      while look is not None:
          if look.x ==x and look.y==y:
              return True
          look = look.next

class f_astar:
  open_list = PriorityQueue()
  closed_list = linked_list()
  checker = cell_checker()
  startx =0
  starty =0
  unable =0

  def __init__(self,grid,beginx,beginy,goalx,goaly,xb,yb):
      self.grid = grid
      self.beginx = beginx
      self.beginy= beginy
      self.goalx = goalx
      self.goaly = goaly
      self.xb = xb
      self.yb=yb




  def f_searching(self):

      fig = plt.figure(figsize=(10, 10))
      plt.scatter(self.beginx, self.beginy, marker='o', color='m')
      plt.scatter(self.goalx, self.goaly, marker='o', color='b')
      plt.scatter(self.xb, self.yb, marker='s', color='r')
      open_list = PriorityQueue()
      #handle tie breaking according to g values

      closed_list = linked_list()
      checker = cell_checker()

      unable = 0
      f =0
      h =0
      h = checker.h_values(beginx,beginy, self.goalx, self.goaly)
      print('Distance from start to finish '+ str(h))
      open_list.enqueue(self.grid.item(self.beginy, self.beginx), checker.isBlocked(self.grid.item(self.beginy, self.beginx)), 0, h,h, self.beginx, self.beginy)
      ndone = 5
      while open_list is not None:

          startx, starty, f, g, h = open_list.dequeue()

          closed_list.insert(self.grid.item(starty, startx),checker.isBlocked(self.grid.item(starty, startx)), g, h, f, startx, starty)
          plt.scatter(startx, starty, marker='>', color='g')
          plt.pause(0.01)


          #prevents expanding nodes that already have been expanded


          # sets the cell to  M when agent has moved
          #checking Up
          if checker.is_valid(startx, starty - 1, 100) == True:

              if checker.isGoal(startx, starty - 1, self.goalx, self.goaly) == True:
                  print('The cell destination has been found')
                  g = checker.isBlocked(self.grid[starty - 1][startx]) + 1
                  h = checker.h_values(startx, starty - 1, self.goalx, self.goaly)
                  # print('Distance from up to goal is ' + str(h))
                  f = g + h
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g, h,f, self.goalx,self.goaly)
                  break
              if closed_list.search(startx, starty - 1) != True and self.grid[starty-1][startx] == b'O' :

                  #g = checker.distance_start(startx, starty-1, startx, starty)
                  g = checker.isBlocked(self.grid[starty - 1][startx]) + g
                  h = checker.h_values(startx, starty - 1, self.goalx, self.goaly)
                  # print('Distance from up to goal is ' + str(h))
                  f = g + h

                  if open_list.search(startx, starty - 1) != True or open_list.isEmpty() :
                      # print('Inserted into the UP')
                      # print(f)
                          open_list.enqueue(self.grid.item(starty - 1, startx), checker.isBlocked(self.grid.item(starty - 1, startx)), g,h,f, startx, starty - 1)



                  if open_list.search(startx, starty - 1) == True:
                          g2 = open_list.search_g(startx,starty-1)
                          if g > g2:
                              open_list.enqueue(self.grid.item(starty - 1, startx), checker.isBlocked(self.grid.item(starty - 1, startx)), g, h, f, startx, starty - 1)

              if self.grid[starty - 1][startx] == b'B':
                  g =0



              # checking the down
          if checker.is_valid(startx, starty + 1, 100) == True:

              if checker.isGoal(startx, starty + 1, goalx, goaly) == True:
                  print('The cell destination has been found')
                  g = checker.isBlocked(self.grid[starty + 1][startx]) + 1
                  h = checker.h_values(startx, starty + 1, self.goalx, self.goaly)
                  # print('Distance from down to goal is ' + str(h))
                  f = g + h
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g, h,f, self.goalx,self.goaly)
                  break

              if closed_list.search(startx, starty + 1) != True and self.grid[starty+1][startx] == b'O' :


                  #g = checker.distance_start(startx,starty+1,startx,starty)
                  g = checker.isBlocked(self.grid[starty + 1][startx]) + g
                  h = checker.h_values(startx, starty + 1, self.goalx, self.goaly)
                  # print('Distance from down to goal is ' + str(h))
                  f = g + h

                  # handling the tie breaaking and inserts based off of smaller f values
                  if open_list.search(startx, starty + 1) != True or open_list.isEmpty() :


                      open_list.enqueue(self.grid.item(starty + 1, startx), checker.isBlocked(self.grid.item(starty + 1, startx)), g,h,f, startx, starty + 1)

                      if open_list.search(startx, starty + 1) == True:
                                  g2 = open_list.search_g(startx,starty+1)
                                  if g > g2:
                                     open_list.enqueue(self.grid.item(starty + 1, startx),checker.isBlocked(self.grid.item(starty + 1, startx)), g, h,f, startx, starty + 1)
              if self.grid[starty + 1][startx] == b'B':
                  g = 0

              # checking the right
          if checker.is_valid(startx + 1, starty, 100) == True:

              if checker.isGoal(startx + 1, starty, goalx, goaly) == True:
                  print('The cell destination has been found')
                  g = checker.isBlocked(self.grid[starty][startx + 1]) + 1

                  h = checker.h_values(startx + 1, starty, self.goalx, self.goaly)
                  f = g + h
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g,h, f, self.goalx, self.goaly)
                  break

              if closed_list.search(startx + 1, starty) != True and self.grid[starty][startx+1] == b'O' :

                   g = checker.isBlocked(self.grid[starty][startx + 1]) + g

                   h = checker.h_values(startx + 1, starty, self.goalx, self.goaly)
                   f = g + h



                   if open_list.search(startx + 1, starty) != True or open_list.isEmpty():


                              open_list.enqueue(self.grid.item(starty, startx + 1), checker.isBlocked(self.grid.item(starty, startx + 1)), g,h,f, startx + 1, starty)


                   if open_list.search(startx+1, starty) == True:
                          g2 = open_list.search_g(startx+1,starty)
                          if g > g2:
                            open_list.enqueue(self.grid.item(starty, startx+1),checker.isBlocked(self.grid.item(starty + 1, startx)), g, h, f, startx+1,starty)
              if self.grid[starty][startx+1] == b'B':

                  g = 0
               #checking the left
          if checker.is_valid(startx - 1, starty, 100) == True:

              if checker.isGoal(startx - 1, starty, goalx, goaly) == True:
                  print('The cell destination has been found')
                  g = checker.isBlocked(self.grid[starty][startx - 1]) + 1

                  h = checker.h_values(startx - 1, starty, self.goalx, self.goaly)

                  f = g + h
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g,h, f, self.goalx,self.goaly)
                  break

              if closed_list.search(startx - 1, starty) != True and self.grid[starty][startx-1] == b'O' :


                  g = checker.isBlocked(self.grid[starty][startx - 1]) + g

                  h = checker.h_values(startx - 1, starty, self.goalx, self.goaly)

                  f = g + h



                  # handling the tie breaaking
                  if open_list.search(startx - 1, starty) != True or open_list.isEmpty():

                              open_list.enqueue(self.grid.item(starty, startx - 1), checker.isBlocked(self.grid.item(starty, startx - 1)), g,h,f, startx - 1, starty)


                  if open_list.search(startx-1, starty) == True:
                      g2 = open_list.search_g(startx-1,starty)
                      if g > g2:
                          open_list.enqueue(self.grid.item(starty, startx-1),checker.isBlocked(self.grid.item(starty, startx-1)), g, h, f, startx-1,starty)
              if self.grid[starty][startx-1] == b'B':
                  g = 0

          if (open_list.isEmpty()):
              print('Goal is unable to be found')

              open_list = None

      plt.title('Forward A star Greater G value')
      plt.show()


  def f_searching_b(self):

      fig = plt.figure(figsize=(10, 10))
      plt.scatter(self.beginx, self.beginy, marker='o', color='m')
      plt.scatter(self.goalx, self.goaly, marker='o', color='b')
      plt.scatter(self.xb, self.yb, marker='s', color='r')
      open_list = PriorityQueue()
      #handle tie breaking according to g values

      closed_list = linked_list()
      checker = cell_checker()

      unable = 0
      f =0
      h =0
      h = checker.h_values(beginx,beginy, self.goalx, self.goaly)
      print('Distance from start to finish '+ str(h))
      open_list.enqueue(self.grid.item(self.beginy, self.beginx), checker.isBlocked(self.grid.item(self.beginy, self.beginx)), 0, h,h, self.beginx, self.beginy)
      ndone = 5
      while open_list is not None:

          startx, starty, f, g, h = open_list.dequeue()

          closed_list.insert(self.grid.item(starty, startx),checker.isBlocked(self.grid.item(starty, startx)), g, h, f, startx, starty)
          plt.scatter(startx, starty, marker='>', color='g')
          plt.pause(0.01)





          # sets the cell to  M when agent has moved
          #checking Up
          if checker.is_valid(startx, starty - 1, 100) == True:

              if checker.isGoal(startx, starty - 1, self.goalx, self.goaly) == True:
                  print('The cell destination has been found')
                  g = checker.isBlocked(self.grid[starty - 1][startx]) + 1
                  h = checker.h_values(startx, starty - 1, self.goalx, self.goaly)

                  f = g + h
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g, h,f, self.goalx,self.goaly)
                  break
              if closed_list.search(startx, starty - 1) != True and self.grid[starty-1][startx] == b'O' :

                  g = checker.isBlocked(self.grid[starty - 1][startx]) + g
                  h = checker.h_values(startx, starty - 1, self.goalx, self.goaly)

                  f = g + h

                  if open_list.search(startx, starty - 1) != True or open_list.isEmpty() :

                          open_list.enqueue(self.grid.item(starty - 1, startx), checker.isBlocked(self.grid.item(starty - 1, startx)), g,h,f, startx, starty - 1)



                  if open_list.search(startx, starty - 1) == True:
                          g2 = open_list.search_g(startx,starty-1)
                          if g < g2:
                              open_list.enqueue(self.grid.item(starty - 1, startx), checker.isBlocked(self.grid.item(starty - 1, startx)), g, h, f, startx, starty - 1)
              if self.grid[starty - 1][startx] == b'B':

                  g =0



              # checking the down
          if checker.is_valid(startx, starty + 1, 100) == True:

              if checker.isGoal(startx, starty + 1, goalx, goaly) == True:
                  print('The cell destination has been found')
                  g = checker.isBlocked(self.grid[starty + 1][startx]) + 1
                  h = checker.h_values(startx, starty + 1, self.goalx, self.goaly)

                  f = g + h
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g, h,f, self.goalx,self.goaly)
                  break

              if closed_list.search(startx, starty + 1) != True and self.grid[starty+1][startx] == b'O' :


                  g = checker.isBlocked(self.grid[starty + 1][startx]) + g
                  h = checker.h_values(startx, starty + 1, self.goalx, self.goaly)

                  f = g + h

                  # handling the tie breaaking and inserts based off of smaller f values
                  if open_list.search(startx, starty + 1) != True or open_list.isEmpty() :


                      open_list.enqueue(self.grid.item(starty + 1, startx), checker.isBlocked(self.grid.item(starty + 1, startx)), g,h,f, startx, starty + 1)

                      if open_list.search(startx, starty + 1) == True:
                                  g2 = open_list.search_g(startx,starty+1)
                                  if g < g2:
                                     open_list.enqueue(self.grid.item(starty + 1, startx),checker.isBlocked(self.grid.item(starty + 1, startx)), g, h,f, startx, starty + 1)
              if self.grid[starty + 1][startx] == b'B':
                  g = 0

              # checking the right
          if checker.is_valid(startx + 1, starty, 100) == True:

              if checker.isGoal(startx + 1, starty, goalx, goaly) == True:
                  print('The cell destination has been found')
                  g = checker.isBlocked(self.grid[starty][startx + 1]) + 1

                  h = checker.h_values(startx + 1, starty, self.goalx, self.goaly)
                  f = g + h
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g,h, f, self.goalx, self.goaly)
                  break

              if closed_list.search(startx + 1, starty) != True and self.grid[starty][startx+1] == b'O' :

                   g = checker.isBlocked(self.grid[starty][startx + 1]) + g

                   h = checker.h_values(startx + 1, starty, self.goalx, self.goaly)
                   f = g + h


                  # handling the tie breaaking
                   if open_list.search(startx + 1, starty) != True or open_list.isEmpty():


                              open_list.enqueue(self.grid.item(starty, startx + 1), checker.isBlocked(self.grid.item(starty, startx + 1)), g,h,f, startx + 1, starty)


                   if open_list.search(startx+1, starty) == True:
                          g2 = open_list.search_g(startx+1,starty)
                          if g < g2:
                            open_list.enqueue(self.grid.item(starty, startx+1),checker.isBlocked(self.grid.item(starty + 1, startx)), g, h, f, startx+1,starty)
              if self.grid[starty][startx+1] == b'B':

                  g = 0
               #checking the left
          if checker.is_valid(startx - 1, starty, 100) == True:

              if checker.isGoal(startx - 1, starty, goalx, goaly) == True:
                  print('The cell destination has been found')
                  g = checker.isBlocked(self.grid[starty][startx - 1]) + 1

                  h = checker.h_values(startx - 1, starty, self.goalx, self.goaly)

                  f = g + h
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g,h, f, self.goalx,self.goaly)
                  break

              if closed_list.search(startx - 1, starty) != True and self.grid[starty][startx-1] == b'O' :

                  g = checker.isBlocked(self.grid[starty][startx - 1]) + g
                  h = checker.h_values(startx - 1, starty, self.goalx, self.goaly)
                  f = g + h


                  # handling the tie breaaking
                  if open_list.search(startx - 1, starty) != True or open_list.isEmpty():

                              open_list.enqueue(self.grid.item(starty, startx - 1), checker.isBlocked(self.grid.item(starty, startx - 1)), g,h,f, startx - 1, starty)


                  if open_list.search(startx-1, starty) == True:
                      g2 = open_list.search_g(startx-1,starty)
                      if g < g2:
                          open_list.enqueue(self.grid.item(starty, startx-1),checker.isBlocked(self.grid.item(starty, startx-1)), g, h, f, startx-1,starty)
              if self.grid[starty][startx-1] == b'B':
                  g = 0

          if (open_list.isEmpty()):
              print('Goal is unable to be found')

              open_list = None


      plt.title('Forward A star Lesser G value')
      plt.show()

  #Reverse Searching here
  def b_searching(self):


      fig = plt.figure(figsize=(10, 10))
      plt.scatter(self.beginx, self.beginy, marker='o', color='m')
      plt.scatter(self.goalx, self.goaly, marker='o', color='b')
      plt.scatter(self.xb, self.yb, marker='s', color='r')
      open_list = PriorityQueue()
      closed_list = linked_list()
      checker = cell_checker()
      unable = 0
      f2 =0
      g = 0
      h =0
      f=0
      g = checker.h_values(beginx, beginy, self.goalx, self.goaly)
      open_list.enqueue(self.grid.item(self.beginy, self.beginx), checker.isBlocked(self.grid.item(self.beginy, self.beginx)), g,0,f, self.beginx, self.beginy)

      while open_list is not None:
          startx, starty, f, g,h = open_list.dequeue()


          closed_list.insert(self.grid.item(starty, startx), checker.isBlocked(self.grid.item(starty, startx)), g,h, f, startx, starty)
          plt.scatter(startx, starty, marker='>', color='g')
          plt.pause(0.01)
          h =0


          #checking Up
          if checker.is_valid(startx, starty - 1, 100) == True:

              if checker.isGoal(startx, starty - 1, self.goalx, self.goaly) == True:
                  print('The cell destination has been found')
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g, h,f, self.goalx,self.goaly)

                  break
              if closed_list.search(startx, starty - 1) != True and c[starty - 1][startx] == b'O':

                  h = checker.isBlocked(self.grid[starty - 1][startx]) + h
                  g = checker.h_values(startx, starty - 1, self.goalx, self.goaly)
                  f = g + h

                  # handling the tie breaaking
                  if open_list.search(startx, starty - 1) != True or open_list.isEmpty() :

                      open_list.enqueue(self.grid.item(starty - 1, startx), checker.isBlocked(self.grid.item(starty - 1, startx)), g,h,f, startx, starty - 1)

                  if open_list.search(startx, starty - 1) == True:
                      g2 = open_list.search_g(startx, starty - 1)
                      if g > g2:
                          open_list.enqueue(self.grid.item(starty - 1, startx),checker.isBlocked(self.grid.item(starty - 1, startx)), g, h, f, startx,starty - 1)

                  if self.grid[starty - 1][startx] == b'B':
                      h = 0

              # checking the down
          if checker.is_valid(startx, starty + 1, 100) == True:

              if checker.isGoal(startx, starty + 1, goalx, goaly) == True:
                  print('The cell destination has been found')
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g, h,f, self.goalx,self.goaly)

                  break

              if closed_list.search(startx, starty + 1) != True and c[starty + 1][startx] == b'O':



                  h = checker.isBlocked(self.grid[starty + 1][startx]) + h
                  g = checker.h_values(startx, starty + 1, self.goalx, self.goaly)

                  f = g + h

                  if open_list.search(startx, starty + 1) != True or open_list.isEmpty() :

                      open_list.enqueue(self.grid.item(starty + 1, startx), checker.isBlocked(self.grid.item(starty + 1, startx)), g,h,f, startx, starty + 1)

                  if open_list.search(startx, starty + 1) == True:
                      g2 = open_list.search_g(startx, starty + 1)
                      if g > g2:
                          open_list.enqueue(self.grid.item(starty + 1, startx),checker.isBlocked(self.grid.item(starty + 1, startx)), g, h, f, startx,starty + 1)
                  if self.grid[starty + 1][startx] == b'B':
                      h = 0
              # checking the right
          if checker.is_valid(startx + 1, starty, 100) == True:

              if checker.isGoal(startx + 1, starty, goalx, goaly) == True:
                  print('The cell destination has been found')
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g,h, f, self.goalx, self.goaly)

                  break

              if closed_list.search(startx + 1, starty) != True and c[starty][startx + 1] == b'O':

                   h = checker.isBlocked(self.grid[starty][startx + 1]) + h

                   g = checker.h_values(startx + 1, starty, self.goalx, self.goaly)
                   f = g + h


                  # handling the tie breaaking
                   if open_list.search(startx + 1, starty) != True or open_list.isEmpty():
                      #
                      open_list.enqueue(self.grid.item(starty, startx + 1), checker.isBlocked(self.grid.item(starty, startx + 1)), g,h,f, startx + 1, starty)

                   if open_list.search(startx + 1, starty) == True:
                      g2 = open_list.search_g(startx + 1, starty)
                      if g > g2:
                          open_list.enqueue(self.grid.item(starty, startx + 1),
                                            checker.isBlocked(self.grid.item(starty + 1, startx)), g, h, f, startx + 1,
                                            starty)
                   if self.grid[starty][startx + 1] == b'B':
                       h = 0
              # checking the left
          if checker.is_valid(startx - 1, starty, 100) == True:

              if checker.isGoal(startx - 1, starty, goalx, goaly) == True:
                  print('The cell destination has been found')
                  closed_list.insert(self.grid.item(self.goaly, self.goalx), checker.isBlocked(self.grid.item(starty, startx)), g,h, f, self.goalx,self.goaly)
                  break

              if closed_list.search(startx - 1, starty) != True and c[starty][startx - 1] == b'O':

                  h = checker.isBlocked(self.grid[starty][startx - 1]) + h
                  g = checker.h_values(startx - 1, starty, self.goalx, self.goaly)
                  f = g + h

                  # handling the tie breaaking
                  if open_list.search(startx - 1, starty) != True or open_list.isEmpty():
                      open_list.enqueue(self.grid.item(starty, startx - 1), checker.isBlocked(self.grid.item(starty, startx - 1)), g,h,f, startx - 1, starty)

                  if open_list.search(startx-1, starty ) == True:
                      g2 = open_list.search_g(startx-1, starty)
                      if g > g2:
                          open_list.enqueue(self.grid.item(starty, startx-1),checker.isBlocked(self.grid.item(starty, startx-1)), g, h, f, startx-1,starty)
                  if self.grid[starty][startx - 1] == b'B':
                      h = 0



          if (open_list.isEmpty()):
              print('Goal is unable to be found')
              #plt.title('Forward A star/ Goal Unable to be Found')
              open_list = None
              unable = 1





      plt.title('Reverse A star')
      plt.show()

blocking_list = blocked_linked_list()
cells= random_cell(0,100)
c = np.chararray([0])
c.resize((101,101))
c.fill('O')
checker=cell_checker()
startx =0
starty=0
x =0
y =0
f =0
xb =[]
yb=[]
#this for loop randomly sets a cell to 1 signifying that the cell is blocking
done = False
done2 = False
p =0
#This while loop is preventing tie breaking when selecting a cell to set as blocking
while done2 is not True:
    r, col = cells.row_column()
    # settling a tie in coordinates

    if blocking_list.search(str(r) + ' ' + str(col)) == True:

        None
    else:
        blocking_list.insert(str(r) + ' ' + str(col))
        xb.append(r)
        yb.append(col)
        c.itemset(col, r, 'B')
        p += 1

    # left is column right is row
    if p == 3060:
        done2 = True
        break

#this while loop handles if the start and end locations are the same or if they are locations marked as blocked
while done is not True:
  startx, starty = cells.start_end()
  goalx, goaly = cells.start_end()

  if blocking_list.search(str(startx) + ' ' + str(starty)) != True and blocking_list.search(str(goalx) + ' ' + str(goaly)) != True and  startx != goalx and starty != goaly:

      c.itemset(starty, startx, 'S')
      c.itemset(goaly, goalx, 'G')
      done = True


print('Start: '+ str(startx),str(starty))
print('Goal: '+ str(goalx), str(goaly))
beginx = startx
beginy = starty
F_star = f_astar(c,beginx,beginy,goalx,goaly,xb,yb)
print('Enter 1. for Forward A Star Settling Ties with greater G value')
print('Enter 2. for Forward A Star Settling Ties with lesser G value')
print('Enter 3. for Reverse A Star')
start =0
end = 0
fin = False
while fin is not True:
    start = 0
    end = 0
    g = int(input('Please enter in an option:'))
    print('Start: ' + str(startx), str(starty))
    print('Goal: ' + str(goalx), str(goaly))
    if g == 1:
        start = time.time()
        cost = F_star.f_searching()
        print(cost)
        end = time.time()
    elif g ==2:
        start = time.time()
        F_star.f_searching_b()
        end = time.time()

    elif g == 3:
        start = time.time()
        F_star.b_searching()
        end = time.time()
    print(end-start)
    f = input('Would you like to terminate or get a new layout? Enter Yes or No: ')
    if f == 'Yes' or f == 'yes':
        fin == True
        break

#F_star.adaptive_searching()


