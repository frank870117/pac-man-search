# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    #creating a stack
    stack = util.Stack()
    stack.push(problem.getStartState())
    print(stack.pop)
    #push in 2 empty nodes and use the getStartState to get initial
    notEmptiness = True
    emptyBlock = []
    visited = []
    stack.push((problem.getStartState(), emptyBlock) )
    while notEmptiness:
        #assign the 2 empty nodes to aciton and visited
        block, direction = stack.pop()
        #if the goal state is reached, exit while loop and return path
        if problem.isGoalState(block):
            notEmptiness = False
            return path
        #loop through its children using getSuccessor
        for child, direct, steps in problem.getSuccessors(block):
            #check against the visited array
            if not child in visited:                
                visited = visited + [block]
                stack.push((child, direction + [direct] ))
                path = direction + [direct]
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #created a queue
    queue = util.Queue()
    #assign initial blocks
    emptyBlock = []
    #push the initial block into the queue, and keep track of visited and path
    queue.push( (problem.getStartState(), emptyBlock, emptyBlock) )
    visited = []
    notEmptiness = True
    #loop through the entire array
    while notEmptiness:
        block, path, Steps = queue.pop()
        if(not block in visited):
            visited.append(block)
            #exit if goal block
            if problem.isGoalState(block):
                notEmptiness = False
                return path
            #go to children if not goal
            for child, direct, steps in problem.getSuccessors(block):
                queue.push((child, path+[direct], Steps + [steps]))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #create priority queue
    priority = util.PriorityQueue()
    emptyBlock = []
    visited = []
    #get the starting block, and we add the cost of the block this time, which will be called step
    priority.push( (problem.getStartState(), emptyBlock, 0), 0 )
    notEmptiness = True
    while notEmptiness:
        #Steps is total step
        block, path, Steps = priority.pop()
        if(not block in visited):
            #to make sure we dont go back to same block
            visited.append(block)
            if problem.isGoalState(block):
                notEmptiness = False
                return path
            for child, direct, step in problem.getSuccessors(block):
                priority.push((child, path+[direct], Steps + step), Steps + step)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    priority2 = util.PriorityQueue()
    priority2.push( (problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem) )
    visited = []
    g = []
    notEmptiness = True
    while notEmptiness:
        node, path, Steps = priority2.pop()

        if(not node in visited):
            visited.append(node)

            if problem.isGoalState(node):
                notEmptiness = False
                return path

            for child, direct, step in problem.getSuccessors(node):
                g = Steps + step
                priority2.push((child, path+[direct], Steps + step), g + heuristic(child, problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
