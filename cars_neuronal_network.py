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
def pre_trained_model():
    w1 = [[-0.5612649353146966, -1.5857685294519417, 0.9477923762994517, -1.5755669235229328, 1.5517888320050188], [-0.200024845496113, -0.28878923175335575, 1.2770140393383373, 1.0677229098061032, 0.7344021648679355], [-2.7013787265833513, 0.831403033694068, -0.750342316295, -0.7252892770806829, 0.53787877783724], [0.7066586878998831, -1.4406167809121244, 2.1015596355907555, 0.10973027635607412, 0.9659311191131521], [0.8265805717557644, -2.019212924553034, 1.0997701735136243, 2.5072721848750295, -1.072645618800964], [0.07610851499255047, 0.4344501796537151, 0.8973541503023397, -1.8283880889272868, -0.5748420755468312]]

    w2 = [[-0.6379763000047467, 0.4534397420067342, -1.0314448446245033, -1.5063337713651084, 2.0131499636691155, -0.19180067428476302], [1.0924796642417005, 1.416630321327378, 1.9444412573396639, -1.2534630283314412, 0.32315969919184195, 1.5629961743501108]]
    return w1, w2