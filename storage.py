import argparse
import tempfile
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--value')
args = parser.parse_args()
if args.value:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.isfile(storage_path):
        with open(storage_path, 'r+') as f:
            f.seek(0)
            current_dict = json.load(f)
            f.seek(0)
            f.truncate()
            if args.key in current_dict.keys():
                current_dict[args.key] = current_dict[args.key] + [args.value]
            else:
                current_dict[args.key] = [args.value]
            json.dump(current_dict, f)

    else:
        storage_path = os.path.join(tempfile.gettempdir(), storage_path)
        with open(storage_path, 'w+') as f:
            d = {args.key: [args.value]}
            json.dump(d, f)

else:
    storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
    if os.path.isfile(storage_path):
        with open(storage_path, "r") as f:
            f.seek(0)
            current_dictionary = json.load(f)
            if args.key in current_dictionary.keys():
                print(", ".join(current_dictionary[args.key]))
            else:
                print(None)
    else:
        print(None)













