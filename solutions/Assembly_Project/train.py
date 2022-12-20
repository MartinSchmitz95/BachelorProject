import torch
import pickle
def pnr(y_train):
    b = 0
    n = 0
    for i in y_train:
        if i == 1:
            b += 1
        else:
            n += 1
    return b/n
if __name__=='__main__':
    #x_train = []
    with open('./chr19_raven_graphs_nx_with_gt/train/x.pkl', 'rb') as f:
        x_train = pickle.load(f)
    with open('./chr19_raven_graphs_nx_with_gt/train/y.pkl', 'rb') as f:
        y_train = pickle.load(f)
    with open('./chr19_raven_graphs_nx_with_gt/test/x.pkl', 'rb') as f:
        x_test = pickle.load(f)
    with open('./chr19_raven_graphs_nx_with_gt/test/y.pkl', 'rb') as f:
        y_test = pickle.load(f)



    class Feedforward(torch.nn.Module):
        def __init__(self, input_size, hidden_size):
            super(Feedforward, self).__init__()
            self.input_size = input_size
            self.hidden_size = hidden_size
            self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size)
            self.relu = torch.nn.ReLU()
            self.fc2 = torch.nn.Linear(self.hidden_size, 1)
            self.sigmoid = torch.nn.Sigmoid()
        def forward(self, x):
            hidden = self.fc1(x)
            relu = self.relu(hidden)
            output = self.fc2(relu)
            output = self.sigmoid(output)
            return output

    x_train = torch.FloatTensor(x_train)
    y_train = torch.FloatTensor(y_train)
    x_test = torch.FloatTensor(x_test)
    y_test = torch.FloatTensor(y_test)
    # print(len(x_train))
    # print(len(y_train))
    # print(len(x_test))
    # print(len(y_test))
    pos_neg_ratio = pnr(y_train)
    model = Feedforward(2, 10)
    criterion = torch.nn.BCELoss() #weight=torch.tensor(pos_neg_ratio)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    model.eval()
    y_pred = model(x_test)
    before_train = criterion(y_pred.squeeze(), y_test)
    print('Test loss before training: ', before_train.item())
    correct = 0
    for i in range(len(y_test)):
        if y_pred[i] == y_test[i]:
            correct += 1
    print('Test accuracy before training: ', correct/len(y_test))
    total_neg = 0
    false_neg = 0
    total_pos = 0
    false_pos = 0
    for i in range(len(y_test)):
        if y_pred[i] == 0:
            total_neg += 1
            if y_test[i] == 1:
                false_neg += 1
        else:
            total_pos += 1
            if y_test[i] == 0:
                false_pos += 1
    #print('Test false negative rate before training: ', false_neg/total_neg)
    #print('Test false positive rate before training: ', false_pos/total_pos)


    model.train()
    epoch = 20
    for epoch in range(epoch):
        optimizer.zero_grad()
        y_pred = model(x_train)
        loss = criterion(y_pred.squeeze(), y_train)
        print('Epoch {}: train loss: {}'.format(epoch, loss.item()))
        loss.backward()
        optimizer.step()

    print()

    model.eval()
    y_pred = model(x_test)
    after_train = criterion(y_pred.squeeze(), y_test)
    print('Test loss after training: ', after_train.item())
    correct = 0
    for i in range(len(y_test)):
        if y_pred[i] == y_test[i]:
            correct += 1
    print('Test accuracy after training: ', correct / len(y_test))
    total_neg = 0
    false_neg = 0
    total_pos = 0
    false_pos = 0
    for i in range(len(y_test)):
        if y_pred[i] == 0:
            total_neg += 1
            if y_test[i] == 1:
                false_neg += 1
        else:
            total_pos += 1
            if y_test[i] == 0:
                false_pos += 1
    #print('Test false negative rate after training: ', false_neg / total_neg)
    #print('Test false positive rate after training: ', false_pos / total_pos)

    # FOR TRAINING SET
    print()
    y_pred = model(x_train)
    after_train = criterion(y_pred.squeeze(), y_train)
    print('Training set loss after training: ', after_train.item())
    correct = 0
    for i in range(len(y_train)):
        if y_pred[i] == y_train[i]:
            correct += 1
    print('Training set accuracy after training: ', correct / len(y_train))
    total_neg = 0
    false_neg = 0
    total_pos = 0
    false_pos = 0
    for i in range(len(y_train)):
        if y_pred[i] == 0:
            total_neg += 1
            if y_train[i] == 1:
                false_neg += 1
        else:
            total_pos += 1
            if y_train[i] == 0:
                false_pos += 1
    # print('Training set false negative rate after training: ', false_neg / total_neg)
    # print('Training set false positive rate after training: ', false_pos / total_pos)
