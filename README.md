# Deploy a Machine Learning Model with Flask and a ReactJS Frontend
When I started with the webdevelopment and machine learning stuff I felt overwhelmed by all the tutorials and guides available. This repository demonstrates how you could easily deploy a ML model with flask and react. Here are some really useful tutorials in case you don't want to clone the repository and do it all by yourself:
- [How to connect Flask and React](https://www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/)
- [Save and Load ML Models with Pickle](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/)

Please note I am neither an expert in React nor Flask. But this should give you a good starting point.

</br>

## Step-By-Step Guide

Let's start by creating a basic ReactJS App:</br>
`$ create-react-app frontend react_flask_app --skip-git` </br>

... this takes a few seconds.
</br>

Next, built the Flask Backend:</br>
`$ mkdir backend`</br>

Create a virtual environment:</br>
`$ cd backend`</br>
`$ python -m venv flask-react-venv`</br>
`$ pip install -r requirements.txt`</br>

The frontend will run on port 3000 and the backend on port 5000. Add the following to your package.json (in frontend folder):
`"proxy":"http://localhost:5000/",`</br>
... and don't forget the `,` at the end of the line.

Now you are ready to do what ever you like in the backend and frontend. To start the backend server, type:</br>
`python server.py`</br>
and to start the frontend, type:</br>
`npm start`</br>
... both commands in their suitable folder.


## The ML Model
Here is the code of the ML Model I used. It is just a simple Linear Regression Model with some toy data:</br>
```
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle

# true underlying model
m, n = 2.3, -3
x = np.linspace(0, 50, 300)
# add some noise
y = m*x + n + np.random.normal(loc=4, scale=16, size=300)

x = x.reshape(-1, 1)
plt.scatter(x, y)
plt.show()

reg = linear_model.LinearRegression()
# train the model
reg.fit(x, y)
print(reg.coef_[0], reg.intercept_)

# test for any arbitrary value
print("predicted:", reg.predict(np.array([20]).reshape(-1, 1))[0], ", should be:", 20 * m + n)

# save the model
with open("model.pkl", "wb") as f:
    pickle.dump(reg, f)
```
the toy data:</br>
[![model.png](https://i.postimg.cc/XvNK5x5y/model.png)](https://postimg.cc/9DSq5dJW)


## Result
At the end you will get something like this:</br>
[![frontend.png](https://i.postimg.cc/3RxHPMvJ/frontend.png)](https://postimg.cc/sBq8hNmt)

By entering a number and clicking the button you will receive a prediction from the model. Let's quickly check if the example makes sense: </br>
$$ y = 2.3 \cdot 31 - 3 =  68.3 $$

That's okay since the model used 2.283 and -0.947 as parameters. Why is the second paramter so bad? Because the noise we were adding is not zero-mean. But it doesn't matter here, you can take any other model if you want.

## Dockerize It
If you now want to run the frontend and backend in separate Docker Containers, you will find a Dockerfile in both folders. With that you can follow the instructions below.
### Frontend
`$ cd frontend`</br>
`$ docker build -t <image_name> .`</br>
`$ docker run --name <container_name> -p 3000:3000 <image_name>`

### Backend
`$ cd backend`</br>
`$ docker build -t <image_name> .`</br>
`$ docker run --name <container_name> -p 5000:5000 <image_name>`

### Check if it works
`$ docker ps`

[![Unbenannt.png](https://i.postimg.cc/GmMFH8gW/Unbenannt.png)](https://postimg.cc/YvWGP9HR)

I added the suffix "-cont" to make it clear to the reader that this is the container and not the image. Next, we need to set up a Docker Compose File to let the Frontend and Backend communicate with each other, because just two single Docker containers are pretty useless.

