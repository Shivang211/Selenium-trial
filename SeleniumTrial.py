from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('/Users/shivanggupta/Downloads/chromedriver')

driver.get('https://hoopshype.com/salaries/players/')