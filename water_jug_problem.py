from __future__ import print_function
from simpleai.search import SearchProblem, breadth_first, depth_first, limited_depth_first, \
    iterative_limited_depth_first, uniform_cost
from simpleai.search.viewers import BaseViewer

capacities = []
targets = []

class WaterJugProblem(SearchProblem):
    def __init__(self, initial_state=None):
        super().__init__(initial_state)
        print("Enter the capacities of 3 jugs: ")
        for _ in range(3):
            c = input()
            capacities.append(int(c))
        print("Enter target values of the jugs: ")
        for _ in range(3):
            t = input()
            targets.append(int(t))
        print("==============================================")
        print(f"The capacities of 3 jugs : {capacities}")
        print(f"The target values for the jugs : {targets}")
        print(f"The initial state is : {initial_state}")
        print("==============================================")
        print('')

    def actions(self, state):
        action_list = [
            "Fill the first jug",
            "Fill the second jug",
            "Fill the third jug",
            "Empty the first jug",
            "Empty the second jug",
            "Empty the third jug",
            "Add water from first to second jug",
            "Add water from first to third jug",
            "Add water from second to first jug",
            "Add water from second to third jug",
            "Add water from third to first jug",
            "Add water from third to second jug"
        ]
        return action_list

    def result(self, state, action):
        next_state = list(state)

        if action == "Fill the first jug":
            next_state[0] = capacities[0]
        if action == "Fill the second jug":
            next_state[1] = capacities[1]
        if action == "Fill the third jug":
            next_state[2] = capacities[2]
        if action == "Empty the first jug":
            next_state[0] = 0
        if action == "Empty the second jug":
            next_state[1] = 0
        if action == "Empty the third jug":
            next_state[2] = 0
        if action == "Add water from first to second jug":
            next_state[1] = min(state[0]+state[1], capacities[1])
            next_state[0] = state[0] - (next_state[1]-state[1])
        if action == "Add water from first to third jug":
            next_state[2] = min(state[0]+state[2], capacities[2])
            next_state[0] = state[0] - (next_state[2]-state[2])
        if action == "Add water from second to first jug":
            next_state[0] = min(state[0] + state[1], capacities[0])
            next_state[1] = state[1] - (next_state[0] - state[0])
        if action == "Add water from second to third jug":
            next_state[2] = min(state[1] + state[2], capacities[2])
            next_state[1] = state[1] - (next_state[2] - state[2])
        if action == "Add water from third to first jug":
            next_state[0] = min(state[0] + state[2], capacities[0])
            next_state[2] = state[2] - (next_state[0] - state[0])
        if action == "Add water from third to second jug":
            next_state[1] = min(state[1] + state[2], capacities[1])
            next_state[2] = state[2] - (next_state[1] - state[1])

        return tuple(next_state)

    def cost(self, state, action, state2):
        if action == "Fill the first jug":
            return capacities[0] - state[0]
        if action == "Fill the second jug":
            return capacities[1] - state[1]
        if action == "Fill the third jug":
            return capacities[2] - state[2]
        if action == "Empty the first jug":
            return state[0]
        if action == "Empty the second jug":
            return state[1]
        if action == "Empty the third jug":
            return state[2]
        if action == "Add water from first to second jug":
            return abs(state2[0] - state[0])
        if action == "Add water from first to third jug":
            return abs(state2[0] - state[0])
        if action == "Add water from second to first jug":
            return abs(state2[1] - state[1])
        if action == "Add water from second to third jug":
            return abs(state2[1] - state[1])
        if action == "Add water from third to first jug":
            return abs(state2[2] - state[2])
        if action == "Add water from third to second jug":
            return abs(state2[2] - state[2])
        else:
            return 1

    def is_goal(self, state):
        return state == tuple(targets)


initial = (0, 0, 0)
problem = WaterJugProblem(initial)
my_viewer = BaseViewer()
print("                                            \n"
      "                                            \n"
      "                                            \n"
      " ======= Uninformed Search Algorithms =======\n"
      "                                            \n"
      "                                            \n"
      "                                            \n"
      "==============================================")


def breadth_first_search(graph_search = True):
    result = breadth_first(problem, graph_search=graph_search, viewer=my_viewer)
    try:
        print("Algorithm : Breadth-First Search")
        print(f"Graph Search = {graph_search}")
        print(f"Resulting State : {result.state}")
        print("Resulting Path :")
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(result.path())))
        print(f"Total cost : {result.cost}")
        print(my_viewer.stats)
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")
    except:
        print("No result for this algorithm with the given parameters")
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")

def depth_first_search(graph_search = True):
    result = depth_first(problem, graph_search=graph_search, viewer=my_viewer)
    try:
        print("Algorithm : Depth-First Search")
        print(f"Graph Search = {graph_search}")
        print(f"Resulting State : {result.state}")
        print("Resulting Path :")
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(result.path())))
        print(f"Total cost : {result.cost}")
        print(my_viewer.stats)
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")
    except:
        print("No result for this algorithm with the given parameters")
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")

def depth_limited_search(limit = 100, graph_search = True):
    result = limited_depth_first(problem, limit, graph_search=graph_search, viewer=my_viewer)
    try:
        print("Algorithm : Depth-Limited Search")
        print(f"Depth Limit = {limit}")
        print(f"Graph Search = {graph_search}")
        print(f"Resulting State : {result.state}")
        print("Resulting Path :")
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(result.path())))
        print(f"Total cost : {result.cost}")
        print(my_viewer.stats)
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")
    except:
        print("No result for this algorithm with the given parameters")
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")

def iterative_limited_depth_search(graph_search = True):
    result = iterative_limited_depth_first(problem, graph_search=graph_search, viewer=my_viewer)
    try:
        print("Algorithm : Iterative Limited Depth Search")
        print(f"Graph Search = {graph_search}")
        print(f"Resulting State : {result.state}")
        print("Resulting Path :")
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(result.path())))
        print(f"Total cost : {result.cost}")
        print(my_viewer.stats)
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")
    except:
        print("No result for this algorithm with the given parameters")
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")

def uniform_cost_search(graph_search = True):
    result = uniform_cost(problem, graph_search=graph_search, viewer=my_viewer)
    try:
        print("Algorithm : Uniform Cost Search")
        print(f"Graph Search = {graph_search}")
        print(f"Resulting State : {result.state}")
        print("Resulting Path :")
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(result.path())))
        print(f"Total cost : {result.cost}")
        print(my_viewer.stats)
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")
    except:
        print("No result for this algorithm with the given parameters")
        print("                                            \n"
              "                                            \n"
              "                                            \n"
              "============================================")

def test_func():
    breadth_first_search()
    depth_first_search()
    depth_limited_search(5)
    depth_limited_search(200)
    iterative_limited_depth_search()
    uniform_cost_search()

if __name__ == '__main__':
    test_func()
