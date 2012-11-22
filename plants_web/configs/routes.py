# -*- coding: utf-8 -*-
from plants_web.controllers import plants

ROUTES = [
    # {"url": "/", "method": "GET", "controller": general.home},
    {"url": "/plants/add", "method": "GET", "controller": plants.add_form},
    {"url": "/plants/add", "method": "POST", "controller": plants.add},
    {"url": "/plants/search", "method": "GET", "controller": plants.search_form},
    {"url": "/plants/search", "method": "POST", "controller": plants.search},
]
