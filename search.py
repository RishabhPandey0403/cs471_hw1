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

def depthFirstSearch(problem: SearchProblem):
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
    "*** YOUR CODE HERE ***"
    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    visited = set()
    stack = util.Stack()
    state = problem.getStartState()

    stack.push((state, []))
    while not stack.isEmpty():
        state, actions = stack.pop()
        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return actions
        
        successors = problem.getSuccessors(state)
        for successor, action, stepCost in successors:
            if successor not in visited:
                updated_actions = actions + [action]
                stack.push((successor, updated_actions))

    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    queue = util.Queue()
    state = problem.getStartState()

    queue.push((state, []))
    while not queue.isEmpty():
        state, actions = queue.pop()
        if state in visited:
            continue
        visited.add(state)

        if problem.isGoalState(state):
            return actions
        
        successors = problem.getSuccessors(state)
        for successor, action, stepCost in successors:
            if successor not in visited:
                updated_actions = actions + [action]
                queue.push((successor, updated_actions))
    
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    visited = set()
    priority_queue = util.PriorityQueue()
    state = problem.getStartState()

    priority_queue.push((None, None, state, 0), 0) # (parent, action, state, cost)
    while not priority_queue.isEmpty():
        z = priority_queue.pop()
        state = z[2]
        if state in visited: 
            continue
        if problem.isGoalState(state):
            break
        
        visited.add(state)
        cost = z[3]
        
        successors = problem.getSuccessors(state)
        for successor, action, stepCost in successors:
            if successor not in visited:
                updated_cost = stepCost + cost
                temp = (z, action, successor, updated_cost)
                priority_queue.push(temp, updated_cost)

    actions = []
    while z[1]:
        actions.insert(0, z[1])
        z = z[0]

    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    priority_queue = util.PriorityQueue()
    state = problem.getStartState()
    
    h = heuristic(state, problem)
    priority_queue.push((None, None, state, 0, h), 0 + h)

    while not priority_queue.isEmpty():
        z = priority_queue.pop()
        state = z[2]
        
        if state in visited:
            continue
        if problem.isGoalState(state):
            break

        visited.add(state)
        cost = z[3]

        successors = problem.getSuccessors(state)
        for successor, action, stepCost in successors:
            if successor not in visited:
                h = heuristic(successor, problem)
                temp = (z, action, successor, stepCost + cost, h)
                priority_queue.push(temp, stepCost + cost + h)
    
    actions = []
    while z[1]:
        actions.insert(0, z[1])
        z = z[0]

    return actions
                

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
