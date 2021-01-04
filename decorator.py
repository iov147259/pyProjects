import json

def to_json(func):
    result = func()
    return json.dumps(result)






