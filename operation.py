#! /usr/bin/env python3

import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from db import list_db,display_puppet


def init_webdriver(puppet):
    useragent = puppet['useragent']
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", useragent)
    driver = webdriver.Firefox(profile)
    return driver


def save_cookies(driver, puppet, url):
    driver.get(url)
    _wait = input(f'[+] Sign up/log in to {url} then press Enter after logging in to save the cookie')
    cookie = driver.get_cookies()
    key = f'cookies@{url}'
    puppet[key] = cookie
    # save_puppet(puppet)
    print(f'[+] Cookie for {url} is saved.')


def load_cookies(driver, puppet): # Doesn't work well with LinkedIn
    for field in puppet:
        if "cookies@" in field:
            ActionChains(driver).key_down(Keys.COMMAND).send_keys(
                "t").key_up(Keys.COMMAND).perform()
            url = field.split('@')[1]
            driver.get(url)
            cookies = puppet[field]
            try:
                for cookie in cookies:
                    driver.add_cookie(cookie)
                driver.get(url)
                print(f'[+] Successfully load cookies for {url}')
            except Exception:
                print(f'[!] Error: Failed to load cookies for {url}')


def new_cookies(puppet):
    driver = init_webdriver(puppet)
    url = input('[+] Copy & paste url here: ')
    if 'http' in url:
        save_cookies(driver,puppet,url)
    else:
        print('[!] Invalid url')
        return None

# VI. Write puppet info to json file follow puppet's name
def save_puppet(puppet):
    filename = puppet.get("name")
    saveto = f'./puppets/{filename}.json'
    try:
        with open(saveto, 'w') as db:
            json.dump(puppet, db, indent=2)
    except FileNotFoundError:
        os.makedirs('./puppets')
        with open(saveto, 'w') as db:
            json.dump(puppet, db, indent=2)

    print(f"[+] Sock puppet: {filename} is updated.")
