import torch

class FeedforwardModel(torch.nn.Module):
        def __init__(self, input_size, hidden_size1, hidden_size2, hidden_size3):
            super(FeedforwardModel, self).__init__()
            self.input_size = input_size
            self.hidden_size1  = hidden_size1
            self.hidden_size2  = hidden_size2
            self.hidden_size3  = hidden_size3
            self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size1)
            self.relu = torch.nn.ReLU()
            self.fc2 = torch.nn.Linear(self.hidden_size1, self.hidden_size2)
            self.relu2 = torch.nn.ReLU()
            self.fc3 = torch.nn.Linear(self.hidden_size2, self.hidden_size3)
            self.relu3 = torch.nn.ReLU()
            self.fc4 = torch.nn.Linear(self.hidden_size3, 1)
            self.sigmoid = torch.nn.Sigmoid()
        def forward(self, x):
            hidden = self.fc1(x)
            relu = self.relu(hidden)
            hidden2 = self.fc2(relu)
            relu2 = self.relu2(hidden2)
            hidden3 = self.fc3(relu2)
            relu3 = self.relu3(hidden3)
            output = self.fc4(relu3)
            output = self.sigmoid(output)
            return output
