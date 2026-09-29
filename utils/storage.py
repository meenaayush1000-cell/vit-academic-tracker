import json
import os

def save_json(filename, data):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
    except:
        print("Error saving data!")

def load_json(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except:
            pass
    return None
