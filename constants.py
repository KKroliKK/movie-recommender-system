import os
import json

DATSET_PATH = os.path.join("..", "data", "raw", "ml-100k")
UDATA_PATH = os.path.join(DATSET_PATH, "u.data")
UINFO_PATH = os.path.join(DATSET_PATH, "u.info")
UITEM_PATH = os.path.join(DATSET_PATH, "u.item")
UGENRE_PATH = os.path.join(DATSET_PATH, "u.genre")
UUSER_PATH = os.path.join(DATSET_PATH, "u.user")

U1BASE_PATH = os.path.join(DATSET_PATH, "u1.base")
U1TEST_PATH = os.path.join(DATSET_PATH, "u1.test")

INTERIM_PATH = os.path.join("..", "data", "interim")
RATINGS_PATH = os.path.join(INTERIM_PATH, "ratings")

NUM_RATINGS = 100_000
NUM_USERS = 943
NUM_MOVIES = 1682

PARAMS_PATH = os.path.join("..", "models", "params.json")
params = open(PARAMS_PATH)
params = json.load(params)
NUM_USERS_COLLABORATIVE = params["num_users"]