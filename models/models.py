import numpy as np
from numpy import dot
from numpy.linalg import norm


class Model:
    def fit(self, ratings):
        pass

    def predict(self, user_id):
        pass


class RandomModel(Model):
    def __init__(self, max_score = 5) -> None:
        self.max_score = max_score
    
    def fit(self, ratings):
        self.shape = ratings.shape[1]

    def predict(self, user_id):
        prediction = np.random.random(self.shape) * self.max_score

        return prediction
    

class AvgModel(Model):
    def get_avg_film_ratings(self, film_id, ratings):
        all_ratings = ratings[:, film_id][ratings[:, film_id] != 0]
        if len(all_ratings) == 0:
            avg_rating = 0
        else:
            avg_rating = np.average(all_ratings)

        return avg_rating
    

    def fit(self, ratings):
        self.avg = [self.get_avg_film_ratings(film_id, ratings) for film_id in range(ratings.shape[1])]
        self.avg = np.array(self.avg)

    def predict(self, user_id):
        return self.avg


class ColaborativeModel(Model):
    cos_sim = lambda a, b: dot(a, b) / (norm(a) * norm(b))

    def __init__(self, num_users: int = 30) -> None:
        self.num_users = num_users

    def fit(self, ratings):
        self.ratings = ratings

    def predict(self, user_id):
        user_ratings = self.ratings[user_id]
        similarities = np.array([ColaborativeModel.cos_sim(user_ratings, rating) for rating in self.ratings])
        closest_users = list(reversed(np.argsort(similarities)))
        closest_users = closest_users[1:self.num_users + 1]
        
        closest_similarities = similarities[closest_users]
        sum_closest_similarities = sum(closest_similarities)

        closest_ratingss = self.ratings[closest_users]

        prediction = np.sum((closest_ratingss * closest_similarities[:, None]), axis=0) / sum_closest_similarities

        return prediction