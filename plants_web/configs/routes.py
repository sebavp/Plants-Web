# -*- coding: utf-8 -*-
from plants_web.controllers import plants

ROUTES = [
    # {"url": "/", "method": "GET", "controller": general.home},
    {"url": "/plants/add", "method": "GET", "controller": plants.add_form},
    {"url": "/plants/add", "method": "POST", "controller": plants.add},
    {"url": "/plants/add_sample", "method": "GET", "controller": plants.add_sample_form},
    {"url": "/plants/add_sample", "method": "POST", "controller": plants.add_sample},
    {"url": "/plants/search", "method": "GET", "controller": plants.search_form},
    {"url": "/plants/search", "method": "POST", "controller": plants.search},
]
