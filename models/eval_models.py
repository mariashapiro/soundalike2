import numpy as np
from sklearn.model_selection import ParameterGrid
import implicit
from implicit.evaluation import precision_at_k, train_test_split

from recommender import Recommender
import utils

rand_state = np.random.RandomState(1)

listen_mat = utils.pickle_load('data/listen_matrix.pkl')
train, test = train_test_split(listen_mat, train_percentage=0.8, random_state=rand_state)

als_grid_list = list(ParameterGrid({
    'factors': [50, 100, 150],
    'regularization':[0.001, 0.01, 0.1],
    'iterations': [10, 20, 30]
}))

lmf_grid_list = list(ParameterGrid({
    'factors': [60],
    'learning_rate': [0.1, 1.0, 10.0],
    'regularization': [1.0, 5.0, 10.0],
}))

def eval_model(type, params_grid):
    for i in range(len(params_grid)):
        params = params_grid[i]
        rec = Recommender(type=type, params=params, load=False)
        rec.model.fit(train)
        prec = precision_at_k(rec.model, train, test, K=10)
        print(prec)

# WARNING! May take several hours to run
eval_model('als', als_grid_list)
eval_model('lmf', lmf_grid_list)
