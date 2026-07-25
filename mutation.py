import math
import random
"""
IN THIS FILE: this file handles the mutation of the cars, calculates the fittest car and changes the weights of the others based on it.
"""
def mutation(car_list,car):
    travel_distances = [math.sqrt((c.x - c.originalX)**2 + (c.y - c.originalY)**2) for c in car_list]
    #Get the top1 references:
    fittest_car_distance = max(travel_distances)
    top1_fittest_car_index = travel_distances.index(fittest_car_distance)
    #Now top2
    travel_distances.pop(top1_fittest_car_index) 
    top2_fittest_car_distance = max(travel_distances)
    top2_fittest_car_index = travel_distances.index(top2_fittest_car_distance)
    #Top 1 weights:
    top1_fittest_car_w1 = car_list[top1_fittest_car_index].w1
    top1_fittest_car_w2 = car_list[top1_fittest_car_index].w2
    #Top 2 weights:
    top2_fittest_car_w1 = car_list[top2_fittest_car_index].w1
    top2_fittest_car_w2 = car_list[top2_fittest_car_index].w2
    mutation_strenght = 0.2
    mutated_w1 = []
    for row_index in range(len(car.w1)):
        new_row = []
        for i in range(len(car.w1[row_index])):
            rnmd_int = random.randint(0,2)
            if rnmd_int == 1:
                new_row.append(top1_fittest_car_w1[row_index][i] + random.uniform(-mutation_strenght, mutation_strenght))
            else:
                new_row.append(top2_fittest_car_w1[row_index][i] + random.uniform(-mutation_strenght,mutation_strenght))
        mutated_w1.append(new_row)    
    mutated_w2 = []
    for row_index in range(len(car.w2)):
            new_row = []
            for i in range(len(car.w2[row_index])):
                rnmd_int = random.randint(0,2)
                if rnmd_int == 1:
                    new_row.append(top1_fittest_car_w2[row_index][i] + random.uniform(-mutation_strenght, mutation_strenght))
                else:
                    new_row.append(top2_fittest_car_w2[row_index][i] + random.uniform(-mutation_strenght,mutation_strenght))
            mutated_w2.append(new_row)
    return mutated_w1, mutated_w2

def new_generation(car_list,car_parameter):
        for car in car_list:
            car.x = car.originalX
            car.y = car.originalY
            car.angle_in_degrees = 0
            car.dead = False
            new_w1, new_w2 = mutation(car_list,car_parameter)
            car.w1 = new_w1
            car.w2 = new_w2