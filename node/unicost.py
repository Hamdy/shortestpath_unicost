from queue import PriorityQueue

from .models import Edge

def get_children(nodename):
    """
    Given node name, get all nodes connected to this node
    """
    return Edge.objects.filter(start=nodename)

# uniform cost
def unicost(start, goal):
    """
    Uniform cost algorithm
    """
    
    # start & goal are equal, no short path
    if start == goal:
        return []

    q = PriorityQueue()
    visited = set()
    branch = {}
    found = False

    q.put((0, start)) # (weight=0, starting node name)

    while not q.empty():
        item = q.get()
        current= item[1] # current node name

        if current == start:
            current_cost = 0
        else:
            current_cost = branch[current][0]

        print("current %s" % current)
        if current == goal:
            found = True
            break
        else:
            
            for edge in get_children(current):
                cost = edge.cost
                queue_cost = current_cost + cost
                
                edge_tuple = edge.to_tuple()
                
                if edge_tuple not in visited:
                    print("\tadding to queue %s" % edge)
                    visited.add(edge_tuple)
                    q.put((queue_cost, edge.end))
                    branch[edge.end] = (queue_cost, current, edge.end) 

    path = []
    if found:
        # retrace steps
        path = []
        n = goal
        path_cost = branch[n][0]
        while branch[n][1] != start:
            path.append(branch[n][2])
            n = branch[n][1]
        path.append(branch[n][2])
        path.append(start)
    return path[::-1]
