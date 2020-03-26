import numpy as np


def generate_children(first_parent, second_parent, generated_indexes):
    min_idx = np.min(generated_indexes)
    max_idx = np.max(generated_indexes)

    children = np.zeros(len(first_parent))
    current_ix = 0
    _set = first_parent[min_idx:max_idx]
    for i, elem in enumerate(second_parent):
        if elem not in _set:
            if current_ix != min_idx:
                children[current_ix] = elem
            else:
                current_ix = max_idx
                children[current_ix] = elem
            current_ix += 1
    children[min_idx:max_idx] = _set

    return [int(i) for i in children]


def crossover(first_parent, second_parent):
    points_num = len(first_parent)
    generated_indexes = np.random.choice(points_num - 2, 2, replace=False)

    first_children = generate_children(first_parent, second_parent, generated_indexes)
    second_children = generate_children(second_parent, first_parent, generated_indexes)

    return first_children, second_children
