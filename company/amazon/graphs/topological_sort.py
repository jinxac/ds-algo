from collections import deque

def topological_sort(vertices, edges):
      sortedOrder = []
      if vertices <= 0:
            return sortedOrder

      in_degree = {i: 0 for i in range(vertices)}
      graph = {i: [] for i in range(vertices)}

      for edge in edges:
            parent, child = edge[0], edge[1]
            in_degree[child] += 1
            graph[parent].append(child)

      sources = deque()

      for key in in_degree:
            if in_degree[key] == 0:
                  sources.append(key)

      while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                  in_degree[child] -= 1
                  if in_degree[child] == 0:
                        sources.append(child)

      if len(sortedOrder) != vertices:
            return []

      return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()

