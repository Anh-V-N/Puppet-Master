#! /usr/bin/env python3

import json
import sys
import os
import random
from cmd import Cmd
from operation import save_puppet,new_cookies
import init
# I. List db
profiles = {}
def list_db():
    print('List of puppets')
    print('Index : Name')
    for key,value in profiles.items():
        key = str(key)
        print(key.center(5),":",value)
    print()

def index_db():
    global profiles
    try:
        ls = os.listdir('./Puppets')
        if len(ls) < 1:
            print('[!] There is no record! Please create a new one.')
            print('Automatically generating a random puppet! Please wait..')
            init.init_puppet()
            sys.exit()
        index = 1
        for record in ls:
            record = record.split('.json')[0]
            profiles[index] = record
            index += 1     
    except FileNotFoundError:
        print('[!] There is no record! Please create a new one.')
        print('Automatically generating a random puppet! Please wait..')
        init.init_puppet()
        sys.exit()

# II. Load record
def load(puppet):
    filename = f'./Puppets/{puppet}.json'
    try:
        with open(filename,'r') as db:      
            puppet = json.load(db)
        _u = puppet['useragent']
        return puppet
    except FileNotFoundError:
        print(f"[!] There is no puppet record of {filename}")
        return False
    except KeyError:
        print('[!] Useragent is missing. Generating a new one')
        puppet['useragent'] = set_agent()
        return puppet

# III. Display record
def display_puppet(puppet):
    for key,value in puppet.items():
        if 'cookies@' in key:
            print(key)
        else:
            print(key,":",value)
    print()

      
# IV. Modify info
def edit_info(ori_puppet):
    puppet = ori_puppet.copy()
    name = puppet['name']  
    class terminal(Cmd):  # Terminal for user input
        intro = ' Type "help" or "?" for more information.\n'        
        prompt = f"({name}) > "
        display_puppet(puppet)
        # Commands 
        def do_add(self, line):
            'Edit or add more info using key:value pair\nIf the key exists it will be updated, else a new field will be added\ne.g. add location:Earth'
            if ':' in line: 
                line = line.split(':')
                key = line[0].strip()
                value = line[1].strip()
                puppet[key] = value
            else:
                print("[!] Invalid syntax")
        def do_remove(self, line): 
            'Remove 1 or more fields of info(For name, you can only modify using add)\ne.g. remove dob email inbox'
            keys = line.split(' ')
            for i in keys:
                if i in puppet and i !='name':
                    puppet.pop(i)
                    print(f'[+] Field {i} is removed')              
        def do_show(self,line): 
            'Display all information of the puppet '
            display_puppet(puppet)
        def do_cookies(self,line):
            'Add cookies to puppet'
            new_cookies(puppet)
        def do_save(self,line):
            'Save the changes'
            save_puppet(puppet)
        def do_agent(self,line):
            'Randomly choose an user-agent from useragents.txt'
            puppet['useragent'] = set_agent()
        def do_exit(self, line):
            'Exit the shell.'
            if puppet != ori_puppet:
                save = input('[?] Do you want to save the changes? ')
                if save.lower().startswith('y'):
                    save_puppet(puppet)
            return True           
    terminal().cmdloop()

# V. Remove record
def remove(name):
    filename = f'./Puppets/{name}.json'
    try:
        os.remove(filename)
        print(f'[+] Removed puppet {name}')
    except Exception as e:
        print(e)
    
# Get random useragent from useragents.txt
def set_agent():
    with open('useragents.txt') as f:
        agents = f.readlines()
    agent = random.choice(agents).strip()
    while True: # Deal with empty line 
        if agent == '':
            agent = random.choice(agents).strip()
        else:
            break  
    return agent
