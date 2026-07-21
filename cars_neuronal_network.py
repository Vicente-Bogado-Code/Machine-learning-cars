import random
input_neurons = 5
hidden_layer_neurons = 6
output_neurons = 2
w1 = [[random.uniform(-1,1) for _ in range(input_neurons)] for _ in range(hidden_layer_neurons)]
w2 = [[random.uniform(-1,1) for _ in range(hidden_layer_neurons)] for _ in range(output_neurons)]
def forward_pass(input_neurons_values): 
    weighted_sum = [sum([w[i] * input_neurons_values[i] for i in range(len(input_neurons_values))]) for w in w1]
    print("weighted sum: ",weighted_sum)
    outputs = [sum([l[i] * weighted_sum[i] for i in range(hidden_layer_neurons)]) for l in w2]
    print("Output neurons: ",outputs)

    
input_neurons_values = [random.uniform(-1,1) for _ in range(5)]
forward_pass(input_neurons_values)
