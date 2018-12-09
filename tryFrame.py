#!/usr/bin/env python

from selenium import webdriver
from time import sleep
import os

dr = webdriver.Firefox()
dr.get("file:///"+ os.path.abspath("main.html"))
dr.switch_to.frame("frame")
dr.find_element_by_id("input1").send_keys("testfan")
sleep(3)
dr.quit()