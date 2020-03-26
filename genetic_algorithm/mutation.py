import numpy as np
import random


def mutation(individ, mutation_probability):
    if random.random() > mutation_probability:
        return individ

    idx = np.random.choice(len(individ) + 1, 2, replace=False)
    min_idx = min(idx)
    max_idx = max(idx)

    sub = individ[min_idx:max_idx]
    sub = np.array(list(reversed(sub)))
    individ[min_idx:max_idx] = sub

    return individ
