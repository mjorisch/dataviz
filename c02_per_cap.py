#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:56:00 2020

@author: michaeljorisch
"""

import csv
import pygal
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code

filename = 'c02_per_capita.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    countries, co2s = [], []
    for row in reader:
        try:
            current_country = row[0]
            current_co2 = float(row[58])
        except ValueError:
            print(current_country, 'missing data')
        else:
            countries.append(current_country)
            co2s.append(current_co2)

            
#Build a dictionary of c02 data
cc_co2s = {}
for country, co2 in zip(countries, co2s):
    code = get_country_code(country)
    carbon = co2
    if code and carbon:
        cc_co2s[code] = carbon
            

wm_style = RS('#336699', base_style = LCS)
wm = World(style=wm_style)
wm.title = 'World C02 per Capita in 2014, by Country (metric tons)'
wm.add('2014', cc_co2s)

wm.render_to_file('world_co2.svg')
        

        
            
    
    