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
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    
    

    frontier = util.Stack()#para garantiar FIFO y que la busqueda sea en profucnidad 
                           #expandiendo siempre lo ultio que se hs metido se utiliza la estructura stack
    expanded = []    

    frontier.push((problem.getStartState(), []))
    
    #"meter y sacar nodo y camino"
    while frontier is not None:
        node, path = frontier.pop()
        if problem.isGoalState(node):
            return path
        if node not in expanded:
            expanded.append(node)
            for each in problem.getSuccessors(node):
                if (each[0] not in expanded):
                    frontier.push((each[0], path + [each[1]]))#el nuevo movimiento se concatena con el path ya obtenido
                                                              #de esta manera siempre guardamos el camino que hemos ido siguiendo
                    
                    
            
    return  []
   

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    
    frontier = util.Queue()#Garantizamos la politica LiFo para que la busqueda sea en anchura
    expanded = []    

    frontier.push((problem.getStartState(), []))

  
    while frontier is not None:
        
        node, path = frontier.pop()#extraemos por separado el nodo y el camino que hemos ido siguiendo graccias a la tupla
        
        if problem.isGoalState(node):  
            return path
        if node not in expanded:
            expanded.append(node)
            for each in problem.getSuccessors(node):
                if (each[0] not in expanded):
                    frontier.push((each[0], path + [each[1]]))#el nuevo movimiento se concatena con el path ya obtenido
                                                              #de esta manera siempre guardamos el camino que hemos ido siguiendo
                    
        
            
    return  []
    

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    
    frontier = util.PriorityQueue()# empezamos a implementar colas con prioridad para que el coste sea el que nos interesa
    expanded = []    

    frontier.push((problem.getStartState(), []), 0)# en la primera iteracion el coste es 0 porque no se inserta nuevo movimieinto

  
    while frontier is not None:
        node, path = frontier.pop()
        cost = problem.getCostOfActions(path)
        if problem.isGoalState(node):
            return path
        if node not in expanded:
            expanded.append(node)
            for each in problem.getSuccessors(node):
                if (each[0] not in expanded):
                    frontier.push((each[0], path + [each[1]]), cost + each[2])#se añade el nuevo movimiento con el coste que tiene
                                                                              #concatenado el path mas el nuevo moviemiento
                                                                              #y la prioridad es el coste total del path mas el coste del nuevo movimiento

    return  []



    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0

#si quiero añadir una hheuristica nueva solo tengo que añadir una funcion nueva y ponerla en el comando 

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    #definimos Aheuristic para que sea la suma de la heuristica y el coste de las acciones
    #utilizo como valor de heuristica el valor que se me da en la aStarSearch
    def AHeuristic(state, heuristic):
        
        return heuristic(state[0], problem) + problem.getCostOfActions(state[1])
    
    frontier = util.PriorityQueueWithFunction(AHeuristic) #nuestra cola usa como funcion de prioridad la Aheuristic
    expanded = []    

    #Pasamos como heuristica heuristic pq ya eat definida que es la que le paso en la creacion de la cola
    frontier.push((problem.getStartState(), []),heuristic) 
    
    
    while frontier is not None:
        node, path= frontier.pop()
        if problem.isGoalState(node):
            return path
        if node not in expanded:
            expanded.append(node)
            for each in problem.getSuccessors(node):
                if (each[0] not in expanded):
                    frontier.push((each[0], path + [each[1]]), heuristic) #si la nueva direccion no esta en expanded la añadimos a la cola, concatenando 
                                                                          #con el path que ya hemos ido obteniendo,y la tupla entera entra con la
                                                                          #prioridad definida por la heuristica

    return  []

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
