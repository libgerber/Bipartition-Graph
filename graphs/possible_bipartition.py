# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
#     let’s see various Operations on deque : 

# append():- This function is used to insert the value in its argument to the right end of the deque.
# appendleft():- This function is used to insert the value in its argument to the left end of the deque.
# pop():- This function is used to delete an argument from the right end of the deque.
# popleft():- This function is used to delete an argument from the left end of the deque. 

    if dislikes == []:
        return True
    #list of that is legnth of dislikes, each index will be listed as False to start
    visited = [False] * len(dislikes)
    print(visited)
    
    group1 = set()
    group2 = set()

    doggy_queue = deque()
    #index 0 is added to queue
    doggy_queue.append(0)

    while doggy_queue:
        current_dog = doggy_queue.popleft()
        #when a node is visited, it changes from False to True
        visited[current_dog] = True
        #checks if that one is empty. If empty, then add
        if not dislikes[current_dog]:
            doggy_queue.append(current_dog+1)
    #iterate through adjasency list
        for dog in dislikes[current_dog]:
            #if node not visited, append to queue
            if not visited[dog]:
                doggy_queue.append(dog)
    #check if node is in group1; can't be in same group
            if current_dog not in group1:
                if dog in group2:
                    return False
                #if not in group1; add to group1
                group1.add(dog)
            else:
                if dog in group1:
                    return False
                group2.add(dog)
    print(visited)

    return True

dislikes = [ [],
      [2, 3],
      [1, 4],
      [1],
      [2]
    ]
print(possible_bipartition(dislikes))