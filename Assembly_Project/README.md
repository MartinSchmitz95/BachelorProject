# Assembly Project

This project deals with the topic of Genome assembly with Neural networks. In this task, you get a dataset of assembly graphs created by [Raven](https://github.com/lbcb-sci/raven) with annotated edge labels.

The goal is to train a neural network to classify the edges in the graph as positive and negative edges. Positive edges are edges that are part of an optimal assembly walk, and negative edges are edges that are not part of an optimal assembly walk. After classifying edges, it is easy to find the assembly and walk through the graph to create an assembly.

give them a dataset of graphs as networkx file (including sequence as a feature, but maybe without other features)
load networkx file

## Prepare the dataset
Write a script **process_data.py**
Input: path to the dataset
Output: two files: **x.pkl** and **y.pkl**

First, you need to download the dataset from Godot and unpack the file. You can find the data under: **\home\mschmitz\shared\chr19_raven_graphs_nx_with_gt.tar**
The dataset contains three folders: train, val and test. Train contains two files, the other folders contain one each. The files are pickled networkx graphs.
Install the library networkx and load the graphs in your script. Networkx is a python library for working with graphs. You can check [this link](https://networkx.org/documentation/stable/tutorial.html) to get an overview.

The networkx files are assembly graphs from Raven. Given a FASTA file, Raven can compute an assembly graph from overlaps. Those specific assembly graphs are derived from synthetic reads sampled from chromosome 19.

The networkx graph contains different edge features. Save the edge features **overlap_length** and **overlap_similarity** as a file x.pkl and the edge features **ground_truth** as y.pkl.

Tip: The graphs are quite large. For debugging it could make sense to split the graph or only process a subset.

## Train Neural Network
Write a script **train.py**
Input: two files: **x.pkl** and **y.pkl**
Output: The trained neural network **model.py**

Checkout [this tutorial](https://medium.com/biaslyai/pytorch-introduction-to-neural-network-feedforward-neural-network-model-e7231cff47cb) and [this tutorial](https://pytorch.org/tutorials/beginner/basics/intro.html) of how a MultiLayer Perceptron works and can be implemented in Python using Pytorch. Since this is your first encounter with machine learning, you can take some time to try to understand the basic concepts and follow the tutorials. I also encourage you to read other beginner-friendly introductions to neural networks at this point.
Implement a neural network with a training and evaluation loop to process the dataset consisting of samples **x.pkl** and labels **y.pkl**. This is a basic classification task. Follow [this tutorial](https://medium.com/biaslyai/pytorch-introduction-to-neural-network-feedforward-neural-network-model-e7231cff47cb) for the implementation.

**Note:** For the BCE-loss, please add a parameter weight=pos_neg_ratio, where pos_neg_ratio is the ratio of positive to negative labels in the dataset. The dataset is highly unbalanced, which makes it challenging to learn the neural network, without this.

Compute and track the following metrics on both training and validation sets:
* Loss
* Accuracy
* False Negative Rate
* False Positive Rate
Save the trained model as **model.py**.

**Optional:**
Track the metrics using [Weights and Biases](https://docs.wandb.ai/guides/track)

## Optional: Test different node and edge features

Create a file **pipeline.py**
Input: a node feature configuration
Output: trained model and evaluation

The script calls both: **process_data.py** and **train.py** to process data and train a model on it. Then it evaluates the performance of the newly trained model.
The goal of the task is to experiment with different feature vectors as input for the neural network. Feature engineering is an important part of many machine-learning projects.
Every edge has a source and a target node, so in addition to edge features, source and target node features can be added to the feature vectors.
Test the following features as input for the neural network:

Edge Features:
* overlap length
* overlap similarity
Node Features:
* sequence length
* in- and out-degree
* longest distance (check [this](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.dag.dag_longest_path.html))
* look for other features

Do all of those features improve the results of the model? Which is the optimal combination of features?

**Note:** You can try different normalization techniques for the features
