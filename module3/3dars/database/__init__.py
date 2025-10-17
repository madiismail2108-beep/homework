import json

file_path='pro.json'

def load_data():
    try:
        with open(file_path) as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        return {}

def save_detail(data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)