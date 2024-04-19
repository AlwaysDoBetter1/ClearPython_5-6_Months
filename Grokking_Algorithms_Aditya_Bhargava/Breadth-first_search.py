"""
Breadth-first search, for finding nearest required object in FIFO queue
"""

from collections import deque

# bulding genealogy tree graph ith unweighted connections
graph = {}
graph["you"] = ["dad", "mom"]
graph["dad"] = ["uncle", "aunt1", "you"]
graph["mom"] = ["aunt2", "you"]
graph["aunt1"] = ["dad"]
graph["aunt2"] = ["mom"]
graph["uncle"] = ["dad"]

# function for found the right person
def search(start, name):
    search_queue = deque()
    search_queue += graph[start]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:  # for preventing an endless loop when person refer to each other
            if person == name:
                print("the person was found")
                return True
            else:  # looking further afield
                search_queue += graph[person]
                searched.append(person)
    return False  # if not found

search("you", "uncle")


