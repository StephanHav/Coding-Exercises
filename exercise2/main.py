import os
import json


def read_json(input_file):

    assert input_file.split('.')[-1] == "json", "Please give a JSON file as input file"
        
    # check if file exists, if not create it
    if not os.path.isfile(input_file):
            print("Specified JSON file does not exist")
            return
    
    # Open file in read mode
    with open(input_file, 'r') as content:
        data = json.load(content)

        print(data)

def main():

    read_json('exercise2/deps.json')
    

if __name__ == '__main__':
    main()