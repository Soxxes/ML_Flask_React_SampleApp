from flask import Flask
from flask_restful import Api
from argparse import ArgumentParser

from rest._routes import initialize_routes

# init flask app
app = Flask(__name__)

# parse command line arguments (for docker)
parser = ArgumentParser()
parser.add_argument("--host", help="Serve the host ip", required=False)

args = parser.parse_args()


# get the routes
initialize_routes(Api(app))

# start app
if __name__ == "__main__":
    # app.run(debug=True)
    if args.host:
        app.run(debug=False, host=args.host)
    else:
        app.run(debug=False, host="127.0.0.1")

    