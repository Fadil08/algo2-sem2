# # Graph - Shortest Path (Dijkstra Algoritm)

# - Algoritma Dijkstra adalah sebuah prosedur iteratif yang mencari lintasan terpendek antara a dan z dalam graf dengan pembobot.
# - Prosesnya dengan cara mencari panjang lintasan terpendek dari sebuah simpul pendahulu  dan menambahkan simpul-simpul tersebut ke set simpul S. 
# - Algoritma berhenti setelah mencapai simpul z.

import tkinter as tk
import matplotlib as plt


# create class for graph visualization
class GraphVisualization:
  def __init__(self, graph):
    self.G = tk.Graph()
    self.graph = graph
    self.nodes = list(graph.keys())

  # method for add edges
  def addEdge(self, a, b, weight):
    self.G.add_edge(a, b, weight=weight)
  
  # method for visualize a graph
  def visualize(self):
    pos = tk.spring_layout(self.G)
    weights = tk.get_edge_attributes(self.G, "weight")

    self.G.add_nodes_from(self.nodes)
    plt.figure()
    tk.draw(
      self.G, pos, edge_color='black', width=1, linewidths=1,
      node_size=500, node_color='pink', alpha=0.9,
      labels={node: node for node in self.G.nodes()}
    )
    tk.draw_networkx_edge_labels(self.G, pos, edge_labels=weights)
    plt.axis('off')
    plt.show()

  # visualize a graph
  def graph_visualize(self):
    for i in self.graph:
      for j in self.graph[i]:
        self.addEdge(i, j['v'], j['w'])

    self.visualize()
    # Created graph
graph = {
    'A': [{'v': 'B','w': 4}, {'v': 'C','w': 2}],
    'B': [{'v': 'A','w': 4}, {'v': 'C','w': 1}, {'v': 'D','w': 5}],
    'C': [{'v': 'A','w': 2}, {'v': 'B','w': 1}, {'v': 'D','w': 8}, {'v': 'E','w': 10}],
    'D': [{'v': 'B','w': 5}, {'v': 'C','w': 8}, {'v': 'E','w': 2}, {'v': 'Z','w': 6}],
    'E': [{'v': 'C','w': 10}, {'v': 'D','w': 2}, {'v': 'Z','w': 3}],
    'Z': [{'v': 'D','w': 6}, {'v': 'E','w': 3}]
}
# function for get path weight
def get_path_weight(path):
  path_weight = 0

  for index, value in enumerate(path):
    try:
      for j in graph[value]:
        if j['v'] == path[index + 1]:
            path_weight += j['w']
    except:
      break

  return path_weight
  # function to find the shortest path (dijkstra algorithm)
def find_shortest_path(graph, start, end, path =[]):
  path = path + [start]
  shortest = None
  weights = None

  if start == end: return path

  for node in graph[start]:
      if node['v'] not in path:
          newpath = find_shortest_path(graph, node['v'], end, path)
          if newpath:
            new_wexight = get_path_weight(newpath)
            if not weights or new_wexight < weights:
              shortest = newpath
              weights = new_wexight

  return shortest
shortest_path = find_shortest_path(graph, 'A', 'Z')
weight_shortest_path = get_path_weight(shortest_path)

print('Shortest Path :', shortest_path)
print('Weight :', weight_shortest_path)
shortest_graph = {}

# generate shortest_graph
for index, value in enumerate(shortest_path):
  try:
    for j in graph[value]:
      if j['v'] == shortest_path[index + 1]:
        shortest_graph.update({value: [j]})
  except:
    break

# Visualize shortest path
S = GraphVisualization(shortest_graph)

for i in shortest_graph:
  for j in shortest_graph[i]:
        S.addEdge(i, j['v'], j['w'])

S.visualize()