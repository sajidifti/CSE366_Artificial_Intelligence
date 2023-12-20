# Assignment 7: Implementation of Genetic Algorithm to solve 8 Queen Problem
#
# Submitted By:
# Md. Sajid Anam Ifti
# ID: 2020-1-60-060
# 
# Md. Hasibur Rahman
# ID: 2020-1-60-068

import random


def generate_population(n):
    population = []

    while len(population) != n:
        sample = [random.randint(0, 63) for _ in range(8)]

        if sample not in population:
            population.append(sample)

    return population


def calculate_fitness(sample):
    fitness = 0

    for i in range(len(sample)):
        for j in range(i + 1, len(sample)):
            if sample[i] == sample[j]:
                fitness += 1

            elif abs(i - j) == abs(sample[i] - sample[j]):
                fitness += 1

    return 28 - fitness


def crossover(parent1, parent2):
    gene1 = random.randint(0, 7)
    gene2 = random.randint(gene1, 7)
    child = parent1[:gene1] + parent2[gene1:gene2] + parent1[gene2:]

    return child


def mutation(sample):
    gene = random.randint(0, 7)
    sample[gene] = random.randint(0, 7)

    return sample


def selection(population):
    fitness_arr = [calculate_fitness(sample) for sample in population]
    min_fitness = min(fitness_arr)
    min_fitness_index = fitness_arr.index(min_fitness)

    return population[min_fitness_index]


def genetic_algorithm(population):
    print("Initial Population:")

    for i in range(len(population)):
        print("sample No. {} = {}".format(i, population[i]))
        print("fitness = {}".format(calculate_fitness(population[i])))

    for i in range(100000):
        if i % 10000 == 0:
            print("iteration {}:".format(i))
            best_sample = selection(population)
            print("current best = {}".format(best_sample))
            print("fitness = {}".format(calculate_fitness(best_sample)))

        parent1, parent2 = random.sample(population, 2)
        child = crossover(parent1, parent2)

        if random.random() < 0.1:
            child = mutation(child)
        population.append(child)
    best_sample = selection(population)


if __name__ == "__main__":
    population = generate_population(6)
    genetic_algorithm(population)
