import numpy as np
from scipy.spatial.distance import euclidean

from definitions import *


def read_tsp_file(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path) as f:
        while f.readline() != 'TYPE : TSP\n':
            pass
        points_count = int(f.readline().split(':')[1])
        while f.readline() != 'NODE_COORD_SECTION\n':
            pass
        coord = np.zeros(shape=(points_count, 2))
        for i in range(points_count):
            coord[i] = f.readline().split()[1:]
    return coord


def create_matrix(file_name):
    coord = read_tsp_file(file_name)
    file_path = os.path.join(DATA_DIR, '{}_matrix.npy'.format(file_name.split()[0]))
    try:
        matrix = np.load(file_path)
    except IOError:
        matrix = np.zeros((len(coord), len(coord)))
        for i in range(len(coord)):
            for j in range(len(coord)):
                matrix[i][j] = euclidean(coord[i], coord[j])
        np.save(file_path, matrix)

    return matrix
