#Thomas Patsanis, 3318
#Execute with the 2 files as arguments
#Example: python3 createData.py nodes.txt edges.txt



import sys



def readData(nodes_filename,edges_filename):
	nodes_file = open(nodes_filename, 'r')
	edges_file = open(edges_filename, 'r')
	data = []
	node = []
	for line in nodes_file:
		node_list = []
		node_list = line.split(" ")
		node_id = int(node_list[0])
		node_long = float(node_list[1])
		node_lat = float(node_list[2])
		node = [node_id,node_long,node_lat]
		data.append(node)
	for line in edges_file:
		edge_list = []
		edge_list = line.split(" ")
		neighbor_left = int(edge_list[1])
		neighbor_right = int(edge_list[2])
		distance = float(edge_list[3])
		data[neighbor_left].append(neighbor_right)
		data[neighbor_left].append(distance)
		data[neighbor_right].append(neighbor_left)
		data[neighbor_right].append(distance)
	return data



def writeData(data):
	output_file = open('out.txt', 'w')
	for record in data:
		s = ""
		for x in range(len(record)):
			if x<len(record)-1:
				s += str(record[x])+" "
			else:
				s += str(record[x])
		output_file.write(s+'\n')
	output_file.close()



def main(argv):
	nodes_filename = argv[0]
	edges_filename = argv[1]
	data = readData(nodes_filename,edges_filename)
	writeData(data)


if __name__ == '__main__':
	main(sys.argv[1:])
