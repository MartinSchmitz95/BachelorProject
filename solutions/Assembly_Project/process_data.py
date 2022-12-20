import networkx as nx
import pickle

if __name__ == '__main__':
    G0 = nx.read_gpickle('./chr19_raven_graphs_nx_with_gt/train/0.gpickle')
    G1 = nx.read_gpickle('./chr19_raven_graphs_nx_with_gt/train/1.gpickle')
    G2 = nx.read_gpickle('./chr19_raven_graphs_nx_with_gt/val/2.gpickle')
    G3 = nx.read_gpickle('./chr19_raven_graphs_nx_with_gt/test/3.gpickle')
    G0e = G0.edges
    G1e = G1.edges
    G2e = G2.edges
    G3e = G3.edges
    x0 = []
    y0 = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    for e in G0e:
        xt = [G0e[e]['overlap_length'], G0e[e]['overlap_similarity']] #x temporary
        x0.append(xt)
        yt = (G0e[e]['ground_truth'])
        y0.append(yt)
    for e in G1e:
        xt = [G1e[e]['overlap_length'], G1e[e]['overlap_similarity']]
        x1.append(xt)
        yt = (G1e[e]['ground_truth'])
        y1.append(yt)
    x = x1 + x2
    y = y1 + y2
    with open('./chr19_raven_graphs_nx_with_gt/train/x.pkl', 'wb') as f:
        pickle.dump(x, f)
    with open('./chr19_raven_graphs_nx_with_gt/train/y.pkl', 'wb') as f:
        pickle.dump(y, f)

    for e in G2e:
        xt = [G2e[e]['overlap_length'], G2e[e]['overlap_similarity']] #x temporary
        x2.append(xt)
        yt = (G2e[e]['ground_truth'])
        y2.append(yt)
    with open('./chr19_raven_graphs_nx_with_gt/val/x.pkl', 'wb') as f:
        pickle.dump(x2, f)
    with open('./chr19_raven_graphs_nx_with_gt/val/y.pkl', 'wb') as f:
        pickle.dump(y2, f)

    for e in G3e:
        xt = [G3e[e]['overlap_length'], G3e[e]['overlap_similarity']]  # x temporary
        x3.append(xt)
        yt = (G3e[e]['ground_truth'])
        y3.append(yt)
    with open('./chr19_raven_graphs_nx_with_gt/test/x.pkl', 'wb') as f:
        pickle.dump(x3, f)
    with open('./chr19_raven_graphs_nx_with_gt/test/y.pkl', 'wb') as f:
        pickle.dump(y3, f)