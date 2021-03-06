
import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # Time Complexity: O(numUsers)
        # Space Complexity: O(numUsers)
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(numUsers ^ 2)
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(1)
        random.shuffle(possibleFriendships)

        # Time Complexity: O(avgFriendships * numUsers // 2)
        # Space Complexity: O(avgFriendships * numUsers // 2)
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        visited[userID] = [userID]
        parent_path = visited[userID]
        q.enqueue([self.friendships[userID], parent_path])
        while q.size() > 0:
            friends = q.dequeue()
            friends_set = friends[0]
            parent_path = friends[1]

            for friend in friends_set:
                if friend not in visited:
                    q.enqueue([self.friendships[friend],
                               [*parent_path, friend]])
                    visited[friend] = [*parent_path, friend]
        return visited


def getAllSocialPathsNate(self, userID):
    # # Create an empty Queue
    q = Queue()
    # Create an empty Visited dict
    visited = {}  # Note that this is a dictionary, not a set
    # Add A PATH TO the starting vertex to the queue
    q.enqueue([userID])
    # While the queue is not empty...
    while q.size() > 0:
            # Dequeue the first PATH
        path = q.dequeue()
        # Grab the last vertex of the path
        v = path[-1]

        # If it has not been visited...
        if v not in visited:
                # Mark it as visited
                # Then enqueue each of its neighbors in the queue
            for friendship in self.friendships[v]:
                path_copy = path.copy()
                path_copy.append(friendship)
                visited[v] = path.copy()
                q.enqueue(path_copy)
    return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.users)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    connections2 = sg.getAllSocialPaths(1)
    print(connections)
    print(connections2)
