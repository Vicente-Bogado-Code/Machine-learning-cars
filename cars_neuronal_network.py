import random
import math
"""
IN THIS FILE:
This file will hanlde the car "brain" by giving it the functions to learn using a neuronal network with 5 input neurons, 6 hidden layer neurons and 2 output neurons.
-generate_weights() returns two list of lists that have each weight, w1 connects each input layer with each hidden layer neuron and w2 connects each hidden layer neuron with each output neuron
-forward_pass() returns the neuronal network output, a list with 2 numbers that will hande:
first number will handle how much each car rotates (-1 full right, 1 full left), and the second number how much will the car use to move forward (acceleration)
"""
input_neurons = 5
hidden_layer_neurons = 6
output_neurons = 2

def generate_weigths():
    w1 = [[random.uniform(-1,1) for _ in range(input_neurons)] for _ in range(hidden_layer_neurons)]
    w2 = [[random.uniform(-1,1) for _ in range(hidden_layer_neurons)] for _ in range(output_neurons)]
    return w1,w2
def forward_pass(input_neurons_values,w1,w2): 
    weighted_sum = [max(0,sum([w[i] * input_neurons_values[i] for i in range(len(input_neurons_values))])) for w in w1]
    outputs = [math.tanh(sum([l[i] * weighted_sum[i] for i in range(hidden_layer_neurons)])) for l in w2]
    return outputs