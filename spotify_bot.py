# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:34:34 2020

@author: shivj
"""

from selenium import webdriver
from time import sleep

class spotify_bot:
    
    def __init__(self, user, pwd):
        self.user=user
        self.pwd=pwd
        self.driver=webdriver.Chrome()
        self.driver.get("https://open.spotify.com/")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/header/div[4]/button[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/div/input").send_keys(user)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/div/input").send_keys(pwd)
        sleep(4)
    
    def play(self,playlist):
        self.playlist=playlist
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/nav/ul/li[2]/div/a").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/header/div[3]/div/div/label/input").send_keys(playlist)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div/div/div/section[1]/div/div[2]/div/div/div/div[4]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/div[1]/section/div/div/div[1]/div/header/div[2]/div[2]/div[1]/button").click()   
        
login=spotify_bot("ENTER_EMAIL_ID","ENTER_PASSWORD")
login.play("ENTER_PLAYLIST")