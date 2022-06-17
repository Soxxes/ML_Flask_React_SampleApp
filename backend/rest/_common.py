import json
from flask import Response

# build the response
def get_response(obj, status=200):
    if type(obj) is dict:
        return Response(json.dumps(obj), mimetype="application/json", status=status)
    elif type(obj) is str:
        return Response(obj, mimetype="application/json", status=status)
    else:
        return Response(obj.to_json(), mimetype="application/json", status=status)
        