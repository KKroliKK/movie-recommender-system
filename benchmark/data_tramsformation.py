import sys

import pandas as pd
import numpy as np

sys.path.append("..")

from constants import NUM_MOVIES, NUM_USERS


def convert_raw_to_matrix(path: str) -> np.array:
    udata = pd.read_csv(path, sep="\t", header=None)
    udata.columns = ["user_id", "item_id", "rating", "timestamp"]

    udata = np.array(udata)
    udata = udata[:, :3]
    ratings = np.zeros((NUM_USERS, NUM_MOVIES))

    for user_id, film_id, rating in udata:
        ratings[user_id - 1][film_id - 1] = rating

    return ratings