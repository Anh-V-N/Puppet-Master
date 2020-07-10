#! /usr/bin/env python3

import json
import requests
import sys
import random
from db import edit_info, set_agent
from operation import save_puppet

class Puppet:
    def __init__(self,name, dob, email, inbox, useragent):
        self.name = name
        self.dob = dob
        self.email = email
        self.inbox = inbox
        self.useragent = useragent
        # self.location = location
    


# Generate random identity using namefake
def random_puppet():
    with requests.get("https://api.namefake.com/") as api:
        namefake = json.loads(api.text)
    agent = set_agent()
    puppet = Puppet(namefake['name'], namefake['birth_data'],
                    f"{namefake['email_u']}@{namefake['email_d']}", f"https:{namefake['email_url']}", agent)
    print('Generated puppet is as of following:')
    print(f'[+] name: {puppet.name}')
    print(f'[+] dob: {puppet.dob}')
    print(f'[+] email: {puppet.email}')
    print(f'[+] inbox: {puppet.inbox}')
    print(f'[+] useragent: {puppet.useragent}')
    return puppet


# Manually input puppet info
def manual_puppet(puppet):
    # os.system("cls||clear")
    name = input(f'name[{puppet.name}] : ')
    if name == '':
        name = puppet.name
    dob = input(f'dob[{puppet.dob}] : ')
    if dob == '':
        dob = puppet.dob
    email = input(f'email[{puppet.email}] : ')
    if email == '':
        email = puppet.email

    if email != puppet.email:
        inbox = None
    else:
        inbox = puppet.inbox      
    useragent = input(f'useragent[{puppet.useragent}] : ')
    if useragent == '':
        useragent = puppet.useragent
    puppet = Puppet(name, dob, email, inbox, useragent)
    puppet = vars(puppet)

    return puppet



def init_puppet():
    puppet = random_puppet()
    create_puppet = input('[?] Do you want to use this puppet?(Y/N) ').strip().lower()
    if create_puppet.startswith('n'):        
        puppet = manual_puppet(puppet)
        if puppet.inbox != None:
            print(f'[+] inbox: {puppet.inbox}')
    else:
        pass
    puppet = vars(puppet) # Turn the puppet class object to dict

    add_info = input("[?] Do you want to edit/add more info?(Y/N) ").strip().lower()
    if add_info.startswith('n'):
        save_puppet(puppet)
    else:
        edit_info(puppet)
    return(puppet)
