import sys
import clipboard
import json


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(sys.agrv[1])
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_date(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load" :
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist. ")
    
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
    


