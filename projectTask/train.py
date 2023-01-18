import torch
import os
import pickle

from process_data import process
from model import FeedforwardModel

class FeatureDataset(torch.utils.data.Dataset):
    def __init__(self, root, additionalFeature):
        self.root = os.path.abspath(root)
        self.additionalFeature = additionalFeature

        self.lista = []
        for filename in os.listdir(self.root):
            f = os.path.join(self.root, filename)
            process(f, additionalFeature)

            file1 = open('x.pkl', 'rb')
            file2 = open('y.pkl', 'rb')

            data1 = pickle.load(file1)
            data2 = pickle.load(file2)

            file1.close()
            file2.close()

            x=torch.FloatTensor(data1)
            n = len(data1)/ int(len(data1)/len(data2))
            x=x.view(int(n), int(len(data1)/len(data2)))
            #print('First tensor is: {}'.format(x),'\nSize of it:{}'.format(x.size()),
            #     '\ntype of tensor:{}\n'.format(x.dtype))
    
            y=torch.FloatTensor(data2)
            #print('Second tensor is: {}'.format(y),'\nSize of it:{}'.format(y.size()),
            #      '\ntype of tensor:{}\n'.format(y.dtype))

            listElement = []
            listElement.append(x)
            listElement.append(y)

            self.lista.append(listElement)

        self.inputSize = int(len(data1)/len(data2))

    def __len__(self):
        return len(os.listdir(self.root))

    def __getitem__(self, i):
        return self.lista[i]

    def __getinputsize__(self):
        return self.inputSize


def statistics(y_t, y, loss):
    correct = 0
    for i in range (0, len(y)):
        if (y[i] == y_t[i]):
            correct = correct + 1
        
    acc = correct / len(y)

    positive = (y_t==1).sum().item()
    true_positive = (y == 1).sum().item()

    false_positive = 0
    if (positive > true_positive):
        false_positive = positive - true_positive

    negative = (y_t==0).sum().item()
    true_negative = (y == 0).sum().item()

    false_negative = 0
    if (negative > true_negative):
        false_negative = negative - true_negative
    
    if (false_negative == 0):
        false_negative_rate = 0
    else:
        false_negative_rate = false_negative / (true_positive + false_negative)

    if (false_positive == 0):
        false_positive_rate = 0
    else:
        false_positive_rate = false_positive / (true_negative + false_positive)

    print("loss: " + str(loss.item()))
    print("accuracy: " + str(acc))
    print("false negative rate: " + str(false_negative_rate))
    print("false positive rate: " + str(false_positive_rate))
    print()

def pos_to_neg_ratio(dataset):
    p = 0
    n = 0
    for x, y in dataset:
        p += (y == 1).sum().item()
        n += (y == 0).sum().item()
    return p / n

def train(additionalFeature):
    test_path="chr19_raven_graphs_nx_with_gt/test"
    dataset = FeatureDataset(test_path, additionalFeature)

    model = FeedforwardModel(FeatureDataset.__getinputsize__(dataset), 100, 50, 150)

    criterion = torch.nn.BCELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

    criterion.weight = torch.tensor([pos_to_neg_ratio(dataset)])
    
    model.eval()

    print("Test statistics:")
    print()
    for x, y in dataset:
        y_prevTrain = model(x)
        before_train = criterion(y_prevTrain.squeeze(), y)

        y_prevTrain = (y_prevTrain>0.5).float()
        statistics(y_prevTrain.squeeze(), y, before_train)

    model.zero_grad()
    model.train()

    train_path="chr19_raven_graphs_nx_with_gt/train"
    dataset = FeatureDataset(train_path, additionalFeature)

    criterion.weight = torch.tensor([pos_to_neg_ratio(dataset)])

    print("Train statistics (last epoch):")
    print()

    epoch = 20
    for x, y in dataset:
        for e in range(epoch):             
            optimizer.zero_grad()
            
            y_t = model(x)
    
            loss = criterion(y_t.squeeze(), y)
    
            loss.backward()
            optimizer.step()

            print("epoch " + str(e) + ": loss: " + str(loss.item()))
            
        y_t = (y_t>0.5).float()

        print()
        statistics(y_t.squeeze(), y, loss)

    val_path="chr19_raven_graphs_nx_with_gt/val"
    dataset = FeatureDataset(val_path, additionalFeature)

    criterion.weight = torch.tensor([pos_to_neg_ratio(dataset)])

    model.eval()

    print("Validate statistics:")
    print()
    
    for x, y in dataset:
        y_afterTrain = model(x)
        after_train = criterion(y_afterTrain.squeeze(), y)

        y_afterTrain = (y_afterTrain>0.5).float()
        statistics(y_afterTrain.squeeze(), y, after_train)


print("Training with edge features: overlap_length, overlap_similarity:")
print()

train("")

print("Training with additional feature: sequence length (read_length):")
print()

train("sequence_length")
