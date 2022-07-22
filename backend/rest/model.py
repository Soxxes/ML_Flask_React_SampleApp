from flask import request
from flask_restful import Resource
import numpy as np

from rest._common import get_response
from logic.linear_model import predict

class LinearModelApi(Resource):

    def post(self):
        x = int(request.get_json().get("X"))
        x = np.array(x)
        result = predict(x)
        return get_response({
            "prediction": result[0]
        })

    def get(self):
        return get_response({"msg": "worked"}, 200)
