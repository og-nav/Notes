"""
Title: Network Delay Time
URL: https://leetcode.com/problems/network-delay-time/description/
Difficulty: Medium
Tags: NeetCode 150
Topics: Depth-First Search Breadth-First Search Graph Heap (Priority Queue) Shortest Path

Approach:
- Basically Dijkstra's, but we take the longest path
- initialize a distances hashmap with infinite distances for each node
- at the top of the while loop, make a check to make sure the popped time is less than the current max time in distances
-- this is because a destination node may have been pushed to the heap multiple times and since the current time is worse
--- than our best time, we don't want to consider this route
- we perform one more check in the for loop to make sure only viable candidate routes are pushed to the heap
- IMPORTANT: make sure the first element in the tuple is the weight and NOT the node

- also I used to think that Dijkstra's is just BFS (w/ using a visit set) but with a heap instead of a queue
- maybe it's right, but I kept getting the implementation wrong
- so stick to initializing all nodes to infinity and doing the double if statement check

Time Complexity: O(V + E log(V))
Space Complexity: O(V + E)



Solution:
"""
from template import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)] # (time elapsed, starting node)
        distances = {i: float('inf') for i in range(1, n + 1)} # all nodes set to infinity
        distances[k] = 0

        while heap:
            time, node = heapq.heappop(heap)
            if time > distances[node]: # means node was pushed to the heap multiple times and this route is suboptimal
                continue

            for neighbor, weight in graph[node]:
                if time + weight < distances[neighbor]: # candidate path
                    distances[neighbor] = time + weight
                    heapq.heappush(heap, (time + weight, neighbor))
        
        for node in distances:
            if distances[node] == float('inf'): # this node wasn't "visited"
                return -1
        
        return max(distances.values())
              

"""
Question:

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""