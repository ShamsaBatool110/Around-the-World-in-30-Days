def baalti(graph, root):
    distance = [] #format = [['vertex', distance]]
    bucket = []
    queue = []
    bucket.append(root)
    distance.append([root, 0])
    for e in graph[root]:
        queue.extend(e[0])
     
    while len(bucket) != len(graph):
        # get the edges of last added vertex
        current_vertex = bucket[-1]
        optional_edges = []
        for vertex in graph:
            if current_vertex == vertex:
                optional_edges = graph[vertex]
        # select edge with minimum weight
        min_weight = 100000
        min_w_edge = ''
        for edge in optional_edges:
            if (edge[1] + distance[-1][1]) < min_weight:
                if edge[0] not in bucket:
                    min_weight = edge[1]
                    min_w_edge = edge[0]
        # iterate on queue to delete the vertex selected
        for corr_vertex in queue:
            if corr_vertex == min_w_edge:
                queue.remove(corr_vertex)
        # update bucket, distance and queue
        bucket.append(min_w_edge)
        distance.append([min_w_edge, (min_weight + distance[-1][1])])
        for e in graph[min_w_edge]:
            queue.extend(e[0])
    return distance

graph = {'a': [['b',2], ['k',9], ['f',3]], 'b': [['c',2], ['d',3], ['a', 2]], 'd' : [['b',3], ['f',2], ['e',1]], 'f': [['d',2], ['a',3], ['g',3]], 'c' : [['b',2], ['k',3]], 'e' : [['d',1], ['c', 1]], 'g' : [['f',3], ['h',2]], 'k' : [['c',3], ['i',3], ['a',9]], 'h' : [['g',2], ['i',6], ['j',4]], 'i' : [['k',3], ['j',3], ['h',6]], 'j' : [['i',3], ['h', 4]]}
root = 'e'
distances = baalti(graph, root)
print(distances)