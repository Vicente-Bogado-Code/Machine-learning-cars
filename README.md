# Neuroevolution Car Simulation

A 2D car racing simulation where cars learn to navigate a track using a neural
network "brain" trained entirely through a genetic algorithm. No
backpropagation, no gradient descent, and no external ML libraries. Every part
of this project, from the car physics to the neural network math to the
evolutionary training loop, is built from scratch in pure Python.

## What's happening here

Each car is controlled by a small neural network that takes 5 raycast sensor
readings as input (front, left, right, and two diagonals) and outputs 2
values: how much to steer, and how much to accelerate. Cars start with
completely random weights and no idea how to drive.

This project uses Neuroevolution:

1. A population of cars attempts to drive the track using their current weights
2. Each car's fitness is measured by how far it travels from its starting
   position before crashing
3. The top 2 performing cars are selected as parents for the next generation
4. Each new car's weights are built by randomly choosing, per weight, between
   the top 1 and top 2 parent's value, then adding a small random mutation
5. Repeat, generation after generation, until the population reliably
   completes the track

No car is ever told the "correct" way to drive. Improvement emerges purely
from selection pressure on random variation across generations, usually takes 40 - 80 generations until they properly learn how to drive,

## Running it

```bash
python cars_rendering.py
```

Project structure

- `cars_rendering.py` — main file: game loop, car class, physics, raycasting,
  and collision detection
- `cars_neuronal_network.py` — weight initialization, the forward pass, and
  the pretrained model's saved weights
- `mutation.py` — fitness evaluation, selection, crossover, and mutation
  logic for producing each new generation
- `draw_tracks.py` — wall/track layout definitions

