"""
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
"""

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        self.dfs(robot, 0, 0, 0, 1, visited)

    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))

        for k in range(4):
            new_x = x + direction_x
            new_y = y + direction_y

            if (new_x, new_y) not in visited and robot.move():
                self.dfs(robot, new_x, new_y, direction_x, direction_y, visited)
                # Backtrack to the previous location
                robot.turnLeft()
                robot.turnLeft()
                robot.move()

                # turn back to its previous orientation
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft() # this help the robot turn to the new orientation
            direction_x, direction_y = -direction_y, direction_x
room = [
           [1,1,1,1,1,0,1,1],
           [1,1,1,1,1,0,1,1],
           [1,0,1,1,1,1,1,1],
           [0,0,0,1,0,0,0,0],
           [1,1,1,1,1,1,1,1]
       ],
row = 1,
col = 3