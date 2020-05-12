#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, current_app, request, Request


app = Flask(__name__)


a = current_app
d = current_app.config['DEBUG']
