import operator
from genetic_algorithm.mutation import mutation
from genetic_algorithm.crossover import crossover
from genetic_algorithm.selection import selection
from utils.visualize import *


import numpy as np


class Path:
    def __init__(self, path, fitness):
        self.path = path
        self.fitness = fitness
        self._prob = None

    def update_path(self, new_path, fitness):
        self.path = new_path
        self.fitness = fitness


def evaluate_fitness(matrix, path):
    dist = matrix[path[0]][path[-1]]
    for i in range(len(path) - 2):
        dist += matrix[path[i + 1]][path[i]]
    return dist


def generate_population(matrix, num_of_cities, population_size):
    population = []
    for _ in range(population_size):
        path = np.random.permutation([i for i in range(num_of_cities)])
        new_path = Path(path, evaluate_fitness(matrix, path))
        population.append(new_path)
    return population


def main_loop(matrix, coordinates, population_size=20, generations=1000, best_population=0.2, mutation_probability=0.2, verbose=1, show_plots=0, images_dir=None):
    num_of_cities = matrix.shape[0]
    population = generate_population(matrix, num_of_cities, population_size)
    population.sort(key=operator.attrgetter('fitness'), reverse=False)

    x, y = [], []
    for epoch in range(1, generations + 1):
        population.sort(key=operator.attrgetter('fitness'), reverse=False)
        new_generation = []

        for i in range(int(population_size * best_population)):
            new_generation.append(population[i])

        for i, j in selection(population, best_population):
            child_1, child_2 = crossover(i.path, j.path)
            new_generation.append(Path(child_1, evaluate_fitness(matrix, child_1)))
            new_generation.append(Path(child_2, evaluate_fitness(matrix, child_2)))
        population = new_generation[:population_size]

        for i in range(1, len(population)):
            new_path = mutation(population[i].path, mutation_probability)
            population[i].update_path(new_path, evaluate_fitness(matrix, new_path))

        population.sort(key=operator.attrgetter('fitness'), reverse=False)

        if verbose:
            if epoch % 100 == 0:
                print('Generation {}'.format(epoch))
                print('Fitness-value: {}\n'.format(population[0].fitness))

        x.append(epoch)
        y.append(population[0].fitness)

        if epoch % 1000 == 0:
            plot_path(population[0].path, coordinates, epoch, images_dir=images_dir, show_plots=show_plots)

    plot_convergence(x, y, images_dir=images_dir, show_plots=show_plots)

    return population[0].fitness
