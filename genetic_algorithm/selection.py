import random


def yield_mating_pairs(pairs, population):
    for j in range(pairs):
        chosen = []
        for _ in range(2):
            selection_probability = random.random()
            for individ in population:
                if selection_probability >= individ._prob:
                    chosen.append(individ)
                    break
        if len(chosen) < 2:
            chosen.append(population[-1])
            if len(chosen) == 1:
                chosen.append(population[-2])
        yield chosen[0], chosen[1]


def selection(population, best_population):
    cumsum_fitness = 0
    for individ in population:
        cumsum_fitness += individ.fitness
        individ._prob = individ.fitness / cumsum_fitness
    return yield_mating_pairs(int(len(population) - int(len(population) * best_population)) // 2 + 1, population)
