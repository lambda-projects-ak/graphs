"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def bft(self, starting_vertex):
        # create an empty queue
        q = Queue()  # import queue data structure
        # create an empty visited set
        visited = set()
        # add the starting vertex to the queue
        q.enqueue(starting_vertex)
        # while queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if it has not been visited
            if v not in visited:
                # mark it as visited (add it to the visited set)
                visited.add(v)
                # then enqueue of its neighbors in the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        print("BFT", visited)

    def dft(self, starting_vertex):
       # create an empty stack
        s = Stack()  # import stack data structure
        # create an empty visited set
        visited = set()
        # push the starting vertex to the stack
        s.push(starting_vertex)
        # while stack is not empty
        while s.size() > 0:
            # pop the last vertex, this is the main difference between BFT and DFT
            v = s.pop()
            # if it has not been visited
            if v not in visited:
                # mark it as visited (add it to the visited set)
                visited.add(v)
                # then push its neighbors onto the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        print("DFT", visited)

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()

        # mark the starting node as visited
        # print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        # call dft_recursive on each unvisited neighbors

    def bfs(self, starting_vertex, destination_vertex, visited=None):
        # Return a list containing the shortest path from
        # starting_vertex to destination_vertex in breath-first order.
        q = Queue()
        path = []
        solution = []

        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v not in path and v is not destination_vertex:
                path.append([v, self.vertices[v]])
                for child in self.vertices[v]:
                    q.enqueue(child)
            elif v is destination_vertex:
                path.append(destination_vertex)
                break

        # reverse list so loop doesn't have to iterate backwards
        path.reverse()

        # current value references set before loop because it has no children associated
        current_value = path[0]

        # loop over list
        for i in range(1, len(path) - 1):
            # store children of next node in variable
            next_node_children = path[i + 1][1]

            # compare current node with children of current node
            # if there is a match, it's part of the shortest path
            # append current value and set current value to next value
            if current_value in next_node_children:
                solution.append(current_value)
                current_value = path[i + 1][0]

        # add on starting value since it's always going to be in the path
        solution.append(starting_vertex)
        # reverse to get
        solution.reverse()

        print(path)
        print("Solution", solution)

    # Brady Solution Code
    def bfs2(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty Queue
        q = Queue()
        # Create an empty Visited set
        visited = set()
        # Add A PATH TO the starting vertex to the queue
        q.enqueue([starting_vertex])
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex of the path
            v = path[-1]
            # Check if it's our destination
            if v == destination_vertex:
                return path
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited (add it to the visited set)
                visited.add(v)
                # Then enqueue PATHS TO each of its neighbors in the queue
                for neighbor in self.vertices[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        # Return a list containing a path from starting_vertex
        # to destination_vertex in depth-first order.
        s = Stack()
        destination_path = []

        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop()

            if v not in destination_path and v is not destination_vertex:
                destination_path.append(v)

                for neighbor in self.vertices[v]:
                    s.push(neighbor)

            elif v is destination_vertex:
                destination_path.append(v)
                break

        print("DFS", destination_path)

    # Brady Solution Code
    def dfs2(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack
        s = Stack()
        # Create an empty Visited set
        visited = set()
        # Add A PATH TO the starting vertex to the queue
        s.push([starting_vertex])
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # Grab the last vertex of the path
            v = path[-1]
            # Check if it's our destination
            if v == destination_vertex:
                return path
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited (add it to the visited set)
                visited.add(v)
                # Then push PATHS TO each of its neighbors in the stack
                for neighbor in self.vertices[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
