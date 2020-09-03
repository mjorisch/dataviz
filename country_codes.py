#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:16:19 2020

@author: michaeljorisch
"""

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for given country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        #If the country code wasn't found return None.
    return country_codes.get(country_name)
country_codes = {
    'Yemen, Rep.': 'ye',
    'Venezuela, RB': 've',
    'Vietnam': 'vn',
    'Egypt, Arab Rep.': 'eg',
    'Bolivia': 'bo',
    'Congo, Dem. Rep.': 'cd',
    'Congo, Rep.': 'cg',
    'Dominica': 'do',
    'Gambia, The': 'gm',
    'Hong Kong SAR, China': 'hk',
    'Iran, Islamic Rep.': 'ir',
    'Korea, Dem. Rep.': 'kp',
    'Korea, Rep.': 'kr',
    'Lao PDR': 'la',
    'Libya': 'ly',
    'Macao SAR, China': 'mo',
    'Macedonia, FYR': 'mk',
    'Moldova': 'md',
    'Slovak Republic': 'sk',
    'Tanzania': 'tz',
}

