#Thomas Patsanis, 3318

import sys
import ast
import math
from queue import PriorityQueue




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



def convertInputToInt(list):
	for i in range(len(list)):
		list[i] = int(list[i])
	



def executeDijkstra(source_node):
	queue = PriorityQueue()
	iterations=0
	nodes = {}
	source = [0,source_node,[]]
	queue.put(source)
	#visited.append(source_node)
	while(queue):
		iterations+=1
		current_node = queue.get()

		yield(current_node)
		
		if current_node[1] in nodes:
			iterations-=1
		nodes[current_node[1]] = [current_node[0],current_node[2]]
		neighbors = findNeighbors(current_node[1])
		#print(current_node[1])
		#if(current_node[1] != target_node):
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





	



def nra(starting_nodes):
	generators_list = []
	nodes_dict = {}
	best_up = math.inf
	for i in starting_nodes:
		#returns something like [dist,id,path]
		gen = executeDijkstra(i)
		generators_list.append(gen)
		#lower_bound.append(0)
	flag = False
	known = -1
	extras = []
	mini = [-math.inf]*len(starting_nodes)
	while(not flag):
		for i in range(len(starting_nodes)):
			node = next(generators_list[i])
			n_dist = node[0]
			n_id = node[1]
			n_path = node[2]
			if(mini[i]<n_dist):
				mini[i]=n_dist
			#upper_bound = n_dist
			if n_id in nodes_dict:

				if(i not in nodes_dict[n_id][2]):
					nodes_dict[n_id][2].append(i)
					nodes_dict[n_id][1][i] = n_dist
				if(len(nodes_dict[n_id][2]) == len(starting_nodes) and nodes_dict[n_id][0] == -1):
					nodes_dict[n_id][0] = max(nodes_dict[n_id][1])
					if(nodes_dict[n_id][0]<best_up):
						extras = []
						best_up = nodes_dict[n_id][0]
						known = n_id
						print("Best point until now: "+str(known))
						print("Upper Bound until now: "+str(nodes_dict[known][0]))
					elif(nodes_dict[n_id][0]==best_up):
						extras.append(n_id)
			else:
				lower_bound = [0] * len(starting_nodes)
				upper_bound = -1
				lower_bound[i] = n_dist
				nodes_dict[n_id] = [upper_bound,lower_bound,[i]]
				
		
			if(known!=-1 and nodes_dict[known][0]<min(mini)):
				
				print("\n-------------FINAL RESULTS-------------")
				print("Point Of Meeting: "+str(known))
				print("Bounds: "+str(nodes_dict[known][1]))
				print("Upper Bound: "+str(nodes_dict[known][0]))
				print("Also at the same cost you can meet in: "+str(extras))
				flag = True
				break
			 









def main(argv):
	global data
	#print(argv)
	convertInputToInt(argv)
	#print(argv)
	data = readData()
	nra(argv)



data = []
if __name__ == '__main__':
	main(sys.argv[1:])



