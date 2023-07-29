import os
import json
import chardet

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

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def main():

    encoding = detect_file_encoding('deps.json')
    print(f"The encoding of deps.json is: {encoding}")
    #read_json('deps.json')
    

if __name__ == '__main__':
    main()