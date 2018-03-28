#!/usr/bin/env python
#coding: utf8 

from flask import Flask

webserver = Flask(__name__)
from webserver import resources
