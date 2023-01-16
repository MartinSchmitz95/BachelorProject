import networkx as nx
import pickle
import numpy as np

def normalize(e, min, max):
    e = (e - min) / (max - min)
    return e

def process(path, additional_feature):
    G = nx.read_gpickle(path)
    #print(set(np.array([list(G._node[n].keys()) for n in G.nodes()]).flatten()))
    #print(set(np.array([list(G.edges[n].keys()) for n in G.edges()]).flatten()))

    n = nx.number_of_edges(G)
    
    with open("x.pkl", "wb") as handleX, open("y.pkl", "wb") as handleY:
        edgeFeatures1 = []
        edgeFeatures2 = []

        edgeFeatures11 = list((nx.get_edge_attributes(G, "overlap_length")).values())
        edgeFeatures12 = list((nx.get_edge_attributes(G, "overlap_similarity")).values())

        overlapLengthMin = min(edgeFeatures11)
        overlapLengthMax = max(edgeFeatures11)
        edgeFeatures11 = [normalize(e, overlapLengthMin, overlapLengthMax) for e in edgeFeatures11]

        if (additional_feature == "sequence_length"):
            nodeFeatures1 = list((nx.get_node_attributes(G, "read_length")).values())

            edgesNode = []
            for e in G.edges():
                source,target = e
                edgesNode.append(e)
            
            readLengthMin = min(nodeFeatures1)
            readLengthMax = max(nodeFeatures1)
            nodeFeatures1 = [normalize(n, readLengthMin, readLengthMax) for n in nodeFeatures1]
            
        
        edgeFeatures1 = []
        for i in range(0, len(edgeFeatures11)):
            edgeFeatures1.append(edgeFeatures11[i])
            edgeFeatures1.append(edgeFeatures12[i])
            if (additional_feature == "sequence_length"):
                edgeFeatures1.append(nodeFeatures1[int(edgesNode[i][0])])
                edgeFeatures1.append(nodeFeatures1[int(edgesNode[i][1])])

        edgeFeatures2.extend((nx.get_edge_attributes(G, "ground_truth")).values())

        pickle.dump(edgeFeatures1, handleX, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(edgeFeatures2, handleY, protocol=pickle.HIGHEST_PROTOCOL)



        
