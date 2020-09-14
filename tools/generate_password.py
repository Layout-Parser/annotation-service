import argparse
import json
import secrets
import os 

parser = argparse.ArgumentParser()
parser.add_argument('--path',      type=str, default='../data', help='the path to save row images')

def read_json(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

def write_json(data, filename):
    with open(filename, 'w') as fp:
        return json.dump(data, fp)

if __name__ == "__main__":
    args = parser.parse_args()
    
    config = read_json(os.path.join(args.path, 'config.json'))
    
    username = input("Please Type the user name\n")
    token = secrets.token_urlsafe(12)
    
    config['username'] = username
    config['password'] = token
    print("\n\n" + "==="*20 + '\n')
    print("The server config file has been updated:")
    print(f"Username: {username}")
    print(f"Password: {token}") 
    print("==="*20 + '\n')
    write_json(config, os.path.join(args.path, 'config.json'))