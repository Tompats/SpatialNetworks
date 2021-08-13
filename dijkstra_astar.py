#Thomas Patsanis, 3318

import sys
import ast
import math
from queue import PriorityQueue

class Node:
  def __init__(self, id, distance,path):
    self.id = id
    self.distance = distance
    self.path = path



def readData():
	data = []
	out_file = open('out.txt', 'r')
	for line in out_file:
		record = line.split(" ")
		entry = []
		for i in record:
			x = ast.literal_eval(i)
			entry.append(x)
		#print(entry)
		data.append(entry)
	return data





def findNeighbors(id):
	node = data[id]
	n = []
	for i in range(3,len(node),2):
		n.append([node[i],node[i+1]])
	return n







def executeDijkstra(source_node,target_node):
	print("\nDijkstra's Algorithm")
	queue = PriorityQueue()
	iterations=0
	nodes = {}
	source = [0,source_node,[]]
	queue.put(source)
	#visited.append(source_node)
	while(queue):
		iterations+=1
		current_node = queue.get()
		if current_node[1] in nodes:
			iterations-=1
		else:
			nodes[current_node[1]] = [current_node[0],current_node[2]]
			neighbors = findNeighbors(current_node[1])
			#print(current_node[1])
			if(current_node[1] != target_node):
				for neighbor in neighbors:
					if(neighbor[0] in nodes):
						if(current_node[1]<nodes[current_node[1]][0]):
							nodes[current_node[1]] = [current_node[0],current_node[2]]
					else:
						child_path = []
						for p in current_node[2]:
							child_path.append(p)
						child_path.append(current_node[1])
						child_dist = current_node[0]+neighbor[1]
						child = [child_dist,neighbor[0],child_path]
						queue.put(child)

			else:
				nodes[target_node][1].append(target_node)
				break
	print("Number Of Visited Nodes: "+str(iterations))
	print("Shortest Path Distance: "+str(nodes[target_node][0]))
	print("Shortest Path: "+str(nodes[target_node][1]))
	print("Shortest Path Length: "+str(len(nodes[target_node][1])))



def findNeighbors_Astar(id,t_id):
	node = data[id]
	n = []
	for i in range(3,len(node),2):
		dist = getDistance(node[i],t_id)
		n.append([node[i],dist,node[i+1]])
	return n



def getDistance(id,t_id):
	result = 0
	child = data[id]
	target = data[t_id]
	x1 = child[1]
	x3 = target[1]
	y1 = child[2]
	y3 = target[2]
	x_t = (x1-x3)
	y_t = (y1-y3)
	r_t = pow(x_t,2) + pow(y_t,2)
	result_t = math.sqrt(r_t)
	result = result_t
	return result





def executeAStar(source_node,target_node):
	print("\nA* Algorithm")
	queue = PriorityQueue()
	iterations=0
	nodes = {}
	source = [0,source_node,0,[]]
	queue.put(source)
	#visited.append(source_node)
	while(queue):
		iterations+=1
		current_node = queue.get()
		if current_node[1] in nodes:
			iterations-=1
		else:
			nodes[current_node[1]] = [current_node[0],current_node[2],current_node[3]]
			neighbors = findNeighbors_Astar(current_node[1],target_node)
			#print(current_node[1])
			if(current_node[1] != target_node):
				for neighbor in neighbors:
					if(neighbor[0] in nodes):
						if(current_node[1]<nodes[current_node[1]][0]):
							nodes[current_node[1]] = [current_node[0],current_node[2],current_node[3]]
					else:
						child_path = []
						for p in current_node[3]:
							child_path.append(p)
						child_path.append(current_node[1])
						child_dist = neighbor[1]+current_node[2]+neighbor[2]
						child_dist_real = current_node[2]+neighbor[2]
						child = [child_dist,neighbor[0],child_dist_real,child_path]
						queue.put(child)

			else:
				nodes[target_node][2].append(target_node)
				break
	print("Number Of Visited Nodes: "+str(iterations))
	print("Shortest Path Distance: "+str(nodes[target_node][1]))
	print("Shortest Path: "+str(nodes[target_node][2]))
	print("Shortest Path Length: "+str(len(nodes[target_node][2])))








def main(argv):
	global data
	source_node = int(argv[0])
	target_node = int(argv[1])
	data = readData()
	executeDijkstra(source_node,target_node)
	executeAStar(source_node,target_node)



data = []
if __name__ == '__main__':
	main(sys.argv[1:])
