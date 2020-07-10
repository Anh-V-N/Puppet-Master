
import random

def set_agent():
    with open('useragents.txt') as f:
        agents = f.readlines()
    agent = random.choice(agents)
    return agent

# Tested
# a = set_agent()
# print(a)
from init import Puppet
from db import save_puppet, set_agent
import requests, json

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
    puppet = vars(puppet)
    return puppet

puppet = random_puppet()
# print(puppet)
# print(type(puppet))

save_puppet(puppet)
