import numpy as np
from sklearn.model_selection import train_test_split

filetxt = np.loadtxt('seeds_dataset.txt', dtype=float)
np.random.shuffle(filetxt)

train_data, test_data = train_test_split(filetxt, test_size=0.2)

X_train = train_data[:, :-1]
y_train = train_data[:, -1]
X_test = test_data[:, :-1]
y_test = test_data[:, -1]

input_size = X_train.shape[1]
hidden_size = 5
output_size = len(np.unique(y_train))
learning_rate = 0.01
epochs = 1000

weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))

def calculate_sigmoid(x):
    return 1 / (1 + np.exp(-x))

def calculate_simoid_derivative(x):
    return calculate_sigmoid(x) * (1 - calculate_sigmoid(x))

def error(true, pred):
    return np.mean((true - pred)**2)

def forward(x, weights_input, weights_output):

    hidden_input = np.dot(x,weights_input)
    hidden_output = calculate_sigmoid(hidden_input)

    output_input = np.dot(hidden_output, weights_output)
    output = calculate_sigmoid(output_input)

    return hidden_output, output

hidden_output, output = forward(X_train, weights_input_hidden, weights_hidden_output)
print(hidden_output)
print(output)