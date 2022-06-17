import pickle

def predict(x):
    model = pickle.load(open('logic/model.pkl','rb'))
    result = model.predict(x.reshape(-1, 1))
    return result
