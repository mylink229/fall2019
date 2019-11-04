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

    """
    "*** YOUR CODE HERE ***"
    """util.raiseNotDefined()"""
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState())) #false
    #print("Is the start a goal?", problem.isGoalState((1,1))) #true
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
 
    #start = problem.getStartState()
    fringe = util.Stack()
    vistedSuccessors = []

    # gets start state
    currentState = problem.getStartState()
    # no direction since just starting
    direction = []
    # cost = 0 since just starting
    cost = 0
    vistedSuccessors.append(currentState)

    # before this while loop, currentState == (5,5)
    # therefore, the goal state is false and will 
    # kick off this loop
    while not problem.isGoalState(currentState):
        sucessors = problem.getSuccessors(currentState)
        for s in sucessors:
            if (s[0] not in vistedSuccessors ):
                fringe.push((s[0], direction + [s[1]], cost + s[2]))
                vistedSuccessors.append(s[0])
        (currentState, direction, cost) = fringe.pop()
    return direction

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    currentState = problem.getStartState()
    directions = []
    cost = 0
    fringe = util.Queue()
    vistedSuccessors = []
    vistedSuccessors.append(currentState)

    while not problem.isGoalState(currentState):
        successors = problem.getSuccessors(currentState)
        for s in successors:
            if (s[0] not in vistedSuccessors) or (problem.isGoalState(s[0])):
                fringe.push((s[0], directions + [s[1]], cost + s[2]))
                vistedSuccessors.append(s[0])
        (currentState, directions, cost) = fringe.pop()

    return directions

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue() 
    visitedSuccessor = []
    currentState = problem.getStartState
    directions = []
    cost = 0
    totalCost = 0

    fringe.push((problem.getStartState(),[],0),0)

    (currentState,directions,cost) = fringe.pop()

    visitedSuccessor.append((currentState,cost))

    while not problem.isGoalState(currentState): 
        successors = problem.getSuccessors(currentState) 
        for s in successors:
            visitedExist = False
            totalCost = cost + s[2]
            for (visitedState, visitedToCost) in visitedSuccessor:
                if (s[0] == visitedState) and (cost >= visitedToCost): 
                    visitedExist = True
                    break

            if not visitedExist:        
                fringe.push((s[0],directions + [s[1]],cost + s[2]),cost + s[2]) 
                visitedSuccessor.append((s[0],cost + s[2])) 

        (currentState,directions,cost) = fringe.pop()

    return directions







def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    fringe = util.PriorityQueue()
    visitedSuccessors = []
    cost = 0
    totalCost = 0
    directions = []
    currentState = problem.getStartState()
    heri = heuristic(currentState, problem)

    visitedSuccessors.append((currentState, cost + heri))

    while not problem.isGoalState(currentState): 
        successors = problem.getSuccessors(currentState)
        for s in successors:
            visitedExist = False
            totalCost = cost + s[2]
            for (visitedState,visitedToCost) in visitedSuccessors:
                if (s[0] == visitedState) and (totalCost >= visitedToCost): 
                    visitedExist = True
                    break

            if not visitedExist:        
                fringe.push((s[0],directions + [s[1]],cost + s[2]),cost + s[2] + heuristic(s[0],problem)) 
                visitedSuccessors.append((s[0],cost + s[2])) 

        (currentState,directions,cost) = fringe.pop()

    return directions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
