class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    print(start)
    
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return None

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

dfs(gdict, 'a')

'''
output:
a
b
d
e
c
'''
