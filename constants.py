import os

DATSET_PATH = os.path.join("..", "data", "raw", "ml-100k")
UDATA_PATH = os.path.join(DATSET_PATH, "u.data")
UINFO_PATH = os.path.join(DATSET_PATH, "u.info")
UITEM_PATH = os.path.join(DATSET_PATH, "u.item")
UGENRE_PATH = os.path.join(DATSET_PATH, "u.genre")
UUSER_PATH = os.path.join(DATSET_PATH, "u.user")

INTERIM_PATH = os.path.join("..", "data", "interim")
RATINGS_PATH = os.path.join(INTERIM_PATH, "ratings")

NUM_RATINGS = 100_000
NUM_USERS = 943