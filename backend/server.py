from flask import Flask
from flask_restful import Api

from rest._routes import initialize_routes

# init flask app
app = Flask(__name__)

# get the routes
initialize_routes(Api(app))

# start app
if __name__ == "__main__":
    app.run(debug=True)
    