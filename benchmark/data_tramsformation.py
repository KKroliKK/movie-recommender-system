import sys
from typing import Tuple

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

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


def split_raw_to_train_test(path: str, test_size: float = 0.2) -> Tuple[np.array, np.array]:
    udata = pd.read_csv(path, sep="\t", header=None)
    udata.columns = ["user_id", "item_id", "rating", "timestamp"]

    udata = np.array(udata)
    udata = udata[:, :3]

    train_ratings, test_ratings = train_test_split(udata, test_size=test_size)

    train = np.zeros((NUM_USERS, NUM_MOVIES))
    for user_id, film_id, rating in train_ratings:
        train[user_id - 1][film_id - 1] = rating

    test = np.zeros((NUM_USERS, NUM_MOVIES))
    for user_id, film_id, rating in test_ratings:
        test[user_id - 1][film_id - 1] = rating

    return train, test