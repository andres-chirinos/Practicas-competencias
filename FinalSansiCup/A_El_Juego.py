#https://sansicup.jukijudge.com/contest/view/2880/problems

def bfs_path(start,goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return -1

for _i in range(int(input())):
    n = int(input())
    graph = {str(x):set() for x in range(1,n+1)}
    for _ in range(1,n):
        a_i, b_i = input().split()
        graph[a_i].add(b_i)
        graph[b_i].add(a_i)
    start='1'
    for i in range(2,n+1):
        if len(graph[str(i)])==1:
            print(_i,graph,len(bfs_path(start, str(i)))%2==0)
    