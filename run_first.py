import os
import time
import sys
import fnmatch
import requests
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from setuptools.config import read_configuration
print('test')

conf_dict = read_configuration("/Users/jose.pacheco/PycharmProjects/setup.cfg")