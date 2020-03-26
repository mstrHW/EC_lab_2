from utils.read_data import create_matrix, read_tsp_file
from genetic_algorithm.main_loop import main_loop
from definitions import *

import numpy as np
import random

np.random.seed(14)
random.seed(14)


def main():
    files = ['pma343', 'xqf131', 'xqg237']
    file_name = files[2]
    data_file = file_name + '.tsp'
    experiment_path = os.path.join('experiments', file_name)
    make_dirs(experiment_path)

    images_dir = os.path.join(experiment_path, 'images')
    make_dirs(images_dir)

    matrix = create_matrix(data_file)
    coord = read_tsp_file(data_file)

    result = main_loop(
        matrix,
        coord,
        population_size=100,
        generations=5000,
        best_population=0.3,
        mutation_probability=0.4,
        verbose=1,
        show_plots=0,
        images_dir=images_dir,
    )
    print(result)


if __name__ == '__main__':
    main()
