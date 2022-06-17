from rest.model import LinearModelApi

def initialize_routes(api):
    api.add_resource(LinearModelApi, "/predict")
