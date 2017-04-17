# Assignment 2

Muhammed Hasan Çelik - 213960832

## PriorityQueue

It is similar to course priority queue implementation, since I do not like course implementation, I implement my own priority queue with more pythonic way.

It has 'insert' which is insert item to queue with O(log(n)) time, 'peek' which give min item but do not remove with O(1), 'pop' which give min item and remove with O(log(n)), 'decrease_key' which update key for given value.

## Grid

It is helper class to create graph. It has two methods: 'cells' which return all cells of grid with their value as tuple of 3 item, and 'neighbors' which return neighbors of given cell coordinates by configuration of question.

## Graph

This is basic graph representation as dictionary like:
```
{
  'node1':{
    'node2': weight,
    ...
  }
  ...
}
```

But class version of this implementation ;thus, it is inherited from dictionary and includes some methods that will be explained in related parts.

## Q.1

I create graph with calling 'from_grid' static method. And I just run my dijkstra implementation on this graph. This 'dijkstra' return 'dists' dictionary which holds all optimal distance from starting point and 'prev' which holds all nodes prev nodes to rich initial node to find path in linear time.

Complexity: O((E+V)\*log(V)) since I use dijkstra algorithm

## Q.2

I create graph with calling 'from_negative_graph'. It creates DAG and I implementation algorithm explained in following psuedo code:

```
prev, dists = initialize prev dists from node

for each node in topological ordered graph then
    for each neighbor_node, neighbor_weight in edges of node then
        if dists[neighbor_node] > dists[node] + neighbor_weight then
            dists[neighbor_node] = dists[node] + neighbor_weight
            prev[neighbor_node] = node

return dists[to_node], path from prev for end point
```
Initially, all dist are inf except staring proint and prev is empty distinary. That implemented 'init_prev_dists' method in graph.

Since it is graph, topological ordering is so easy with just iterating each row by order and outputing each item in row by order. That implemented in 'topological_order' method in graph.

Lastly, it find path from prev for given node which is end point just while loop until null pointer. That is implemented in 'prev_to_path' method in graph.

Complexity: O(E+V) since it is topological orders and just all node visited by this order.

## Q.3

In last part, I create graph with calling 'from_check_point' method which convert all checkpoint into zero weighted node and store their coordinates in  '\_checkpoints' dynamic property of graph class. Then problem solved with algorithm explained in following psuedo code:

```
source_dists, source_prev = dijkstra(starting_node)
destination_dists, destination_prev = dijkstra(end_node)
cost = float('inf')
for each checkpoint in checkpoints:
    t_cost = source_dists[checkpoint] + destination_dists[checkpoint]
    if cost > t_cost:
        cost = t_cost
        optimal_checkpoint = checkpoint
p_start = path from start to optimal_checkpoint
p_end = path from end to optimal_checkpoint
path = merge p_start and p_end
return cost, path
```

I run dijkstra in beginning for starting and end point to find optimal path from starting point to any point and end point to any point ('dijkstra' method and its outputs explained in previous parts). Then, I iterate each checkpoint and check their distance to source point and end point. And I get min of them. This is checkpoint in optimal path which have checkpoint. Then, I return this path and its path.

Complexity: O((V+E)\*log(V)) because I use two dijkstra their complexity is 2\*(V+E)\*log(V) and iterate all checkpoint one thus plus k. Then, complexity is 2\*(V+E)\*log(V)+k and V >= k thus we can ignore k and 2. Thus, it equal to complexity mentioned above.  
